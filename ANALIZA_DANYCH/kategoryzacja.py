# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "id":[1,2,3,4,5,6],
    "wiersz_opisu":["a","b","b","a","d","f"]
})

df["wiersz"] = df["wiersz_opisu"].astype("category")
print(df["wiersz"])

df["wiersz"].cat.categories=["totalna klapa","tak sobie","dobrze","znakomicie"]
print(df["wiersz"])

df["wiersz"] = df["wiersz"].cat.set_categories(["totalna klapa","kiepsko","tak sobie","dobrze","jest ok","znakomicie"])

print(df["wiersz"])

df.sort_values(by="wiersz")

df.groupby("wiersz").size()

