from collections import Counter

from czas_okna import DEFAULT_STEP, DEFAULT_WINDOW_SIZE, TAG_PALETTE, build_windows
from statystyki import cooccurrence, count_series, legend, pearson, svg_chart


def _series_colors(series):
    return {
        item["name"]: TAG_PALETTE[i % len(TAG_PALETTE)]
        for i, item in enumerate(series)
    }


def build_relations_page(model, window_size=DEFAULT_WINDOW_SIZE, step=DEFAULT_STEP):
    windows = build_windows(
        model,
        size=window_size,
        step=step,
        direction="teraz",
    )
    labels = [window["label"] for window in windows]
    available = Counter(event["tag_key"] for event in model["events"])

    trio_tags = ["frustracja", "bezsilnosc", "gniew"]
    trio = None
    if all(available[tag] for tag in trio_tags):
        trio_values = count_series(windows, "tags", trio_tags)
        trio_series = [
            {"name": tag, "label": tag, "values": trio_values[tag]}
            for tag in trio_tags
        ]
        trio_colors = _series_colors(trio_series)
        trio = {
            "chart": svg_chart(labels, trio_series, trio_colors),
            "legend": legend(trio_series, trio_colors),
        }

    pairs = []
    for a, b in [
        ("czulosc", "strach"),
        ("bezsilnosc", "frustracja"),
        ("gniew", "frustracja"),
        ("milosc", "czulosc"),
    ]:
        if not available[a] or not available[b]:
            continue

        values = count_series(windows, "tags", [a, b])
        series = [
            {"name": a, "label": a, "values": values[a]},
            {"name": b, "label": b, "values": values[b]},
        ]
        colors = _series_colors(series)
        pairs.append({
            "a": a,
            "b": b,
            "r": pearson(values[a], values[b]),
            "co": cooccurrence(model, a, b),
            "chart": svg_chart(labels, series, colors),
            "legend": legend(series, colors),
        })

    return {
        "window_size": window_size,
        "step": step,
        "trio": trio,
        "pairs": pairs[:3],
    }
