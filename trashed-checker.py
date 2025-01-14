# SPDX-License-Identifier: WTFPL

# /// script
# dependencies = [
#   "py7zr==0.22.0",
#   "rarfile==4.2",
#   "requests",
# ]
# ///

import os
import glob
from pathlib import Path
import zipfile
import rarfile
import py7zr
import requests
import subprocess
import time
from urllib.parse import urlparse
import sys

potential_ids = []

print("getting all potential ids...")
"""
for i, filename in enumerate(glob.iglob("gamebanana-fileids/*.json")):
    if os.path.getsize(filename) == 0:
        potential_ids.append(int(Path(filename).stem.replace("_", "")))
    if (i % 10000) == 0 and i != 0:
        print(f"  did {i}")
"""
for line in open("../todo-gb/bhop urls.txt"):
    potential_ids.append(int(line.replace("https://gamebanana.com/dl/", "")))

print("\ngetting all previously scraped ids...")
def remove_from_folder(folder, potential):
    for i, filename in enumerate(glob.iglob(folder+"/*")):
        try:
            dlid = int(Path(filename).stem.split("_")[1].replace("_", ""))
        except:
            print(f" ???? {filename}")
            continue
        if dlid not in potential:
            continue
        print(f"  removing {dlid}")
        potential.remove(dlid)

print("\nremoving stuff...")
remove_from_folder("../gamebanana-scrape", potential_ids)
print("\nremoving stuff-maybe...")
remove_from_folder("../gamebanana-scrape-maybe-trashed", potential_ids)

print("\nhey...")

def get_filelist(filename):
    archive = None
    names = []
    try:
        if filename.endswith(".7z"):
            archive = py7zr.SevenZipFile(filename)
            names = archive.getnames()
        elif filename.endswith(".zip"):
            archive = zipfile.ZipFile(filename)
            names = archive.namelist()
        elif filename.endswith(".rar"):
            archive = rarfile.RarFile(filename)
            names = archive.namelist()
    except:
        print("  bad archive " + filename)
    finally:
        if archive != None:
            archive.close()
    return names

session = requests.Session()

for id in potential_ids: #reversed(potential_ids):
    print(" sending " + str(id))
    r = session.get("https://gamebanana.com/dl/"+str(id), allow_redirects=False)
    if r.status_code != 301 and r.status_code != 302 and r.status_code != 303 and r.status_code != 307 and r.status_code != 308:
        with open(f"../gamebanana-scrape-maybe-trashed/0_{id}__.{r.status_code}", "w") as f:
            print("   failed? and got a " + str(r.status_code))
        continue
    location = r.headers["Location"]
    o = urlparse(location)
    basefn = Path(o.path).name
    subprocess.check_call(("curl.exe", "-o", f"../gamebanana-scrape-maybe-trashed/0_{id}_{basefn}", location), shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
    print("    downloaded ", f"../gamebanana-scrape-maybe-trashed/0_{id}_{basefn}")



#.rar, .zip, and .7z file-list reader & grep for .bsp in filenames...
