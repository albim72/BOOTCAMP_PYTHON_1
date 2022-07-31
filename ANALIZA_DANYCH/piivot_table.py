# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
    "A":["jeden","dwa","trzy","trzy"]*3,
    "B":["A","B","C"]*4,
    "C":["Kraków","Toruń","Kraków","Toruń","Kraków","Toruń"]*2,
    "D":np.random.randn(12),
    "E":np.random.randn(12)
    }
)

df

#tworzenie tabeli przestawnej
przest = pd.pivot_table(df,values="D",index=["A","B"], columns=["C"])

przest

przest2 = pd.pivot_table(df,values="E",index=["A"], columns=["C"])

przest2

