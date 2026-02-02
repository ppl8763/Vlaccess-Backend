import subprocess
import json

def get_video_duration(video_path: str) -> int:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "json",
        video_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError("Failed to read video duration")

    duration = float(json.loads(result.stdout)["format"]["duration"])
    return int(duration)
