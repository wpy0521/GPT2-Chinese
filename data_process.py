import os
import pandas as pd 
import json

data = pd.read_csv("paragrah.csv")
data = data[data["paratype"]==3]
content = list(data["contents"])
print(len(content))
with open("train.json",'w') as f:
    json.dump(content, f)
