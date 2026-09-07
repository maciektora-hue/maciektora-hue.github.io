import html
import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VALUES_PATH = ROOT / "dane-analityczne" / "tag-wartosci.json"
PALETTE = ["#315f73", "#7a5c85", "#8a6a3b", "#4f6f52", "#8b4b3f", "#5d5d5d"]


def key(value):
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return text.casefold().strip()


def base_tag(tag):
    return str(tag or "").strip().split(":", 1)[0].strip()


def parse_tags(value):
    if value is None:
        return []
    text = str(value).strip()
    if not text:
        return []
    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return [str(x).strip() for x in parsed if str(x).strip()]
    except Exception:
        pass
    cleaned = re.sub(r"^\s*[\[\(\{]", "", text)
    cleaned = re.sub(r"[\]\)\}]\s*$", "", cleaned)
    return [
        part.strip().strip("'\"")
        for part in re.split(r"[,;|\n]+", cleaned)
        if part.strip().strip("'\"")
    ]


def fetch(conn, sql, columns):
    return [dict(zip(columns, row)) for row in conn.execute(sql).fetchall()]


def load_model(conn):
    songs = fetch(
        conn,
        """
        SELECT lyrics_id, spotify_order, title_original, artist_original
        FROM middle_end
        WHERE spotify_order IS NOT NULL
        ORDER BY spotify_order
        """,
        ["lyrics_id", "spotify_order", "title_original", "artist_original"],
    )
    snapshots = fetch(
        conn,
        "SELECT lyrics_id, tagged_at, tags FROM tag_snapshots ORDER BY tagged_at, lyrics_id",
        ["lyrics_id", "tagged_at", "tags"],
    )
    tag_axes = fetch(
        conn,
        "SELECT tag, axis_name FROM tag_axis ORDER BY tag, axis_name",
        ["tag", "axis_name"],
    )
    axes = fetch(
        conn,
        "SELECT axis_name, label, description, family_name, sort_order FROM axes ORDER BY sort_order",
        ["axis_name", "label", "description", "family_name", "sort_order"],
    )
    families = fetch(
        conn,
        "SELECT family_name, label, color_hex, description, sort_order FROM families ORDER BY sort_order",
        ["family_name", "label", "color_hex", "description", "sort_order"],
    )

    song_by_lyrics = {row["lyrics_id"]: row for row in songs if row.get("lyrics_id")}
    axes_by_tag = defaultdict(list)
    for row in tag_axes:
        axes_by_tag[key(row["tag"])].append(row["axis_name"])
    family_by_axis = {row["axis_name"]: row["family_name"] for row in axes}

    events = []
    tags_by_song = defaultdict(set)
    for snapshot in snapshots:
        song = song_by_lyrics.get(snapshot.get("lyrics_id"))
        if not song:
            continue
        try:
            order = int(song["spotify_order"])
        except (TypeError, ValueError):
            continue
        for raw_tag in parse_tags(snapshot.get("tags")):
            tag = base_tag(raw_tag)
            tag_key = key(tag)
            if not tag_key:
                continue
            axis_names = list(axes_by_tag.get(tag_key, []))
            family_names = sorted({family_by_axis[a] for a in axis_names if a in family_by_axis})
            events.append({
                "lyrics_id": song["lyrics_id"],
                "spotify_order": order,
                "tag": tag,
                "tag_key": tag_key,
                "axis_names": axis_names,
                "family_names": family_names,
            })
            tags_by_song[song["lyrics_id"]].add(tag_key)

    max_order = max((int(row["spotify_order"]) for row in songs), default=0)
    return {
        "songs": songs,
        "events": events,
        "tags_by_song": dict(tags_by_song),
        "axes": axes,
        "families": families,
        "max_order": max_order,
    }


def build_chunks(model, size=80):
    if model["max_order"] <= 0:
        return []
    n = (model["max_order"] + size - 1) // size
    chunks = []
    for i in range(n):
        start = i * size + 1
        end = min((i + 1) * size, model["max_order"])
        chunks.append({
            "label": f"{start}–{end}",
            "tag_total": 0,
            "tags": Counter(),
            "axes": Counter(),
            "families": Counter(),
        })
    for event in model["events"]:
        i = (event["spotify_order"] - 1) // size
        if i < 0 or i >= len(chunks):
            continue
        chunk = chunks[i]
        chunk["tag_total"] += 1
        chunk["tags"][event["tag_key"]] += 1
        for axis_name in event["axis_names"]:
            chunk["axes"][axis_name] += 1
        for family_name in event["family_names"]:
            chunk["families"][family_name] += 1
    return chunks


def percent_series(chunks, bucket, names):
    return {name: [100.0 * chunk[bucket].get(name, 0) / (chunk["tag_total"] or 1) for chunk in chunks] for name in names}


def count_series(chunks, bucket, names):
    return {name: [chunk[bucket].get(name, 0) for chunk in chunks] for name in names}


def top_names(chunks, bucket, limit=6):
    total = Counter()
    for chunk in chunks:
        total.update(chunk[bucket])
    return [name for name, _ in total.most_common(limit)]


def svg_chart(labels, series, colors=None, width=920, height=320):
    if not labels or not series:
        return "<p>Brak danych do wykresu.</p>"
    left, right, top, bottom = 52, 18, 20, 52
    iw, ih = width - left - right, height - top - bottom
    all_values = [float(v) for item in series for v in item["values"]]
    max_y = max(all_values, default=1.0) or 1.0

    def xpos(i):
        return left + (iw / 2 if len(labels) == 1 else iw * i / (len(labels) - 1))

    def ypos(v):
        return top + ih * (1.0 - float(v) / max_y)

    out = [
        f'<svg class="chart" viewBox="0 0 {width} {height}" role="img">',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + ih}" class="axis-line"/>',
        f'<line x1="{left}" y1="{top + ih}" x2="{left + iw}" y2="{top + ih}" class="axis-line"/>',
        f'<text x="{left - 8}" y="{top + 4}" text-anchor="end" class="axis-text">{max_y:.1f}</text>',
        f'<text x="{left - 8}" y="{top + ih + 4}" text-anchor="end" class="axis-text">0</text>',
    ]
    for i, label in enumerate(labels):
        out.append(f'<text x="{xpos(i):.1f}" y="{height - 18}" text-anchor="middle" class="axis-text">{html.escape(label)}</text>')
    for s, item in enumerate(series):
        color = (colors or {}).get(item["name"]) if colors else None
        color = color or PALETTE[s % len(PALETTE)]
        points = " ".join(f"{xpos(i):.1f},{ypos(v):.1f}" for i, v in enumerate(item["values"]))
        out.append(f'<polyline points="{points}" fill="none" stroke="{html.escape(color)}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
        for i, v in enumerate(item["values"]):
            out.append(f'<circle cx="{xpos(i):.1f}" cy="{ypos(v):.1f}" r="3.2" fill="{html.escape(color)}"/>')
    out.append("</svg>")
    return "".join(out)


def legend(series, colors=None):
    out = ['<div class="legend">']
    for i, item in enumerate(series):
        color = (colors or {}).get(item["name"]) if colors else None
        color = color or PALETTE[i % len(PALETTE)]
        out.append(f'<span><i style="background:{html.escape(color)}"></i>{html.escape(item["label"])}</span>')
    out.append("</div>")
    return "".join(out)


def build_time_page(model, chunk_size=80):
    chunks = build_chunks(model, chunk_size)
    labels = [c["label"] for c in chunks]
    family_names = [row["family_name"] for row in model["families"]]
    family_meta = {row["family_name"]: row for row in model["families"]}
    family_values = percent_series(chunks, "families", family_names)
    family_series = [{"name": name, "label": family_meta[name].get("label") or name, "values": family_values[name]} for name in family_names]
    family_colors = {row["family_name"]: row.get("color_hex") or "#555" for row in model["families"]}
    axis_names = top_names(chunks, "axes", 6)
    axis_meta = {row["axis_name"]: row for row in model["axes"]}
    axis_values = percent_series(chunks, "axes", axis_names)
    axis_series = [{"name": name, "label": axis_meta.get(name, {}).get("label") or name, "values": axis_values[name]} for name in axis_names]
    available = Counter(event["tag_key"] for event in model["events"])
    pair = next((p for p in [("bezsilnosc", "frustracja"), ("czulosc", "strach"), ("gniew", "czulosc")] if available[p[0]] and available[p[1]]), None)
    pair_chart = pair_legend = None
    if pair:
        values = count_series(chunks, "tags", list(pair))
        pair_series = [{"name": t, "label": t.replace("-", " "), "values": values[t]} for t in pair]
        pair_chart = svg_chart(labels, pair_series)
        pair_legend = legend(pair_series)
    return {
        "chunk_size": chunk_size,
        "max_order": model["max_order"],
        "family_chart": svg_chart(labels, family_series, family_colors),
        "family_legend": legend(family_series, family_colors),
        "axis_chart": svg_chart(labels, axis_series),
        "axis_legend": legend(axis_series),
        "pair_chart": pair_chart,
        "pair_legend": pair_legend,
    }


def build_direction_page(model):
    config = json.loads(VALUES_PATH.read_text(encoding="utf-8"))
    tag_counts = Counter(event["tag_key"] for event in model["events"])
    valence_counts = Counter()
    mapped = 0
    for tag, spec in config.get("tags", {}).items():
        count = tag_counts[key(tag)]
        if count and spec.get("valence") is not None:
            valence_counts[int(spec["valence"])] += count
            mapped += count
    denom = sum(valence_counts.values()) or 1
    contrasts = []
    for spec in config.get("contrasts", []):
        left = sum(tag_counts[key(t)] for t in spec.get("left", []))
        right = sum(tag_counts[key(t)] for t in spec.get("right", []))
        total = left + right
        contrasts.append({
            "label": spec.get("label", "kontrast"),
            "description": spec.get("description", ""),
            "left_label": spec.get("left_label", "lewo"),
            "right_label": spec.get("right_label", "prawo"),
            "left": left,
            "right": right,
            "score": ((right - left) / total) if total else None,
            "left_width": 100.0 * left / total if total else 50.0,
            "right_width": 100.0 * right / total if total else 50.0,
        })
    return {
        "note": config.get("note", ""),
        "valence": {
            "negative": valence_counts[-1],
            "neutral": valence_counts[0],
            "positive": valence_counts[1],
            "negative_pct": 100.0 * valence_counts[-1] / denom,
            "neutral_pct": 100.0 * valence_counts[0] / denom,
            "positive_pct": 100.0 * valence_counts[1] / denom,
            "mapped_occurrences": mapped,
        },
        "contrasts": contrasts,
    }


def pearson(xs, ys):
    if len(xs) != len(ys) or len(xs) < 2:
        return None
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    dx, dy = [x - mx for x in xs], [y - my for y in ys]
    denom = math.sqrt(sum(x * x for x in dx) * sum(y * y for y in dy))
    return None if denom == 0 else sum(x * y for x, y in zip(dx, dy)) / denom


def cooccurrence(model, a, b):
    sets = list(model["tags_by_song"].values())
    n = len(sets)
    ca = sum(a in s for s in sets)
    cb = sum(b in s for s in sets)
    both = sum(a in s and b in s for s in sets)
    expected = ca * cb / n if n else 0.0
    return {"both": both, "expected": expected, "ratio": both / expected if expected else None}


def build_relations_page(model, chunk_size=80):
    chunks = build_chunks(model, chunk_size)
    labels = [c["label"] for c in chunks]
    available = Counter(event["tag_key"] for event in model["events"])
    pairs = []
    for a, b in [("czulosc", "strach"), ("bezsilnosc", "frustracja"), ("gniew", "frustracja"), ("milosc", "czulosc")]:
        if not available[a] or not available[b]:
            continue
        values = count_series(chunks, "tags", [a, b])
        series = [{"name": a, "label": a, "values": values[a]}, {"name": b, "label": b, "values": values[b]}]
        pairs.append({
            "a": a,
            "b": b,
            "r": pearson(values[a], values[b]),
            "co": cooccurrence(model, a, b),
            "chart": svg_chart(labels, series),
            "legend": legend(series),
        })
    return {"chunk_size": chunk_size, "pairs": pairs[:3]}
