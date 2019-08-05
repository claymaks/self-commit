import os
import time
import hashlib
import datetime


def commit():
    os.system("git add .")
    print("Added")
    time.sleep(1)
    hash_object = hashlib.md5(str(datetime.datetime.now()).encode())
    msg = "git commit -m \"" + hash_object.hexdigest() + "\""
    os.system(msg)
    print("Committed")
    time.sleep(1)
    os.system("git push")
    print("Pushed")
