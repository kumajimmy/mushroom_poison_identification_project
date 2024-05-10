from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
import json
import hashlib
import requests
from config import DATABASE_URLS

#fetch dataset
mushroom = fetch_ucirepo(id=73)

#data (as pandas dataframes)
x = mushroom.data.features
y = mushroom.data.targets
df = pd.merge(y, x, left_index=True, right_index=True)

df.fillna('?', inplace=True)

def gen_hash(gillcolor, capcolor, habitat):
  """
  Returns integer value that corresponds to predefined databases based
  on hash number that is generated from mushroom dataset features of
  gill color, cap color, and habitat.
  """
  new_string = f"{gillcolor}{capcolor}{habitat}"
  hash_obj = hashlib.sha256(new_string.encode())
  hash_num = int(hash_obj.hexdigest(), 16)
  return hash_num % len(DATABASE_URLS)

def populate_dbs(row, index, db_links):
  data_json = row.to_json()
  db_id = gen_hash(row['gill-color'], row['cap-color'], row['habitat'])
  target_db = db_links[db_id]
  url = f"{target_db}/{index}.json"
  
  response = requests.put(url, data=data_json)
  if response.status_code != 200:
    print(f"Failed to upload data to {url}. Status code: {response.status_code}")

for index, row in df.iterrows():
    populate_dbs(row, index, DATABASE_URLS)
