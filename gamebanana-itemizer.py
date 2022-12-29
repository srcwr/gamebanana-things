import json
from pathlib import Path

dddd = Path("gamebanana-pages")

#for filename in dddd.glob("*.json"):
for filename in dddd.glob("_*.json"):
    with open(filename, "r") as f:
        j = json.load(f)
    for item in j:
        xd = "gamebanana-items/" + str(item["_idRow"]) + ".json"
        with open(xd, "w", encoding="utf-8") as f:
            json.dump(item, f)
