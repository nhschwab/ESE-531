# ESE 531: HW5 Problem 3

# Causal First-Order System

# libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
from ESE531_HW5_P2 import gdel

# generate impulse response of given system function
h = np.zeros(128)
h[64] = 1
y = lfilter([1], [1, -0.77], h)
n = np.arange(-64, 64, 1)

# part a

# plot the impulse response
plt.stem(n, y)
plt.title('Impulse Response of System')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.show()

# part b

# generate frequency response magnitude
f_mag = np.abs(np.fft.fft(y, 128, norm="ortho"))
f_mag = np.fft.fftshift(f_mag)

# generate group delay
gd, w = gdel(y, n, 128)

# plot the frequency response magnitude and group delay
fig1, axs1 = plt.subplots(2)

axs1[0].plot(w, f_mag)
axs1[0].set_title('Frequency Response Magnitude')
axs1[0].set_xlabel(r'$\omega$')
axs1[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs1[1].plot(w, gd)
axs1[1].set_title('Group Delay')
axs1[1].set_xlabel(r'$\omega$')
axs1[1].set_ylabel(r'$\tau(\omega)$')

fig1.tight_layout()

plt.show()

# part c

# repeat parts a and b for a pole at 0.95
y2 = lfilter([1], [1, -0.95], h)
n2 = np.arange(-64, 64, 1)

plt.stem(n2, y2)
plt.title('Impulse Response of System')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.show()

f_mag2 = np.abs(np.fft.fft(y2, 128, norm="ortho"))
f_mag2 = np.fft.fftshift(f_mag2)

gd2, w2 = gdel(y2, n2, 128)

fig2, axs2 = plt.subplots(2)

axs2[0].plot(w2, f_mag2)
axs2[0].set_title('Frequency Response Magnitude')
axs2[0].set_xlabel(r'$\omega$')
axs2[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs2[1].plot(w2, gd2)
axs2[1].set_title('Group Delay')
axs2[1].set_xlabel(r'$\omega$')
axs2[1].set_ylabel(r'$\tau(\omega)$')

fig2.tight_layout()

plt.show()