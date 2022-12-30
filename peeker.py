
import json
from pathlib import Path
from sanitize_filename import sanitize
import subprocess
import sys

filesizesum = 0

links = []


dddd = Path("gamebanana-items")
for filename in dddd.glob("*.json"):
    with open(filename, "r", encoding="utf-8") as f:
#with open("interesting.txt") as interestingtxt:
#    for interesting in interestingtxt:
#        with open("gamebanana-items/" + interesting.strip(), encoding="utf-8") as f:
            j = json.load(f)
            for file in j["_aFiles"]:
                filesizesum += file["_nFilesize"]
                links.append([file["_sDownloadUrl"], sanitize(str(file["_idRow"]) + "_" + file["_sFile"])])

print(f"filesizesum = {filesizesum}")


for x in links:
    subprocess.check_call(("curl.exe", "-o", x[1], x[0]), shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
    break

