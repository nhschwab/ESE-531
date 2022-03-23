# ESE 531: HW5 Problem 4

# Anti-Causal First-Order System

# libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
from ESE531_HW5_P2 import gdel

# part a

# generate impulse response by time reversing 
h = np.zeros(128)
h[64] = 1
y = lfilter([1], [1, -0.95], h)
n = np.arange(-64, 64, 1)
y = np.flip(y)

# plot the impulse response
plt.stem(n, y)
plt.title('Impulse Response of System')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.show()

# part b

# generate and plot the frequency response magnitude and group delay

# generate frequency response magnitude
f_mag = np.abs(np.fft.fft(y, 128, norm="ortho"))
f_mag = np.fft.fftshift(f_mag)

# generate group delay
gd, w = gdel(y, n, 128)

# plot the frequency response magnitude and group delay
fig, axs = plt.subplots(2)

axs[0].plot(w, f_mag)
axs[0].set_title('Frequency Response Magnitude')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w, gd)
axs[1].set_title('Group Delay')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\tau(\omega)$')

fig.tight_layout()

plt.show()

# part d

# repeat parts a and b for when the pole is 1/0.77
h = np.zeros(128)
h[64] = 1
y2 = lfilter([1], [1, -0.77], h)
n2 = np.arange(-64, 64, 1)
y2 = np.flip(y2)

plt.stem(n2, y2)
plt.title('Impulse Response of System')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.show()

f_mag2 = np.abs(np.fft.fft(y2, 128, norm="ortho"))
f_mag2 = np.fft.fftshift(f_mag2)

gd2, w2 = gdel(y2, n2, 128)

fig, axs = plt.subplots(2)

axs[0].plot(w2, f_mag2)
axs[0].set_title('Frequency Response Magnitude')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w2, gd2)
axs[1].set_title('Group Delay')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\tau(\omega)$')

fig.tight_layout()

plt.show()