# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import matplotlib.pyplot as plt

#przygotowanie funkcji z danymi
t = np.arange(0.0,2.0,0.01)
s = 1 + np.sin(2*np.pi*t)

fig, ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='czas [s]', ylabel = 'napięcie [mV]', title = "zmiana napięcia prądu w czasie....")
ax.grid()
fig.savefig("wykres_sin.png")
plt.show()
