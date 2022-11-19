"""with open("top10s.csv", "r") as f:
    read_data = f.read()

print(read_data)"""

import pandas as pd

df = pd.read_csv("top10s.csv", encoding = 'unicode_escape', engine ='python')

print(df)