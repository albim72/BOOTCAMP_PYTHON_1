# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100 #ile potrzebujemy punktów czasowych?
samplingInterval = 1/samplingFrequency

beginTime = 0
endTime = 10

signal1Frequency = 4 #4Hz
signal2Frequency = 7 #7Hz

time = np.arange(beginTime,endTime,samplingInterval)

amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

figure,axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)

axis[0].set_title('Funkcja falowa reprezentująca sygnał 4Hz')
axis[0].plot(time,amplitude1)
axis[0].set_xlabel('Czas [s]')
axis[0].set_ylabel('Amplituda')


axis[1].set_title('Funkcja falowa reprezentująca sygnał 7Hz')
axis[1].plot(time,amplitude2)
axis[1].set_xlabel('Czas [s]')
axis[1].set_ylabel('Amplituda')

#złożenie funkcji

amplitude = amplitude1 + amplitude2

axis[2].set_title('Funkcja falowa reprezentująca złożeni sygnałów: 4Hz i 7Hz')
axis[2].plot(time,amplitude)
axis[2].set_xlabel('Czas [s]')
axis[2].set_ylabel('Amplituda')

#transformata Fouriera dla złożenia funkcji falowych

fourierTransform = np.fft.fft(amplitude)/len(amplitude) #normalizacja amplitudy
fourierTransform = fourierTransform[range(int(len(amplitude)/2))]

tpCount = len(amplitude)
values = np.arange(int(tpCount/2))

timePeriod = tpCount/samplingFrequency
frequencies = values/timePeriod

axis[3].set_title('Transformata Fouriera wykreślająca składowe częstotliwości')
axis[3].plot(frequencies,abs(fourierTransform))
axis[3].set_xlabel('Częstotliwość')
axis[3].set_ylabel('Amplituda')

plt.show()

