import subprocess

subprocess.run("pactl -- set-sink-volume 0 20%", shell=True, check=True)
subprocess.run("sudo apt-get install sox libsox-fmt-mp3 -y", shell=True, check=True)
subprocess.run("( play -q FIsxS52QXY7_Rick-Astley---Never-Gonna-Give-You-Up.mp3 )&", shell=True, check=True)
