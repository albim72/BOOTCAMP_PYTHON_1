# -*- coding: utf-8 -*-

# -- Sheet --

from cycler import cycler
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#definicja zestawu danych
cases = [None,
         8,
         (30,8),
         [16,24,30],
         [0,-1],
         slice(200,200,3),
         0.1,
         0.3,
         (0.0,0.1),
         (0.45,0.1)
         ]

colors = [
         '#1f77b4',
         '#ff7f0e',
         '#2ca02c',
         '#d62728',
         '#9467bd',
         '#8c564b',
         '#e377c2',
         '#7f7f7f',
         '#bcbd22',
         '#17becf'
]

mpl.rcParams['axes.prop_cycle'] = cycler(markevery=cases, color=colors)
x = np.linspace(0,2*np.pi)
offsets = np.linspace(0,2*np.pi,11,endpoint=False)
yy = np.transpose([np.sin(x+phi) for phi in offsets])

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.6,0.75])

for i in range(len(cases)):
    ax.plot(yy[:,i],marker='o',label=str(cases[i]))
    ax.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad =0.)

plt.title('wyświetlenie grupy wykresów cyklicznych....')
plt.show()

