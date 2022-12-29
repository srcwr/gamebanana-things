import json
from pathlib import Path

dddd = Path(".")
for filename in dddd.glob("**/*.json"):
    with open(filename, "r+", newline='\n', encoding="utf-8") as f:
        orig = f.read()
        if orig == "":
            continue
        j = json.loads(orig)
        pretty = json.dumps(j, sort_keys=True, indent='\t', separators=(',', ': '), ensure_ascii=False)
        if orig != pretty:
            f.seek(0)
            f.truncate()
            f.write(pretty)

