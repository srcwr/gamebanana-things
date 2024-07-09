# SPDX-License-Identifier: WTFPL

import json
from pathlib import Path
import prettyjson

def main(d):
    dddd = Path(f"{d}/gamebanana-pages")
    #for filename in dddd.glob("*.json"):
    for filename in dddd.glob("_*.json"):
        with open(filename, "r", encoding="utf-8") as f:
            j = json.load(f)
        for item in j:
            xd = d + "/gamebanana-items/" + str(item["_idRow"]) + ".json"
            with open(xd, "w", encoding="utf-8") as f:
                json.dump(item, f)
            prettyjson.prettyfile(xd)

if __name__ == "__main__":
    main(".")
