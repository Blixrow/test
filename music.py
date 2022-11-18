import subprocess
import time

subprocess.run("pactl -- set-sink-volume 0 18%", shell=True, check=True)
subprocess.run("sudo apt-get install sox libsox-fmt-mp3 -y", shell=True, check=True)
subprocess.run("( play -q FIsxS52QXY7_Rick-Astley---Never-Gonna-Give-You-Up.mp3 )&", shell=True, check=True)

i = 0
while True:
    time.sleep(3)
    i += 3
    subprocess.run("pactl -- set-sink-volume 0 18%", shell=True, check=True)
    if (i > 180):
    	i = 0
    	subprocess.run("killall play", shell=True, check=True)
    	subprocess.run("( play -q FIsxS52QXY7_Rick-Astley---Never-Gonna-Give-You-Up.mp3 )&", shell=True, check=True)
