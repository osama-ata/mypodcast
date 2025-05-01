
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os
import json

AUDIO_DIR = "static/audio"


def collect_metadata(mp3_path):
    try:
        audio = MP3(mp3_path, ID3=EasyID3)
        return {key: audio.get(key, [""])[0] for key in audio.keys()}
    except Exception as e:
        return {"error": str(e)}


def main():
    result = {}
    for filename in os.listdir(AUDIO_DIR):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(AUDIO_DIR, filename)
            result[filename] = collect_metadata(mp3_path)

    with open("data/audio_metadata.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print("Metadata exported to audio_metadata.json")


if __name__ == "__main__":
    main()
