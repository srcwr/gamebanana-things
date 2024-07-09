# SPDX-License-Identifier: WTFPL

from pathlib import Path
import time
import requests
import prettyjson
import random

# Counter-Strike: Source -> Mods -> Maps
# https://gamebanana.com/mods/cats/5535
# https://gamebanana.com/apiv8/Mod/ByCategory?_aCategoryRowIds[]=5535&_nPage=1&_nPerpage=50&_csvProperties=_aFiles,_idRow,_sName
# https://gamebanana.com/apiv4/Mod/413079
# https://gamebanana.com/apiv8/Mod/ByCategory?_aCategoryRowIds[]=5535&_nPerpage=50&_csvProperties=_aFiles,_idRow,_sName,_aAlternateFileSources,_aLatestUpdates,_sText&_csvFlags=FILE_METADATA&_nPage=1

#apiurl = "https://gamebanana.com/apiv8/Mod/ByCategory?_aCategoryRowIds[]=5535&_nPerpage=50&_csvProperties=_aFiles,_idRow,_sName,_aAlternateFileSources,_aLatestUpdates,_sText&_csvFlags=FILE_METADATA&_nPage="
apiurl = "https://gamebanana.com/apiv8/Mod/ByCategory?_nPerpage=15&_csvProperties=_aFiles,_idRow,_sName,_aAlternateFileSources,_aLatestUpdates,_sText&_csvFlags=FILE_METADATA&_sOrderBy=_tsDateUpdated,DESC"
#https://gamebanana.com/apiv11/Mod/Index?_nPerpage=15&_sSort=Generic_LatestModified&_aFilters%5BGeneric_Category%5D=5535
#https://gamebanana.com/apiv11/Mod/487687?_csvProperties=_aFiles
#https://www.postman.com/s0nought/workspace/gb-api-v11/overview

doprint = False

def fucker(d, category, a, b):
    session = requests.Session()
    for i in range(a, b):
        u = apiurl + "&cachebuster=" + str(random.randint(1,666)) + "&_nPage=" + str(i) + "&_aCategoryRowIds[]=" + str(category)
        #resp = requests.get(u)
        resp = session.get(u)
        #with open(f"gamebanana-pages/{i:03}.json", "wb") as f:
        xd = f"{d}/gamebanana-pages/_{category}_{i:03}.json"
        with open(xd, "wb") as f:
            f.write(resp.content)
            if doprint:
                print(f"write to _{category}_{i:03}.json")
        prettyjson.prettyfile(xd)
        time.sleep(1.5)
    session.close()

def main(d):
    fucker(d, 5535, 1, 2) # up to 785+++
    fucker(d, 95, 1, 2) # up to 38~
    fucker(d, 327, 1, 2) # up to 329~
    fucker(d, 2528, 1, 2) # up to 52~

if __name__ == "__main__":
    doprint = True
    main(".")

"""
dddd = Path("gb-pages")
dddd.mkdir(exist_ok=True)

for filename in dddd.glob("*.json"):
    mapname = filename.stem
    resp = requests.get(f"https://sourcejump.net/api/records/{mapname}?key={api_key}")
    if resp.status_code == 200 and resp.content != b'[]':
        with open(f"sj/{mapname}.json", "ab") as f:
            f.write(resp.content)
            print(f"wrote to {mapname}.json")
    time.sleep(0.3)
"""
