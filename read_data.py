import pandas as pd
import plotly.express as px

df = pd.read_csv("top10s.csv", encoding='unicode_escape', engine='python')


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

# Making lists from the attributes
pop_list = []
for line in df['pop']:
    pop_list.append(line)

dnce_list = []
for line in df['dnce']:
    dnce_list.append(line)

title_list = []
for line in df['title']:
    title_list.append(line)

bpm_list = []
for line in df['bpm']:
    bpm_list.append(line)

spch_list = []
for line in df['spch']:
    spch_list.append(line)

nrgy_list = []
for line in df['nrgy']:
    nrgy_list.append(line)


# Scatter Plot
fig = px.scatter(df, df["pop"], df["dnce"], labels={"pop": "Popularity", "dnce": "Danceability"})
fig.show()

# Aufgabe 12 a+b

# Histogram
histogram = px.histogram(df, x=nrgy_list, labels={"x": "Energy"})
#histogram.show()

# Scatterplot matrix
scatter_matrix = px.scatter_matrix(df, dimensions=["acous", "live", "nrgy", "val", "dnce"], color="pop")
#scatter_matrix.show()
