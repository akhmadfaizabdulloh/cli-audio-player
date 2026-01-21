import subprocess

def play(url):
    print("▶️  Playing... (tekan Q untuk keluar)\n")

    command = [
        "mpv",
        "--no-video",
        "--force-window=no",
        "--quiet",
        url
    ]

    subprocess.run(command)