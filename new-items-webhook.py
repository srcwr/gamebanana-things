
import json
from pathlib import Path
from sanitize_filename import sanitize
import subprocess
import sys
import os.path
import time
import csv
from git import Repo
import requests
import os

links = []

repo = Repo(".")
for item in repo.index.diff("HEAD"):
    if item.a_path.startswith("gamebanana-items"):
        with open(item.a_path, "r", encoding="utf-8") as f:
            j = json.load(f)
            for file in j["_aFiles"]:
                links.append([file["_sDownloadUrl"], sanitize(str(file["_idRow"]) + "_" + file["_sFile"]), j["_sName"], file["_nFilesize"], j["_idRow"]])

alreadydone = os.listdir("../gamebanana-scrape")
death = True

for x in links:
    filename = "../gamebanana-scrape/" + str(x[4]) + "_" + x[1]
    if (str(x[4]) + "_" + x[1]) in alreadydone:
        continue
    death = False

    print("\nfound {filename}")
    open(filename, "w").close()

    data = {
        "content": "message",
        "username": "gamebanana peeper",
        "embeds": [],
    }
    result = requests.post(os.environ.get("WEBHOOK_URL"), json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

    time.sleep(0.333)

if death:
    sys.exit(1)
