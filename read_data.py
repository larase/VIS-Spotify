import pandas as pd

df = pd.read_csv("top10s.csv", encoding = 'unicode_escape', engine ='python')

print(df)

"""
Aufgabe 11b Template

import numpy as np

list = df['pop']

print(np.mean(list))
print(np.std(list))
print(np.var(list))
print(np.median(list))
print(np.max(list))
"""