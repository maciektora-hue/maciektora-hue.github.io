import csv
import io
import os

import libsql
from flask import Flask, Response, jsonify, render_template, request
from flask_cors import CORS

from analizy13 import build_13_analyses
from content_store import (
    ensure_content_storage,
    fetch_content_rows,
)
from content_structure import (
    ensure_content_structure_v2,
    fetch_content_collections_v2,
    fetch_content_status_v2,
    fetch_content_structure,
)
from czas_okna import DEFAULT_STEP, DEFAULT_WINDOW_SIZE, build_time_page_sliding
from hipotezy_okna import build_hypotheses_page
from relacje_okna import build_relations_page
from statystyki import build_direction_page, load_model


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://maciektora-hue.github.io"]}})

TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL", "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io")
TURSO_ADMIN_TOKEN = os.environ.get("TURSO_ADMIN_TOKEN")


def get_connection():
    if not TURSO_ADMIN_TOKEN:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")
    conn = libsql.connect(database=TURSO_DATABASE_URL, auth_token=TURSO_ADMIN_TOKEN)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def fetch_rows(conn, sql, columns):
    rows = conn.execute(sql).fetchall()
    return [dict(zip(columns, row)) for row in rows]


def load_stats_model():
    conn = get_connection()
    try:
        return load_model(conn)
    finally:
        conn.close()


def query_int(name, default):
    try:
        value = int(request.args.get(name, default))
    except (TypeError, ValueError):
        value = default
    return max(1, min(value, 5000))


def initialize_content_storage():
    conn = get_connection()
    try:
        state = ensure_content_storage(conn)
        structure_state = ensure_content_structure_v2(conn)
        collections = fetch_content_collections_v2(conn)
        print(f"CONTENT SQL: {state}", flush=True)
        print(f"CONTENT STRUCTURE: {structure_state}", flush=True)
        print(f"CONTENT SQL STATUS: {collections}", flush=True)
        return {"content": state, "structure": structure_state}
    finally:
        conn.close()


def content_tsv(conn, collection_id):
    if collection_id == "rosja":
        view = "v_rosja_mapa_sekcji"
        filename = "SOL_mapa-sekcji-z-opisami-SQL.tsv"
        columns = [
            "dokument_kod", "dokument_plik", "dokument_tytul", "url_stabilny",
            "poziom", "glebokosc", "kolejnosc", "sekcja_tytul", "anchor",
            "anchor_status", "deep_link", "opis",
        ]
        expected = 620
    elif collection_id == "audhd":
        view = "v_audhd_mapa_sekcji"
        filename = "SOL_mapa-sekcji-i-anchorow-audhd-SQL.tsv"
        columns = [
            "dokument_kod", "dokument_plik", "dokument_tytul", "url_zrodlowy",
            "poziom", "glebokosc", "kolejnosc", "sekcja_tytul", "anchor",
            "anchor_status", "deep_link",
        ]
        expected = 338
    else:
        return None

    rows = conn.execute(f"SELECT {', '.join(columns)} FROM {view}").fetchall()
    if len(rows) != expected:
        raise RuntimeError(
            f"{collection_id}: eksport TSV: oczekiwano {expected} rekordów, jest {len(rows)}"
        )

    out = io.StringIO(newline="")
    writer = csv.writer(out, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(columns)
    writer.writerows(rows)
    return filename, out.getvalue()


# WAŻNE: nie otwieramy połączenia libsql podczas importu modułu Gunicorna.
# Inicjalizacja/migracje są wykonywane osobno; requesty otwierają własne połączenia.
CONTENT_STORAGE_STATE = None


@app.get("/health")
def health():
    try:
        conn = get_connection()
        value = conn.execute("SELECT 1").fetchone()[0]
        conn.close()
        return jsonify(status="ok", database=value), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500


@app.get("/api/piosenki")
def api_piosenki():
    conn = None
    try:
        conn = get_connection()
        data = {
            "middle_end": fetch_rows(conn, """
                SELECT utwu_id, lyrics_id, spotify_id, spotify_order, title_original,
                       title_normalized, title_parsed, artist_original, artist_normalized,
                       artist_parsed, album_original, match_status, match_candidates,
                       match_note, lyrics_status
                FROM middle_end
                ORDER BY spotify_order, utwu_id
                """, ["utwu_id", "lyrics_id", "spotify_id", "spotify_order", "title_original", "title_normalized", "title_parsed", "artist_original", "artist_normalized", "artist_parsed", "album_original", "match_status", "match_candidates", "match_note", "lyrics_status"]),
            "tag_snapshots": fetch_rows(conn, "SELECT lyrics_id, tagged_at, tags FROM tag_snapshots ORDER BY tagged_at, lyrics_id", ["lyrics_id", "tagged_at", "tags"]),
            "tag_catalog": fetch_rows(conn, "SELECT tag, definition FROM tag_catalog ORDER BY tag", ["tag", "definition"]),
            "families": fetch_rows(conn, "SELECT family_name, label, color_hex, description, sort_order FROM families ORDER BY sort_order", ["family_name", "label", "color_hex", "description", "sort_order"]),
            "tag_groups": fetch_rows(conn, "SELECT group_name, label FROM tag_groups ORDER BY group_name", ["group_name", "label"]),
            "axes": fetch_rows(conn, "SELECT axis_name, label, description, family_name, sort_order FROM axes ORDER BY sort_order", ["axis_name", "label", "description", "family_name", "sort_order"]),
            "tag_group": fetch_rows(conn, "SELECT tag, group_name FROM tag_group ORDER BY tag, group_name", ["tag", "group_name"]),
            "tag_axis": fetch_rows(conn, "SELECT tag, axis_name FROM tag_axis ORDER BY tag, axis_name", ["tag", "axis_name"]),
            "lyrics": fetch_rows(conn, "SELECT lyrics_id FROM lyrics ORDER BY lyrics_id", ["lyrics_id"]),
        }
        return jsonify(data), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


@app.get("/api/content")
def api_content_collections():
    conn = None
    try:
        conn = get_connection()
        return jsonify(collections=fetch_content_collections_v2(conn)), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


@app.get("/api/content/<collection_id>")
def api_content_collection(collection_id):
    conn = None
    try:
        conn = get_connection()
        status = fetch_content_status_v2(conn, collection_id)
        if status is None:
            return jsonify(status="not_found", collection_id=collection_id), 404
        rows = fetch_content_rows(conn, collection_id)
        return jsonify(collection_id=collection_id, status=status, rows=rows), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


@app.get("/api/content/<collection_id>/structure")
def api_content_collection_structure(collection_id):
    conn = None
    try:
        conn = get_connection()
        status = fetch_content_status_v2(conn, collection_id)
        if status is None:
            return jsonify(status="not_found", collection_id=collection_id), 404
        rows = fetch_content_structure(conn, collection_id)
        return jsonify(collection_id=collection_id, status=status, rows=rows), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


@app.get("/api/content/<collection_id>/status")
def api_content_collection_status(collection_id):
    conn = None
    try:
        conn = get_connection()
        status = fetch_content_status_v2(conn, collection_id)
        if status is None:
            return jsonify(status="not_found", collection_id=collection_id), 404
        return jsonify(status), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


@app.get("/api/content/<collection_id>/export.tsv")
def api_content_collection_tsv(collection_id):
    conn = None
    try:
        conn = get_connection()
        exported = content_tsv(conn, collection_id)
        if exported is None:
            return jsonify(status="not_found", collection_id=collection_id), 404
        filename, body = exported
        return Response(
            body,
            status=200,
            content_type="text/tab-separated-values; charset=utf-8",
            headers={"Content-Disposition": f'attachment; filename="{filename}"'},
        )
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


@app.get("/statystyki/")
def statystyki_index():
    return render_template("statystyki-index.html")


@app.get("/statystyki/czas")
def statystyki_czas():
    window_size = query_int("okno", DEFAULT_WINDOW_SIZE)
    step = query_int("krok", DEFAULT_STEP)
    direction = request.args.get("kierunek", "teraz")
    if direction not in {"teraz", "przeszlosc"}:
        direction = "teraz"
    data = build_time_page_sliding(
        load_stats_model(),
        window_size=window_size,
        step=step,
        direction=direction,
    )
    return render_template("czas.html", data=data)


@app.get("/statystyki/kierunek")
def statystyki_kierunek():
    return render_template("kierunek.html", data=build_direction_page(load_stats_model()))


@app.get("/statystyki/relacje")
def statystyki_relacje():
    return render_template(
        "relacje.html",
        data=build_relations_page(
            load_stats_model(),
            window_size=DEFAULT_WINDOW_SIZE,
            step=DEFAULT_STEP,
        ),
    )


@app.get("/statystyki/hipotezy")
def statystyki_hipotezy():
    return render_template(
        "hipotezy.html",
        data=build_hypotheses_page(
            load_stats_model(),
            window_size=DEFAULT_WINDOW_SIZE,
            step=DEFAULT_STEP,
        ),
    )


@app.get("/statystyki/13")
def statystyki_13():
    return render_template(
        "analizy13.html",
        data=build_13_analyses(
            load_stats_model(),
            chunk_size=DEFAULT_WINDOW_SIZE,
            step=DEFAULT_STEP,
        ),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))