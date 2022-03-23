# ESE 531, HW2 Problem 4

# libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# part a

# parameters
f1 = 4000 # Hz
mu = 600000 # Hz/sec
T = 0.05 # sec

# chirp signal
c_t = np.cos([np.pi * mu * t**2 + 2 * np.pi * f1 * t for t in np.arange(0, 0.05, 0.001)])

# part b

# sampling frequency
fs = 8000 # Hz
N = int(fs * T)

# sampled chirp signal
c_s = np.cos([np.pi * mu * (n/fs)**2 + 2 * np.pi * f1 * n/fs for n in range(N)])

# plot the continuous and sampled signal together
plt.plot(c_s, 'b-')
plt.stem(c_s, markerfmt='r.', linefmt=None)
plt.title("Chirp signal sampled at $f_s =$ 8 kHz")
plt.xlabel("n")
plt.ylabel("c[n]")
plt.show()

# write the chirp signal to a .wav file
write('chirp_8kHz.wav', 44100, c_s)

# part c
fs2 = 70000 # Hz
N2 = int(fs2 * T)

# sampled chirp signal
c_s2 = np.cos([np.pi * mu * (n/fs2)**2 + 2 * np.pi * f1 * n/fs2 for n in range(N2)])

# plot the continuous and sampled signal together
plt.plot(c_s2, 'b-')
plt.stem(c_s2, markerfmt='r.', linefmt=None)
plt.title("Chirp signal sampled at $f_s =$ 70 kHz")
plt.xlabel("n")
plt.ylabel("c[n]")
plt.show()

# write the chirp signal to a .wav file
write('chirp_70kHz.wav', 44100, c_s2)

