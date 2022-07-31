# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 44100 #Hz
DURATION = 5 #s

def generate_sine_wave(freq,sample_rate,duration):
    x = np.linspace(0,duration,sample_rate*duration, endpoint=False)
    frequencies = x*freq
    y = np.sin((2*np.pi)*frequencies)
    return x,y

x,y = generate_sine_wave(2,SAMPLE_RATE,DURATION)
plt.plot(x,y)
plt.show()

_, nice_tone = generate_sine_wave(400,SAMPLE_RATE,DURATION)
_, noise_tone = generate_sine_wave(4000,SAMPLE_RATE,DURATION)

noise_tone = noise_tone*0.3
mixed_tone = nice_tone + noise_tone
normalized_tone = np.int16((mixed_tone/mixed_tone.max())*32767)

plt.plot(normalized_tone[:1000])
plt.show()

