import os
import os.path
from os import path
import hashlib
import sys
from datetime import datetime

file_sys = {}

blacklist = [
    "/dev",
    "/proc",
    "/run",
    "/sys",
    "/tmp",
    "/var/lib",
    "/var/run"
    "/mnt"
]


outfile = sys.argv[1]

for dirpath, dirs, files in os.walk("./test"):
    for filename in files:
        skip = 0
        for item in blacklist:
            if item in dirpath:
                skip = 1
        if skip == 1:
            continue
        fname = os.path.join(dirpath,filename)
        with open(fname,"rb") as f:
            hash = hashlib.sha256()
            for byte_block in iter(lambda: f.read(4096),b""): #learned about anonymous functions in my game theory class
                hash.update(byte_block)
            file_sys[fname] = [hash.hexdigest(), datetime.now().strftime("%d/%m/%Y %H:%M:%S")]

if path.exists(outfile):
    file_sys_old = eval(open(outfile).read())
    for key in file_sys:
        if file_sys_old[key]:
            if file_sys[key][0] == file_sys_old[key][0]:
                pass
            else:
                print(key,"has been changed.")
        else:
            print(key,"has been added.")
    for key in file_sys_old:
        if key not in file_sys:
            print(key,"has been removed.")
     

with open(outfile,"w") as f:
    f.write(str(file_sys))

