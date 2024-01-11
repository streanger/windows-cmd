import json
import os
import sys
from pathlib import Path
from typing import NamedTuple
from rich import print
import pandas as pd


class PackageInfo(NamedTuple):
    package_family_name: str
    package_identity_name: str
    category_id: str


def read_json(filename):
    """read json file to dict"""
    data = {}
    try:
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return data
    
    
# **** directory files ****
directory = Path(r"C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\InstallService")
files = [directory.joinpath(item) for item in os.listdir(directory)]
content = read_json(files[0])

# **** collect data ****
data = []
for path in files:
    content = read_json(path)
    catalog_item = content['catalogItem']
    info = PackageInfo(
        package_family_name=catalog_item['packageFamilyName'],
        package_identity_name=catalog_item['packageIdentityName'],
        category_id=catalog_item['categoryId'],
    )
    data.append(info)

# **** pretty print ****
df = pd.DataFrame(data)
df.index += 1
md = df.to_markdown()
input('press enter to print ')
print(md)
