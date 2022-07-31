# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
mu = 100 #średnia rozkładu
sigma = 15 #średnie odchylenie standardowe
x = mu + sigma*np.random.randn(437)

num_bins = 50

fig,ax = plt.subplots()
n,bins,patches = ax.hist(x,num_bins,density=True)

#definicja linii dopasowania rozkładu
y = ((1/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*(1/sigma*(bins-mu))**2))
ax.plot(bins,y,'--')
ax.set_xlabel('wartości')
ax.set_ylabel('gęstość prawdopodobieństwa')
ax.set_title(r"Histogram wartośc Q: $\mu=100$, $\sigma=15$")
fig.tight_layout()
plt.show()

