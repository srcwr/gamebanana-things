
import json
from pathlib import Path
from sanitize_filename import sanitize
import subprocess
import sys
import os.path
import time

filesizesum = 0

links = []


"""
interesting:
cd gamebanana-items
rg --sort-files -l "(xc|kz|bh|bhop|surf|climb|trikz|jump|bunny|kreedz|xtreme|hop)" > ../interesting.txt
cd ..
"""

dddd = Path("gamebanana-items")
for filename in dddd.glob("*.json"):
    with open(filename, "r", encoding="utf-8") as f:
#with open("interesting.txt") as interestingtxt:
#    for interesting in interestingtxt:
#        with open("gamebanana-items/" + interesting.strip(), encoding="utf-8") as f:
            j = json.load(f)
            for file in j["_aFiles"]:
                filesizesum += file["_nFilesize"]
                links.append([file["_sDownloadUrl"], sanitize(str(file["_idRow"]) + "_" + file["_sFile"]), j["_sName"]])

print(f"filesizesum = {filesizesum}")

alreadydone = os.listdir("../gamebanana-scrape")

for x in links:
    filename = "../gamebanana-scrape/" + x[1]
    #if os.path.isfile(filename):
    if x[1] in alreadydone:
        continue
    print(f"\ndownloading {x[2]} to {filename}")
    subprocess.check_call(("curl.exe", "--location", "-o", filename, x[0]), shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
    alreadydone.append(x[1])
    time.sleep(0.333)
    #break

