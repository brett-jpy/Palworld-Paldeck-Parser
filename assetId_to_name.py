import requests
import re
from bs4 import BeautifulSoup

def lookup_pal(pal_name):
    r = requests.get("https://palwiki.io/{}".format(pal_name))
    return r.text

def get_assetid(pal_name):
    soup = BeautifulSoup(lookup_pal(pal_name), features="lxml")
    div = soup.find_all("div", {"class": "resource-item pt-2 pb-2"})

    for d in div:
        if d.text.startswith("AssetID:"):
            asset_id = d.text.split(": ")
            return asset_id[1]

def get_palnames():
    all_pals = []
    r = requests.get("https://raw.githubusercontent.com/mlg404/palworld-paldex-api/main/src/pals.json")
    for pal in r.json():
        all_pals.append(pal['name'])
    return all_pals

if __name__=="__main__":
    final = []
    for palname in get_palnames():
        if bool(re.search(r"\s", palname)) == True:
            palname = palname.replace(" ", "-")
            final.append({"palname_ign": palname, "asset_id": get_assetid(palname)})
        else:
            final.append({"palname_ign": palname, "asset_id": get_assetid(palname)})
    print(final)
