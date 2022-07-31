# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

ts = pd.Series(np.random.randn(1000),index = pd.date_range("2019-01-23",periods=1000))
ts = ts.cumsum() #suma kumulacyjna
ts.plot()

df = pd.DataFrame(np.random.randn(1000,4), index=ts.index, columns=["A","B","C","D"])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc="best")

df.to_csv("sumy.csv")

pd.read_csv("sumy.csv")

df.to_excel("dane.xlsx",sheet_name="Arkusz1")

