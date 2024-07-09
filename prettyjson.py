# SPDX-License-Identifier: WTFPL

import json
from pathlib import Path

def prettystr(bin):
    j = json.loads(bin.decode("utf-8"))
    return json.dumps(j, sort_keys=True, indent='\t', separators=(',', ': '), ensure_ascii=False)

def prettyfile(filename):
    with open(filename, "r+", newline='\n', encoding="utf-8") as f:
        orig = f.read()
        if orig == "":
            return
        j = json.loads(orig)
        pretty = json.dumps(j, sort_keys=True, indent='\t', separators=(',', ': '), ensure_ascii=False)
        if orig != pretty:
            f.seek(0)
            f.truncate()
            f.write(pretty)

if __name__ == '__main__':
    dddd = Path(".")
    for filename in dddd.glob("**/*.json"):
        prettyfile(filename)

