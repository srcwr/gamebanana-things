
import json
from pathlib import Path
from sanitize_filename import sanitize
import subprocess
import sys
import os.path
import time
import csv
from git import Repo

filesizesum = 0

links = []


"""
interesting:
cd gamebanana-items
rg --sort-files -l "(xc|kz|bh|bhop|surf|climb|trikz|jump|bunny|kreedz|xtreme|hop)" > ../interesting.txt
cd ..
"""

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
                links.append([file["_sDownloadUrl"], sanitize(str(file["_idRow"]) + "_" + file["_sFile"]), j["_sName"], file["_nFilesize"], j["_idRow"]])
"""

repo = Repo(".")
for item in repo.index.diff(None):
    if item.a_path.startswith("gamebanana-items"):
        with open(item.a_path, "r", encoding="utf-8") as f:
            j = json.load(f)
            for file in j["_aFiles"]:
                filesizesum += file["_nFilesize"]
                links.append([file["_sDownloadUrl"], sanitize(str(file["_idRow"]) + "_" + file["_sFile"]), j["_sName"], file["_nFilesize"], j["_idRow"]])

print(f"filesizesum = {filesizesum}")

alreadydone = os.listdir("../gamebanana-scrape")

def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

"""
mapper = {}
mapper["note"] = "note"

for x in links:
    fucker = rchop(rchop(rchop(x[1], ".zip"), ".rar"), ".7z")
    mapper[fucker] = str(x[4]) + "_" + fucker

with open("../maps-cstrike/unprocessed/gamebanana-everything-rofl-2.csv", "w", newline="", encoding="utf-8") as outfile:
    cw = csv.writer(outfile)
    cw.writerow(["mapname","filesize","filesize_bz2","sha1","note"])
    with open("../maps-cstrike/unprocessed/gamebanana-everything-rofl.csv", newline='', encoding='utf-8') as infile:
        cr = csv.reader(infile)
        for line in cr:
            xxx = line[4].split('/')
            if xxx[0] in mapper:
                xxx[0] = mapper[xxx[0]]
            else:
                print(xxx[0])
            line[4] = '/'.join(xxx)
            #line[4] = mapper[line[4]]
            cw.writerow(line)
"""

"""
for x in links:
    #break
    x1 = rchop(rchop(rchop(x[1], ".zip"), ".rar"), ".7z")
    filename = "../gamebanana-scrape/fuck2/done/" + x1
    #filename = "../gamebanana-scrape/" + str(x[4]) + "_" + x[1]
    #if (str(x[4]) + "_" + x[1]) in alreadydone:
    if (str(x[4]) + "_" + x[1]) in alreadydone:
        f2 = "../gamebanana-scrape/fuck2/done/" + str(x[4]) + "_" + x1
        print(f"rename {filename} to {f2}")
        try:
            os.rename(filename, f2)
        except:
            print(f"bad {filename}")
        continue
"""
for x in links:
    #break
    #filename = "../gamebanana-scrape/" + x[1]
    filename = "../gamebanana-scrape/" + str(x[4]) + "_" + x[1]
    if (str(x[4]) + "_" + x[1]) in alreadydone:
        #f2 = "../gamebanana-scrape/" + str(x[4]) + "_" + x[1]
        #print(f"rename {filename} to {f2}")
        #os.rename(filename, f2)
        continue
    """
    try:
        if os.path.getsize(filename) == x[3]:
            continue
    except:
        continue
    """
    print(f"\ndownloading {x[2]} to {filename}")
    subprocess.check_call(("curl.exe", "--location", "-o", filename, x[0]), shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
    alreadydone.append(x[1])
    time.sleep(0.333)
    #break

