import html
from collections import Counter, defaultdict

from statystyki import count_series, legend, percent_series, svg_chart, top_names


def build_windows(model, size=80, step=30, direction="teraz"):
    max_order = model["max_order"]
    if max_order <= 0:
        return []

    size = max(1, int(size))
    step = max(1, int(step))

    ranges = []
    start = 1
    while start <= max_order:
        end = min(start + size - 1, max_order)
        ranges.append((start, end))
        if end >= max_order:
            break
        start += step

    if direction == "przeszlosc":
        ranges.reverse()

    windows = []
    for start, end in ranges:
        windows.append({
            "start": start,
            "end": end,
            "label": f"{start}–{end}",
            "tag_total": 0,
            "tags": Counter(),
            "axes": Counter(),
            "families": Counter(),
        })

    for event in model["events"]:
        order = event["spotify_order"]
        for window in windows:
            if window["start"] <= order <= window["end"]:
                window["tag_total"] += 1
                window["tags"][event["tag_key"]] += 1
                for axis_name in event["axis_names"]:
                    window["axes"][axis_name] += 1
                for family_name in event["family_names"]:
                    window["families"][family_name] += 1

    return windows


def family_legend_with_axes(model, family_series, colors):
    axes_by_family = defaultdict(list)
    for row in sorted(model["axes"], key=lambda x: x.get("sort_order") or 0):
        family_name = row.get("family_name")
        if not family_name:
            continue
        axes_by_family[family_name].append(row.get("label") or row.get("axis_name") or "")

    out = ['<div class="family-legend">']
    for item in family_series:
        name = item["name"]
        label = item["label"]
        color = colors.get(name) or "#555"
        axes = [axis for axis in axes_by_family.get(name, []) if axis]
        axes_text = " · ".join(axes) if axes else "brak przypisanych osi"
        out.append(
            '<div class="family-legend-item">'
            f'<i style="background:{html.escape(color)}"></i>'
            '<div>'
            f'<strong>{html.escape(label)}</strong>'
            f'<span class="family-axes">{html.escape(axes_text)}</span>'
            '</div>'
            '</div>'
        )
    out.append("</div>")
    return "".join(out)


def build_time_page_sliding(model, window_size=80, step=30, direction="teraz"):
    windows = build_windows(model, window_size, step, direction)
    labels = [window["label"] for window in windows]

    family_names = [row["family_name"] for row in model["families"]]
    family_meta = {row["family_name"]: row for row in model["families"]}
    family_values = percent_series(windows, "families", family_names)
    family_series = [
        {
            "name": name,
            "label": family_meta[name].get("label") or name,
            "values": family_values[name],
        }
        for name in family_names
    ]
    family_colors = {
        row["family_name"]: row.get("color_hex") or "#555"
        for row in model["families"]
    }

    axis_names = top_names(windows, "axes", 6)
    axis_meta = {row["axis_name"]: row for row in model["axes"]}
    axis_values = percent_series(windows, "axes", axis_names)
    axis_series = [
        {
            "name": name,
            "label": axis_meta.get(name, {}).get("label") or name,
            "values": axis_values[name],
        }
        for name in axis_names
    ]

    available = Counter(event["tag_key"] for event in model["events"])
    pair = next(
        (
            pair
            for pair in [
                ("bezsilnosc", "frustracja"),
                ("czulosc", "strach"),
                ("gniew", "czulosc"),
            ]
            if available[pair[0]] and available[pair[1]]
        ),
        None,
    )

    pair_chart = None
    pair_legend = None
    if pair:
        values = count_series(windows, "tags", list(pair))
        pair_series = [
            {
                "name": tag,
                "label": tag.replace("-", " "),
                "values": values[tag],
            }
            for tag in pair
        ]
        pair_chart = svg_chart(labels, pair_series)
        pair_legend = legend(pair_series)

    return {
        "window_size": window_size,
        "step": step,
        "direction": direction,
        "direction_label": (
            "od przeszłości do teraz"
            if direction == "przeszlosc"
            else "od teraz w przeszłość"
        ),
        "max_order": model["max_order"],
        "window_count": len(windows),
        "family_chart": svg_chart(labels, family_series, family_colors),
        "family_legend": family_legend_with_axes(model, family_series, family_colors),
        "axis_chart": svg_chart(labels, axis_series),
        "axis_legend": legend(axis_series),
        "pair_chart": pair_chart,
        "pair_legend": pair_legend,
    }
