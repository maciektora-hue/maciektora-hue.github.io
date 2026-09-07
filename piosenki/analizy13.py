from collections import Counter, defaultdict
from itertools import combinations

from statystyki import build_chunks, legend, svg_chart


DIRECTION_TAGS = [
    "do-siebie",
    "do-innych",
    "do-swiata",
    "ku-przeszlosci",
    "ku-przyszlosci",
    "ku-komus",
    "od-kogos",
    "ku-swiatu",
    "od-swiata",
]


def _top(counter, limit=10, labels=None):
    labels = labels or {}
    return [
        {"name": name, "label": labels.get(name, name).replace("-", " "), "count": count}
        for name, count in counter.most_common(limit)
    ]


def _chunk_index(order, chunk_size, n):
    try:
        i = (int(order) - 1) // chunk_size
    except (TypeError, ValueError):
        return None
    return i if 0 <= i < n else None


def _pair_counts(sets, limit=12):
    counts = Counter()
    for values in sets:
        for a, b in combinations(sorted(values), 2):
            counts[(a, b)] += 1
    return [
        {"a": a.replace("-", " "), "b": b.replace("-", " "), "count": count}
        for (a, b), count in counts.most_common(limit)
    ]


def build_13_analyses(model, chunk_size=80):
    chunks = build_chunks(model, chunk_size)
    labels = [c["label"] for c in chunks]
    n = len(chunks)

    axis_labels = {row["axis_name"]: row.get("label") or row["axis_name"] for row in model["axes"]}
    family_labels = {row["family_name"]: row.get("label") or row["family_name"] for row in model["families"]}

    tag_counts = Counter(event["tag_key"] for event in model["events"])
    axis_counts = Counter()
    family_counts = Counter()
    for event in model["events"]:
        axis_counts.update(event["axis_names"])
        family_counts.update(event["family_names"])

    valence_by_tag = model.get("valence_by_tag", {})

    valence_counts = Counter()
    unresolved = 0
    direction_counts = Counter()
    for event in model["events"]:
        valence = valence_by_tag.get(event["tag_key"])
        if valence is None:
            unresolved += 1
        else:
            valence_counts[valence] += 1
        if event["tag_key"] in DIRECTION_TAGS:
            direction_counts[event["tag_key"]] += 1

    resolved = sum(valence_counts.values())
    total_valence = resolved + unresolved
    valence = {
        "negative": valence_counts[-1],
        "neutral": valence_counts[0],
        "positive": valence_counts[1],
        "unresolved": unresolved,
        "coverage_pct": 100.0 * resolved / total_valence if total_valence else 0.0,
    }

    top_tags = [name for name, _ in tag_counts.most_common(6)]
    tag_series = []
    for name in top_tags:
        values = [chunk["tags"].get(name, 0) for chunk in chunks]
        tag_series.append({"name": name, "label": name.replace("-", " "), "values": values})

    top_axes = [name for name, _ in axis_counts.most_common(6)]
    axis_series = []
    for name in top_axes:
        values = [chunk["axes"].get(name, 0) for chunk in chunks]
        axis_series.append({"name": name, "label": axis_labels.get(name, name), "values": values})

    valence_series = [
        {"name": "negative", "label": "nieprzyjemne", "values": [0] * n},
        {"name": "neutral", "label": "neutralne", "values": [0] * n},
        {"name": "positive", "label": "przyjemne", "values": [0] * n},
    ]
    direction_top = [name for name, _ in direction_counts.most_common(6)]
    direction_series = [
        {"name": name, "label": name.replace("-", " "), "values": [0] * n}
        for name in direction_top
    ]
    direction_series_by_name = {item["name"]: item for item in direction_series}

    per_chunk_valence = [Counter() for _ in chunks]
    per_chunk_direction = [Counter() for _ in chunks]
    for event in model["events"]:
        i = _chunk_index(event["spotify_order"], chunk_size, n)
        if i is None:
            continue
        valence_value = valence_by_tag.get(event["tag_key"])
        if valence_value is not None:
            per_chunk_valence[i][valence_value] += 1
        if event["tag_key"] in DIRECTION_TAGS:
            per_chunk_direction[i][event["tag_key"]] += 1

    for i in range(n):
        valence_series[0]["values"][i] = per_chunk_valence[i][-1]
        valence_series[1]["values"][i] = per_chunk_valence[i][0]
        valence_series[2]["values"][i] = per_chunk_valence[i][1]
        for name in direction_top:
            direction_series_by_name[name]["values"][i] = per_chunk_direction[i][name]

    changes = []
    if len(chunks) >= 2:
        newest, oldest = chunks[0], chunks[-1]
        names = set(newest["tags"]) | set(oldest["tags"])
        newest_total = newest["tag_total"] or 1
        oldest_total = oldest["tag_total"] or 1
        for name in names:
            new_pct = 100.0 * newest["tags"].get(name, 0) / newest_total
            old_pct = 100.0 * oldest["tags"].get(name, 0) / oldest_total
            changes.append({"tag": name.replace("-", " "), "delta": new_pct - old_pct})
        changes.sort(key=lambda row: abs(row["delta"]), reverse=True)
        changes = changes[:12]

    tag_sets = list(model["tags_by_song"].values())
    axes_by_song = defaultdict(set)
    for event in model["events"]:
        axes_by_song[event["lyrics_id"]].update(event["axis_names"])

    relations = []
    for i, chunk in enumerate(chunks):
        vc = per_chunk_valence[i]
        valence_name = max(
            [(vc[-1], "nieprzyjemna"), (vc[0], "neutralna"), (vc[1], "przyjemna")],
            default=(0, "brak"),
        )[1]
        axis_name = chunk["axes"].most_common(1)[0][0] if chunk["axes"] else None
        direction_name = per_chunk_direction[i].most_common(1)[0][0] if per_chunk_direction[i] else None
        relations.append({
            "label": chunk["label"],
            "valence": valence_name,
            "axis": axis_labels.get(axis_name, axis_name or "brak"),
            "direction": (direction_name or "brak").replace("-", " "),
        })

    return {
        "chunk_size": chunk_size,
        "top_tags": _top(tag_counts, 12),
        "top_axes": _top(axis_counts, 12, axis_labels),
        "families": _top(family_counts, 10, family_labels),
        "valence": valence,
        "directions": _top(direction_counts, 12),
        "tag_time_chart": svg_chart(labels, tag_series),
        "tag_time_legend": legend(tag_series),
        "axis_time_chart": svg_chart(labels, axis_series),
        "axis_time_legend": legend(axis_series),
        "valence_time_chart": svg_chart(labels, valence_series),
        "valence_time_legend": legend(valence_series),
        "direction_time_chart": svg_chart(labels, direction_series),
        "direction_time_legend": legend(direction_series),
        "changes": changes,
        "tag_pairs": _pair_counts(tag_sets, 12),
        "axis_pairs": _pair_counts(list(axes_by_song.values()), 12),
        "relations": relations,
    }
