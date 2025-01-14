# SPDX-License-Identifier: WTFPL

# /// script
# dependencies = [
#   "GitPython",
#   "requests",
# ]
# ///

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
import urllib.error
import requests

def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

def main(d, callback, fuck_you_callback):
    filesizesum = 0
    links = []
    repo = Repo(d)
    for item in repo.index.diff("HEAD"):
        if "gamebanana-items" in item.a_path:
            with open(d + "/" + item.a_path, "r", encoding="utf-8") as f:
                j = json.load(f)
                for file in j["_aFiles"]:
                    filesizesum += file["_nFilesize"]
                    links.append([file["_sDownloadUrl"], sanitize(str(file["_idRow"]) + "_" + file["_sFile"]), j["_sName"], file["_nFilesize"], j["_idRow"]])

    #print(f"filesizesum = {filesizesum}")

    alreadydone = os.listdir(d+"/../gamebanana-scrape")

    new_items = []

    session = requests.Session()

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
        for i in range(3):
            req = session.get(x[0], stream=True)
            if (req.status_code >= 200 and req.status_code < 400) or req.status_code == 404:
                break
            fuck_you_callback(str(req.status_code) +" on "+x[0])
            time.sleep(10)
        if req.status_code < 200 or req.status_code >= 400:
            if req.status_code == 404:
                fuck_you_callback(str(req.status_code) +" on "+x[0])
            new_items.pop()
        else:
            req.raw.decode_content = True
            with open(filename, 'wb') as out:
                shutil.copyfileobj(req.raw, out)
            alreadydone.append(x[1])
        time.sleep(0.333)
        #break

    session.close()
    return new_items

if __name__ == "__main__":
    main(".", print)
