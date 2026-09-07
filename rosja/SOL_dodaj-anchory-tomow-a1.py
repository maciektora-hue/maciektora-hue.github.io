#!/usr/bin/env python3
from pathlib import Path

HTML = Path(__file__).resolve().parent / "a1_POCZATEK_ZAMROZONE_kolumbryna-v3_5-2026-03-31-anchory.html"
STATUS = Path(__file__).resolve().parent / "SOL_status-techniczny.txt"

TOMY = [
    ("Tom I", "Front, OPL i arsenał", "front-opl-arsenal"),
    ("Tom II", "Gospodarka, finanse i eksport", "gospodarka-finanse-eksport"),
    ("Tom III", "Infrastruktura i społeczeństwo", "infrastruktura-spoleczenstwo"),
    ("Tom IV", "Synteza i prognoza", "synteza-prognoza"),
    ("Tom V", "Projekt życia mu nie wyszedł", "projekt-zycia-mu-nie-wyszedl"),
    ("Tom VI", "Od Kaukazu po Zatokę", "od-kaukazu-po-zatoke"),
    ("Tom VII", "Od Ormuzu do panelu słonecznego", "od-ormuzu-do-panelu-slonecznego"),
    ("Tom VIII", "Disinfolklore, Dark Legitimacy i etyka", "disinfolklore-dark-legitimacy-etyka"),
    ("Tom IX", "Korekta i przesłuchanie", "korekta-przesluchanie"),
]

s = HTML.read_text(encoding="utf-8")

for i in range(1, 10):
    if s.count(f'id="tom{i}"') != 1:
        raise SystemExit(f"STOP: techniczny anchor tom{i} nie występuje dokładnie raz")

changed = 0
for _, title, ident in TOMY:
    old = f'<div class="volume-title">{title}</div>'
    new = f'<div class="volume-title" id="{ident}">{title}</div>'
    old_count = s.count(old)
    new_count = s.count(new)
    if old_count == 1 and new_count == 0:
        s = s.replace(old, new, 1)
        changed += 1
    elif old_count == 0 and new_count == 1:
        pass
    else:
        raise SystemExit(
            f"STOP: niejednoznaczny stan tomu {title!r}: stary={old_count}, nowy={new_count}"
        )

for _, _, ident in TOMY:
    if s.count(f'id="{ident}"') != 1:
        raise SystemExit(f"STOP: słowny anchor nie jest unikalny: {ident}")

HTML.write_text(s, encoding="utf-8")

st = STATUS.read_text(encoding="utf-8")
marker = "A1 — STRUKTURA TOMÓW I HIERARCHIA H"
note = """
A1 — STRUKTURA TOMÓW I HIERARCHIA H
- A1 ma 9 TOMÓW jako osobną warstwę strukturalną ponad rozdziałami.
- TOMY nie są nagłówkami H1–H6: każdy tom jest <section class="volume" id="tomN">, a jego nazwa jest w <div class="volume-title">.
- Zachowano techniczne anchory tom1–tom9 i dodano dodatkowe ręcznie nazwane anchory słowne do nazw tomów.
- Skoki w hierarchii H wykazane przez audyt są CELOWE i nie są błędem do naprawy.
""".strip()

if marker not in st:
    STATUS.write_text(st.rstrip() + "\n\n" + note + "\n", encoding="utf-8")
elif st.count(marker) != 1:
    raise SystemExit("STOP: notatka A1 w statusie występuje więcej niż raz")

print(f"OK: ręczne anchory tomów A1, dodane teraz: {changed}/9; tom1..tom9 zachowane")
