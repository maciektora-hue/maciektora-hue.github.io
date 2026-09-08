from collections import Counter

from czas_okna import DEFAULT_STEP, DEFAULT_WINDOW_SIZE, TAG_PALETTE, build_windows
from statystyki import count_series, legend, svg_chart


HYPOTHESES = [
    {
        "title": "lęk · hiperczujność · zamartwianie",
        "tags": ["lek", "hiperczujnosc", "zamartwianie"],
    },
    {
        "title": "bezsilność · frustracja · gniew",
        "tags": ["bezsilnosc", "frustracja", "gniew"],
    },
    {
        "title": "smutek · rozpacz · brak nadziei",
        "tags": ["smutek", "rozpacz", "brak-nadziei"],
    },
    {
        "title": "wyczerpanie · brak napędu · anhedonia",
        "tags": ["wyczerpanie", "brak-napedu", "anhedonia"],
    },
    {
        "title": "maskowanie-koszt · rozpad po masce · wyczerpanie",
        "tags": ["maskowanie-koszt", "rozpad-po-masce", "wyczerpanie"],
    },
    {
        "title": "ulga · spokój · bezsilność",
        "tags": ["ulga", "spokoj", "bezsilnosc"],
    },
    {
        "title": "samotność · samotność preferowana · niedopasowanie społeczne",
        "tags": ["samotnosc", "samotnosc-preferowana", "niedopasowanie-spoleczne"],
    },
    {
        "title": "alexithymia · nie wiem co czuję · emocja z opóźnieniem",
        "tags": ["alexithymia", "nie-wiem-co-czuje", "emocja-z-opoznieniem"],
    },
    {
        "title": "kontrola · hiperczujność · niepewność nie do zniesienia",
        "tags": ["kontrola", "hiperczujnosc", "niepewnosc-nie-do-zniesienia"],
    },
    {
        "title": "pogoń · cel nieosiągnięty · nigdy dość",
        "tags": ["pogon", "cel-nieosiagniety", "nigdy-dosc"],
    },
    {
        "title": "czułość · strach · zazdrość",
        "tags": ["czulosc", "strach", "zazdrosc"],
    },
    {
        "title": "gniew · wstyd · frustracja",
        "tags": ["gniew", "wstyd", "frustracja"],
    },
]


def _colors(series):
    return {
        item["name"]: TAG_PALETTE[i % len(TAG_PALETTE)]
        for i, item in enumerate(series)
    }


def build_hypotheses_page(model, window_size=DEFAULT_WINDOW_SIZE, step=DEFAULT_STEP):
    windows = build_windows(
        model,
        size=window_size,
        step=step,
        direction="teraz",
    )
    labels = [window["label"] for window in windows]
    available = Counter(event["tag_key"] for event in model["events"])

    hypotheses = []
    for spec in HYPOTHESES:
        tags = spec["tags"]
        values = count_series(windows, "tags", tags)
        series = [
            {
                "name": tag,
                "label": tag.replace("-", " "),
                "values": values[tag],
            }
            for tag in tags
        ]
        colors = _colors(series)
        hypotheses.append(
            {
                "title": spec["title"],
                "chart": svg_chart(labels, series, colors),
                "legend": legend(series, colors),
                "counts": [
                    {
                        "label": tag.replace("-", " "),
                        "count": available[tag],
                    }
                    for tag in tags
                ],
                "missing": [
                    tag.replace("-", " ")
                    for tag in tags
                    if not available[tag]
                ],
            }
        )

    return {
        "window_size": window_size,
        "step": step,
        "hypotheses": hypotheses,
    }
