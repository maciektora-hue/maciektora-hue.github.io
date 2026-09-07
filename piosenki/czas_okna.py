import html
from collections import Counter, defaultdict

from statystyki import count_series, legend, percent_series, svg_chart, top_names


DEFAULT_WINDOW_SIZE = 80
DEFAULT_STEP = 30

FAMILY_PALETTE = [
    "#1565C0",
    "#00897B",
    "#EF6C00",
    "#7B1FA2",
    "#C62828",
    "#00ACC1",
    "#7CB342",
    "#D81B60",
]
AXIS_PALETTE = [
    "#0066FF",
    "#FF6D00",
    "#00BFA5",
    "#AA00FF",
    "#FF1744",
    "#00B0FF",
    "#64DD17",
    "#FFD600",
]
TAG_PALETTE = [
    "#0057FF",
    "#FF3D00",
    "#00C853",
    "#D500F9",
    "#FFAB00",
    "#00B8D4",
    "#FF1744",
    "#6200EA",
]


def _series_colors(series, palette):
    return {
        item["name"]: palette[i % len(palette)]
        for i, item in enumerate(series)
    }


def build_windows(model, size=DEFAULT_WINDOW_SIZE, step=DEFAULT_STEP, direction="teraz"):
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

    # spotify_order=1 to najnowsze polubienia. Domyślnie pokazujemy więc
    # przeszłość po lewej i teraz po prawej.
    if direction == "teraz":
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


def build_time_page_sliding(model, window_size=DEFAULT_WINDOW_SIZE, step=DEFAULT_STEP, direction="teraz"):
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
    family_colors = _series_colors(family_series, FAMILY_PALETTE)

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
    axis_colors = _series_colors(axis_series, AXIS_PALETTE)

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
        pair_colors = _series_colors(pair_series, TAG_PALETTE)
        pair_chart = svg_chart(labels, pair_series, pair_colors)
        pair_legend = legend(pair_series, pair_colors)

    return {
        "window_size": window_size,
        "step": step,
        "direction": direction,
        "direction_label": (
            "od przeszłości do teraz"
            if direction == "teraz"
            else "od teraz w przeszłość"
        ),
        "max_order": model["max_order"],
        "window_count": len(windows),
        "family_chart": svg_chart(labels, family_series, family_colors),
        "family_legend": family_legend_with_axes(model, family_series, family_colors),
        "axis_chart": svg_chart(labels, axis_series, axis_colors),
        "axis_legend": legend(axis_series, axis_colors),
        "pair_chart": pair_chart,
        "pair_legend": pair_legend,
    }
