# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import matplotlib.pyplot as plt

cases = [
    None,
    8,
    (30,8),
    [16,24,32],
    [0,-1],
    slice(200,200,3),
    0.1,
    0.4,
    (0.2,0.4)
]

delta = 0.11
x = np.linspace(0,10-2*delta,200) + delta
y = np.sin(x)+1.0 + delta

#kreślenie wykresu
fig,axs = plt.subplots(3,3,figsize=(10,6), constrained_layout = True)
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'wykres -> {markevery}')
    ax.plot(x,y,'o',ls='-',ms=4,markevery = markevery)

#kreślenie wykresu w skali logarytmicznej
fig,axs = plt.subplots(3,3,figsize=(10,6), constrained_layout = True)
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'wykres -> {markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x,y,'o',ls='-',ms=4,markevery = markevery)

#kreślenie wykresu - w zakresie
fig,axs = plt.subplots(3,3,figsize=(10,6), constrained_layout = True)
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'wykres -> {markevery}')
    ax.plot(x,y,'o',ls='-',ms=4,markevery = markevery)
    ax.set_xlim((6,6.67))
    ax.set_ylim((1.1,1.7))

#kreślenie wykresu w układzie polarnym
fig,axs = plt.subplots(3,3,figsize=(10,6), constrained_layout = True, subplot_kw={'projection':'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'wykres -> {markevery}')
    ax.plot(x,y,'o',ls='-',ms=4,markevery = markevery)
plt.show()
