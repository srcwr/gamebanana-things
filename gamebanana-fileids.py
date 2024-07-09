# SPDX-License-Identifier: WTFPL

from pathlib import Path
import time
import requests
import prettyjson
import os.path
import sys

already_scraped = {}
with open("already_scraped.txt") as f:
    for line in f:
        already_scraped[int(line.strip())] = True

"""
for i in range(438888):
    xd = f"gamebanana-fileids/_{i:07}.json"
    if os.path.getsize(xd) <= 81:
        with open(xd, "w") as f:
            print("goodbye "+xd)
            pass
"""

session = requests.Session()

#for i in range(1, 785):
#for i in range(1, 100000):
#for i in range(100000, 200000):
#for i in range(200000, 300000):
#for i in range(300000, 438888):

limit = 1001444
base  =  440000
remaining = limit - base
workers = int(sys.argv[1])
tranch = int(remaining / workers)
meidx = int(sys.argv[2])

for i in range(limit):
#for i in range(base+(tranch*meidx), base+(tranch*(meidx+1))):
#for i in range(int(sys.argv[1]), int(sys.argv[2])):
#for i in reversed(range(438725)): #range(1, 130000):  #438725
    xd = f"gamebanana-fileids/_{i:07}.json"
    if os.path.isfile(xd):
        continue
    #if False and already_scraped[i]:
    #    continue
    #resp = requests.get("https://gamebanana.com/apiv11/File/" + str(i))
    resp = session.get("https://gamebanana.com/apiv11/File/" + str(i))
    with open(xd, "w", encoding="utf-8") as f:
        f.write(prettyjson.prettystr(resp.content))
        print(f"write to _{i:07}.json")
    #prettyjson.prettyfile(xd)
    #time.sleep(0.01)
