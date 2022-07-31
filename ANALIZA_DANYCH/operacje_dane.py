# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10,4))
df

lewy = pd.DataFrame({"klucz":["ab","ab"],"wart":[2,4]})
prawy = pd.DataFrame({"klucz":["ab","ab"],"wart":[12,41]})
lewy

prawy

rk = pd.merge(lewy,prawy, on="klucz")
rk

df = pd.DataFrame(
    {
    "A":["ab","zz","ab","zz","ab","zz","ab","ab"],
    "B":["jeden","jeden","dwa","trzy","dwa","dwa","jeden","trzy"],
    "C":np.random.randn(8),
    "D":np.random.randn(8),

    }
)

df

df.groupby("A").sum()

df.groupby(["A","B"]).sum()

krotka = list(
    zip(
        *[
            ["ab","ab","zz","zz","ab","ab","xx","xx"],
            ["czerwony","czarny","czerwony","czarny","czerwony","czarny","czerwony","czarny"],
        ]
    )
)

index = pd.MultiIndex.from_tuples(krotka,names=["pierwszy","drugi"])
df = pd.DataFrame(np.random.randn(8,2), index=index, columns=["A","B"])
df2 = df[:4]
df2

stosik = df2.stack()
print(stosik)

