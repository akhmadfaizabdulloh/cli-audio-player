import shutil
import sys

def check_dependencies():
    required = ["yt-dlp", "mpv"]
    missing = []

    for cmd in required:
        if shutil.which(cmd) is None:
            missing.append(cmd)

    if missing:
        print("❌ Missing dependencies:")
        for m in missing:
            print(f" - {m}")
        sys.exit(1)
        