from pathlib import Path
import time
import requests

# Counter-Strike: Source -> Mods -> Maps
# https://gamebanana.com/mods/cats/5535
# https://gamebanana.com/apiv8/Mod/ByCategory?_aCategoryRowIds[]=5535&_nPage=1&_nPerpage=50&_csvProperties=_aFiles,_idRow,_sName
# https://gamebanana.com/apiv4/Mod/413079
# https://gamebanana.com/apiv8/Mod/ByCategory?_aCategoryRowIds[]=5535&_nPerpage=50&_csvProperties=_aFiles,_idRow,_sName,_aAlternateFileSources,_aLatestUpdates,_sText&_csvFlags=FILE_METADATA&_nPage=1

#apiurl = "https://gamebanana.com/apiv8/Mod/ByCategory?_aCategoryRowIds[]=5535&_nPerpage=50&_csvProperties=_aFiles,_idRow,_sName,_aAlternateFileSources,_aLatestUpdates,_sText&_csvFlags=FILE_METADATA&_nPage="
apiurl = "https://gamebanana.com/apiv8/Mod/ByCategory?_aCategoryRowIds[]=5535&_nPerpage=50&_csvProperties=_aFiles,_idRow,_sName,_aAlternateFileSources,_aLatestUpdates,_sText&_csvFlags=FILE_METADATA&_sOrderBy=_tsDateUpdated,DESC&_nPage="


#for i in range(1, 785):
for i in range(1, 2):
    resp = requests.get(apiurl + str(i))
    #with open(f"gamebanana-pages/{i:03}.json", "wb") as f:
    with open(f"gamebanana-pages/_{i:03}.json", "wb") as f:
        f.write(resp.content)
        print(f"write to {i:03}.json")
    time.sleep(1.5)

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
