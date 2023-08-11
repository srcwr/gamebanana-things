
import json
from pathlib import Path
from sanitize_filename import sanitize
import subprocess
import sys
import os.path
import time
import csv
from git import Repo
import shutil
import urllib.request

def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

def main(d, callback):
    filesizesum = 0
    links = []
    repo = Repo(d)
    for item in repo.index.diff("HEAD"):
        if "gamebanana-items" in item.a_path:
            with open(item.a_path, "r", encoding="utf-8") as f:
                j = json.load(f)
                for file in j["_aFiles"]:
                    filesizesum += file["_nFilesize"]
                    links.append([file["_sDownloadUrl"], sanitize(str(file["_idRow"]) + "_" + file["_sFile"]), j["_sName"], file["_nFilesize"], j["_idRow"]])

    print(f"filesizesum = {filesizesum}")

    alreadydone = os.listdir(d+"/../gamebanana-scrape")

    new_items = []

    for x in links:
        filename = d + "/../gamebanana-scrape/" + str(x[4]) + "_" + x[1]
        if (str(x[4]) + "_" + x[1]) in alreadydone:
            #f2 = "../gamebanana-scrape/" + str(x[4]) + "_" + x[1]
            #print(f"rename {filename} to {f2}")
            #os.rename(filename, f2)
            continue
        new_items.append(str(x[4]) + "_" + x[1])
        callback(new_items[-1])
        """
        try:
            if os.path.getsize(filename) == x[3]:
                continue
        except:
            continue
        """
        print(f"\ndownloading {x[2]} to {filename}")
        req = urllib.request.urlopen(x[0])
        with open(filename, 'wb') as out:
            shutil.copyfileobj(req, out)
        #subprocess.check_call(("curl.exe", "--location", "-o", filename, x[0]), shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
        alreadydone.append(x[1])
        time.sleep(0.333)
        #break
    return new_items

if __name__ == "__main__":
    def nop(arg):
        pass
    main(".", nop)
