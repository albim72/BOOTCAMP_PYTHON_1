import os
from dateutil.parser import parse

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


#przygotowanie zbioru danych
path = 'AirPassengers.csv'
df = pd.read_csv(path)

print(df.head())

df.columns = ['Date','Number of Passengers']

print(df.head())

#wizualizacja szeregów czasowych
def plot_df(df,x,y,title="",xlabel='Data',ylabel="Liczba pasażerów",dpi=100):
    plt.figure(figsize=(15,4),dpi=dpi)
    plt.plot(x,y,color='tab:red')
    plt.gca().set(title=title,xlabel=xlabel,ylabel=ylabel)
    plt.show()

plot_df(df,x=df['Date'],y=df['Number of Passengers'], title = "Licza pasażerów US Airlines lata 1949-1969")


#multiplikatywna dekompozycja szeregu czasowego

multiplicative_decomposition = seasonal_decompose(df['Number of Passengers'], model='multiplicative', period=30)

#addytywna dekompozycja
additive_decomposition = seasonal_decompose(df['Number of Passengers'], model='additive', period=30)

#wykreślanie
plt.rcParams.update({'figure.figsize':(16,12)})
multiplicative_decomposition.plot().suptitle('Kompozycja Multiplikatywna',fontsize=16)
plt.tight_layout(rect=[0,0.03,1,0.95])

additive_decomposition.plot().suptitle('Kompozycja Addytywna',fontsize=16)
plt.tight_layout(rect=[0,0.03,1,0.95])

plt.show()

