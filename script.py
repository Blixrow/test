import subprocess

subprocess.run(["cd ../home/tls-sec/Desktop/"])

for x in range(300):
    with open("file"+str(x), 'w') as f:
      f.write("trolled")
