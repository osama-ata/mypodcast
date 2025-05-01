
import frontmatter
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os

CONTENT_DIR = "content/episodes"
AUDIO_DIR = "static/audio"


def inject_metadata(md_path, mp3_path):
    post = frontmatter.load(md_path)
    meta = post.metadata

    try:
        audio = MP3(mp3_path, ID3=EasyID3)
    except Exception as e:
        print(f"Error loading MP3: {mp3_path} - {e}")
        return

    audio["title"] = meta.get("title", "Unknown Title")
    audio["artist"] = meta.get("author", "Unknown Artist")
    audio["album"] = f"Season {meta.get('season', '1')}"
    audio["tracknumber"] = str(meta.get("episode", "1"))
    audio["date"] = str(meta.get("date", "")).split("T")[0]
    audio["genre"] = "Podcast"
    audio.save()
    print(f"Metadata injected: {mp3_path}")


def main():
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md"):
            md_path = os.path.join(CONTENT_DIR, filename)
            basename = os.path.splitext(filename)[0]
            mp3_filename = f"{basename}.mp3"
            mp3_path = os.path.join(AUDIO_DIR, mp3_filename)
            if os.path.exists(mp3_path):
                inject_metadata(md_path, mp3_path)
            else:
                print(f"MP3 not found: {mp3_path}")


if __name__ == "__main__":
    main()
