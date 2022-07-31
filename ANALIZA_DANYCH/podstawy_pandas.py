# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

s = pd.Series([1,6,17,np.nan,90,12,45])
s

d = pd.Series(np.random.randn(5), index=["a","b","c","d","e"])
d

s.index

sl = {"marka":"Opel","model":"Vectra","rocznik":2008}
pd.Series(sl)

daty = pd.date_range("20220730",periods=6)
daty

df = pd.DataFrame(np.random.randn(6,4), index=daty, columns=list("ABCD"))
df

df.head(3)

df.tail(2)

df.to_numpy()

df.describe()

df.T

df.sort_index(axis=1, ascending=False)

df.sort_values(by="B")

df.loc["20220802":"20220804",["A","D"]]

df.iloc[2:4]

df.loc[daty[0],"A"]

df.at[daty[0],"A"]

df.iloc[3]

df.iloc[3:5,0:2]

df.iloc[[1,2,4],[0,2]]

#indeksowanie logiczne
df[df["A"]>0]

df[df>0]

df2 = df.copy()
df2["E"] = ["sobota","niedziela","poniedziałek","wtorek","środa","czwartek"]
df2

df2[df2["E"].isin(["wtorek","środa"])]

s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range("20220730",periods=6))
s1

df["F"] = s1
df

df.at[daty[0],"A"] = 0
df

df.iat[0,1] = 0
df

df.loc[:,"D"] = np.array([5]*len(df))
df

df3 = df.copy()
df3[df3>0] = -df3
df3

df1 = df.reindex(index=daty[0:4], columns=list(df.columns) + ["E"])
df1.loc[daty[0]:daty[1],"E"] = 1
df1

df4=df1.dropna(how="any")
df4

df5 = df1.fillna(value=100)
df5

pd.isna(df1)

df.mean()

