
"""A simple music catalog with playlist and popularity features."""

import json
import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE songs ("
    "id INTEGER PRIMARY KEY, "
    "title TEXT, "
    "artist TEXT, "
    "plays INTEGER)"
)


def add_song(
    title: str,
    artist: str,
    plays: int = 0,
    playlist: list[str] | None = None,
) -> list[str]:
    """Add a song to the catalog and playlist."""
    if playlist is None:
        playlist = []

    conn.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick() -> int | None:
    """Return a randomly selected song ID, or None if empty."""
    ids = [row[0] for row in conn.execute("SELECT id FROM songs")]

    if not ids:
        return None

    return secrets.choice(ids)


def popularity(title: str) -> str:
    """Classify a song according to its play count."""
    row = conn.execute(
        "SELECT plays FROM songs WHERE title = ?",
        (title,),
    ).fetchone()

    if row is None:
        return "unknown"

    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist: list[str]) -> str:
    """Serialize a playlist as a JSON string."""
    return json.dumps(playlist)


def load_playlist(blob: str) -> list[str]:
    """Deserialize a playlist from a JSON string."""
    return json.loads(blob)


def total_plays() -> int:
    """Return the total number of plays across all songs."""
    try:
        result = conn.execute(
            "SELECT SUM(plays) FROM songs"
        ).fetchone()
        return result[0] or 0
    except sqlite3.Error:
        return 0


def main() -> None:
    """Demonstrate the music catalog functionality."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)

    blob = save_playlist(playlist)
    playlist_loaded = load_playlist(blob)

    if len(playlist_loaded) > 1:
        print("multi-song playlist")

    print(
        popularity("Aurora"),
        popularity("Monsoon"),
        shuffle_pick(),
        total_plays(),
    )


if __name__ == "__main__":
    main()
