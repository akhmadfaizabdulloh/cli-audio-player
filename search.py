import subprocess

def search(query, limit=3):
    command = [
        "yt-dlp",
        "--flat-playlist",
        f"ytsearch{limit}:{query}",
        "--print",
        "%(title)s|%(id)s"
    ]

    process = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if process.returncode != 0:
            print("❌ yt-dlp error")
            print(process.stderr.strip())
            return []
    
    results = []

    for line in process.stdout.strip().split("\n"):
        if "|" not in line:
            continue

        title, video_id = line.split("|", 1)

        results.append({
            "title": title,
            "url": f"https://youtube.com/watch?v={video_id}"
        })
    
    return results