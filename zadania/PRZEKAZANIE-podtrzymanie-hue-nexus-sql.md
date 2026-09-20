# PRZEKAZANIE — podtrzymanie bazy `hue-nexus-sql`

Wersja: 01.00 · Data: 2026-09-20
Dla: repozytorium `hue-nexus/happy-hue-ledger`
Status: **DO WYKONANIA W OSOBNEJ SESJI** — ta jest przypięta do właściciela
`maciektora-hue` i repozytoriów innego właściciela nie dodaje

---

## 1. Co się stało

2026-09-20 przyszedł mail od Supabase: projekt **`hue-nexus-sql`**
(ID `ejqturfbtghybugmizcl`, organizacja `maciekHUE`) jest **zaplanowany do
zapauzowania** z powodu braku aktywności przez ponad 7 dni.

Projekt nie był jeszcze zapauzowany. **Zegar zresetowano ręcznym zapytaniem
o 19:45 UTC** — to kupuje siedem dni, nie więcej.

Dane sprawdzone przy okazji, wszystkie na miejscu: `catalog_files` 2762,
`storage_objects` 2762, `tibetan_syllables` 1140.

**Co się dzieje po pauzie:** odpauzowanie jest ręczne z panelu i możliwe przez
90 dni. Po tym terminie zostaje już tylko pobranie danych.

---

## 2. Dlaczego to dotknęło akurat ten projekt

Repozytorium `maciektora-hue.github.io` ma cron `podtrzymanie-api.yml`, który
codziennie puka w `/health` usługi `piosenki-api`. Ten endpoint otwiera
połączenie i wykonuje `SELECT 1`, więc chroni projekt `maciekGithubHue`.

`hue-nexus-sql` obsługuje usługę `temat-hue` z repozytorium
`hue-nexus/happy-hue-ledger` i **żadnego takiego crona nie ma.**

---

## 3. Dwa osobne zegary — nie mylić

| | Render (plan `free`) | Supabase (plan `free`) |
|---|---|---|
| kiedy zasypia | ~15 minut bezczynności | **7 dni bez ruchu w bazie** |
| skutek | zimny start, kilkanaście sekund | **projekt zapauzowany** |
| czy cron pomaga | **nie** — zaśnie kwadrans po pingu | **tak** |
| co pomaga | wyłącznie płatny plan | codzienny ping |

**Najważniejsze zdanie tego dokumentu:** dla Supabase liczy się wyłącznie to, czy
żądanie **dotyka bazy**. Sam ping Rendera nie jest aktywnością Supabase. Endpoint
zwracający `{"ok": true}` z pamięci obudzi usługę i nie zrobi dla bazy nic.

---

## 4. Do zrobienia — trzy kroki

### Krok 1. Sprawdzić, czy jest endpoint sięgający do bazy

Jeśli nie ma — dodać, wzorem `piosenki/app.py`:

```python
# NIE USUWAĆ STĄD ZAPYTANIA DO BAZY.
#
# To nie jest zwykły health check. SELECT 1 poniżej jest jedyną rzeczą, która
# trzyma projekt Supabase przy życiu: darmowy plan pauzuje projekt po 7 dniach
# bez ruchu w bazie, a odpauzowanie jest ręczne i ma 90-dniowy termin.
#
# Gdyby ktoś "zoptymalizował" ten endpoint tak, żeby zwracał status bez otwierania
# połączenia — co brzmi jak rozsądna zmiana — cron nadal świeciłby na zielono,
# a projekt zapauzowałby się po tygodniu. Awaria byłaby cicha.
@app.get("/health")
def health():
    try:
        conn = get_connection()
        value = conn.execute("SELECT 1").fetchone()[0]
        conn.close()
        return jsonify(status="ok", database=value), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
```

### Krok 2. Dodać cron

Plik `.github/workflows/podtrzymanie-bazy.yml`:

```yaml
name: Podtrzymanie API i bazy

# Darmowy Supabase pauzuje projekt po 7 dniach bez ruchu W BAZIE.
# Odpauzowanie jest ręczne i wygasa po 90 dniach — potem zostaje już tylko
# pobranie danych. Ten cron temu zapobiega.
#
# UWAGA 1: to NIE usuwa zimnego startu. Render na planie free zaśnie
# 15 minut po pingu. Na to pomaga wyłącznie płatny plan.
#
# UWAGA 2: liczy się wyłącznie to, że trafiony endpoint OTWIERA POŁĄCZENIE
# z bazą. Sam ping Rendera nie jest aktywnością Supabase. Jeśli ktoś usunie
# zapytanie z health checka, ten cron nadal będzie zielony, a projekt
# zapauzuje się po tygodniu. Awaria cicha.
#
# UWAGA 3: GitHub wyłącza zaplanowane workflowy w repozytoriach bez
# aktywności przez 60 dni. Wtedy trzeba go włączyć ręcznie w Actions.

on:
  schedule:
    - cron: '23 5 * * *'   # nierówna minuta celowo, o pełnych godzinach jest zator
  workflow_dispatch:

permissions:
  contents: read

jobs:
  ping:
    name: Obudź temat-hue i dotknij Supabase
    runs-on: ubuntu-latest
    steps:
      - name: Puknij w endpoint sięgający do bazy
        run: |
          set -uo pipefail
          URL="https://temat-hue.onrender.com/health"   # endpoint MUSI pytać bazę

          for proba in 1 2 3; do
            echo "── Próba $proba z 3"
            start=$(date +%s)
            odp=$(curl -sS --max-time 180 -w $'\n%{http_code}' "$URL" || true)
            czas=$(( $(date +%s) - start ))
            kod=$(printf '%s' "$odp" | tail -n1)
            echo "   HTTP $kod po ${czas}s"
            printf '%s' "$odp" | sed '$d'
            [ "$kod" = "200" ] && { echo "API i baza odpowiadają."; exit 0; }
            [ "$proba" -lt 3 ] && sleep 30
          done

          echo "::error::temat-hue nie odpowiedziało po 3 próbach."
          exit 1
```

### Krok 3. Sprawdzić ręcznie

Zakładka **Actions**, workflow uruchamiany przyciskiem (`workflow_dispatch`).
Oczekiwany wynik: `HTTP 200` i treść potwierdzająca odczyt z bazy.

---

## 5. Wariant rezerwowy — ping prosto do bazy

Gdyby aplikacja nie miała endpointu dotykającego bazy albo gdyby miała nie
odpowiadać, można pominąć Rendera i pukać wprost do Postgresa:

```yaml
      - name: SELECT 1 prosto do bazy
        env:
          DB_URL: ${{ secrets.SUPABASE_DATABASE_URL }}
        run: psql "$DB_URL" -c 'SELECT 1'
```

Wymaga wstawienia connection stringa do sekretów **tego** repozytorium.
Działa niezależnie od stanu aplikacji.

**Tego wariantu celowo nie wstawiono w `maciektora-hue.github.io`** — oznaczałby
trzymanie poświadczeń innej organizacji w cudzym repozytorium.

---

## 6. Gdyby pauza groziła wcześniej

Ręczne zapytanie z panelu Supabase, cokolwiek w rodzaju `SELECT 1`, zeruje
licznik na kolejne siedem dni. To proteza, nie rozwiązanie.

---

## 7. Wzorce do skopiowania

W repozytorium `maciektora-hue/maciektora-hue.github.io`:

- `.github/workflows/podtrzymanie-api.yml` — działający cron z ponawianiem
- `piosenki/app.py`, endpoint `/health` — zapytanie i ostrzeżenie nad nim
- `SOT-SOA-AKTUALNA.md` — opis obu zegarów i kruchej zależności
- `zadania/SOL_LISTA-ZADAN.md` — to samo zadanie w skrócie

---

Stworzono z pomocą Claude (Anthropic), wariant: Claude Opus 5.
