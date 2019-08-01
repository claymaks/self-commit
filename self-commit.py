import os
import time

os.system("git add .")
time.sleep(1)
os.system("git commit -m \"Test Commit\"")
time.sleep(1)
os.system("git push")
