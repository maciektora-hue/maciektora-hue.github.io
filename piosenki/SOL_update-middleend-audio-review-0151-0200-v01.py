#!/usr/bin/env python3
import os
import libsql

ROWS = [
    ("utwu-000773", "audio-0157", "mQs9TScZulk", "review", "metadata_difference", "YT credits Męskie Granie Orkiestra 2014; Spotify credits Smolik, Brodka, Dawid Podsiadło. Same song: Elektryczny."),
    ("utwu-000776", "audio-0160", "b16vSZMJ13k", "review", "featured_artist_difference", "Spotify explicitly includes Pezet; YT title/artist metadata omits featured artist. Same song: Otwieram wino."),
    ("utwu-000782", "audio-0165", "n7BkXebANI0", "review", "different_performance", "YT title indicates Royal Albert Hall performance; Spotify title is generic. Same song: Zegarmistrz swiatla."),
    ("utwu-000785", "audio-0168", "V6HaijesNEE", "review", "live_vs_studio", "YT is Live at Koningin Elisabethzaal 2012; Spotify title is generic. Same song: Vinegar & Salt."),
    ("utwu-000792", "audio-0176", "Gy1aSTZo0wA", "review", "live_vs_studio", "YT is marked VIDEO - LIVE; Spotify title is generic. Same song: Z imbirem."),
    ("utwu-000795", "audio-0179", "4ylyZ_2FaHs", "review", "featured_artist_difference", "YT credits Daniel Bloom feat. Gaba Kulka; Spotify credits Daniel Bloom, Gaba Kulka and feat. Gaba Kulka in title. Same song."),
    ("utwu-000796", "audio-0180", "2P78nxoE_JY", "review", "live_vs_studio", "Spotify is explicitly Live at Koningin Elisabethzaal 2012; YT title is generic Anger Never Dies."),
    ("utwu-000801", "audio-0185", "ZJSQxbedplM", "review", "live_vs_studio", "YT is Live at Koningin Elisabethzaal 2012; Spotify title is generic. Same song: 2 Wicky."),
    ("utwu-000814", "audio-0197", "2nI9GJbZcnM", "review", "live_vs_studio", "YT is Live at Burg Herzberg festival; Spotify title is generic. Same song: Show Your Love."),
    ("utwu-000816", "audio-0199", "2Qs1J612nZs", "review", "metadata_difference", "Spotify artist is kebe and title is 'Dave Brubeck - Golden Brown'; YT metadata identifies Dave Brubeck / Golden Brown. Treated as the same source track with metadata mismatch."),
    ("utwu-000817", "audio-0200", "If-W2suzy_k", "review", "different_performance", "Same Mahler Symphony No. 5 first movement, but YT is Kyril Kondrashin / Moscow RTV orchestra while Spotify is Bernard Haitink / Berliner Philharmoniker."),
]


def main():
    url = os.environ["TURSO_DATABASE_URL"]
    token = os.environ["TURSO_AUTH_TOKEN"]
    conn = libsql.connect(database=url, auth_token=token)
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        conn.execute("BEGIN TRANSACTION")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audio_match_details (
                utwu_id TEXT PRIMARY KEY REFERENCES middle_end(utwu_id),
                audio_id TEXT NOT NULL REFERENCES audio(audio_id),
                variant_type TEXT NOT NULL,
                note TEXT
            )
        """)

        for utwu_id, audio_id, yt_id, quality, variant_type, note in ROWS:
            conn.execute(
                "UPDATE middle_end SET audio_id=?, youtube_video_id=?, audio_match_quality=? WHERE utwu_id=?",
                (audio_id, yt_id, quality, utwu_id),
            )
            conn.execute(
                "INSERT INTO audio_match_details (utwu_id, audio_id, variant_type, note) VALUES (?, ?, ?, ?)",
                (utwu_id, audio_id, variant_type, note),
            )
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    ids = [r[0] for r in ROWS]
    placeholders = ",".join("?" for _ in ids)
    got = conn.execute(
        f"SELECT utwu_id, audio_id, youtube_video_id, audio_match_quality FROM middle_end WHERE utwu_id IN ({placeholders})",
        ids,
    ).fetchall()
    detail_count = conn.execute(
        f"SELECT COUNT(*) FROM audio_match_details WHERE utwu_id IN ({placeholders})",
        ids,
    ).fetchone()[0]

    expected = {(u, a, y, q) for u, a, y, q, _, _ in ROWS}
    actual = set(got)
    if actual != expected or detail_count != len(ROWS):
        raise RuntimeError(f"Verification failed: middle_end={len(actual)}/{len(expected)}, details={detail_count}/{len(ROWS)}")

    print(f"MIDDLE_END_AUDIO_REVIEW_UPDATE_OK={len(actual)}", flush=True)
    print(f"AUDIO_MATCH_DETAILS_OK={detail_count}", flush=True)
    conn.close()


if __name__ == "__main__":
    main()
