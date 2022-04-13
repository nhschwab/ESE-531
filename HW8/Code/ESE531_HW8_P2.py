# ESE 531: HW8 Problem 2
# Author: Noah Schwab

# import libraries
import matplotlib.pyplot as plt
import numpy as np

# part a

# analytical expressision for DTFT of x[n]
w = np.arange(0, 2 * np.pi, 0.01)
X = np.array([(1 - (0.7 * np.exp(-1j * i)) ** 8) / (1 - 0.7 * np.exp(-1j * i)) for i in w])


# plot the magntiude and phase of DTFT
fig, axs = plt.subplots(2)

axs[0].plot(w, np.abs(X))
axs[0].set_title('Magntiude of DTFT')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|X(e^{j \omega})|$')

axs[1].plot(w, np.angle(X))
axs[1].set_title('Phase of DTFT')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\angle X(e^{j \omega})$')

plt.tight_layout()
plt.show()

# part b

# define x
x = np.array([0.7 ** n for n in range(8)])

# compute 8-point DFT and plot its magnitude and phase
X8 = np.fft.fft(x, n=8)

fig, axs = plt.subplots(2)

axs[0].stem(np.abs(X8))
axs[0].set_title('Magntiude of 8-point DFT')
axs[0].set_xlabel(r'k')
axs[0].set_ylabel(r'$|X[k]|$')

axs[1].stem(np.angle(X8))
axs[1].set_title('Phase of 8-point DFT')
axs[1].set_xlabel(r'k')
axs[1].set_ylabel(r'$\angle X[k]$')

plt.tight_layout()
plt.show()

# part c

# compute 16-point DFT and plot its magnitude and phase
# note: np.fft.fft automatically zero pads the input signal if the DFT length is larger than the signal length
X16 = np.fft.fft(x, n=16)

fig, axs = plt.subplots(2)

axs[0].stem(np.abs(X16))
axs[0].set_title('Magntiude of 16-point DFT')
axs[0].set_xlabel(r'k')
axs[0].set_ylabel(r'$|X[k]|$')

axs[1].stem(np.angle(X16))
axs[1].set_title('Phase of 16-point DFT')
axs[1].set_xlabel(r'k')
axs[1].set_ylabel(r'$\angle X[k]$')

plt.tight_layout()
plt.show()

# part d

# compute 128-point DFT and plot its magnitude and phase
# note: np.fft.fft automatically zero pads the input signal if the DFT length is larger than the signal length
X128 = np.fft.fft(x, n=128)

fig, axs = plt.subplots(2)

axs[0].plot(np.abs(X128))
axs[0].set_title('Magntiude of 128-point DFT')
axs[0].set_xlabel(r'k')
axs[0].set_ylabel(r'$|X[k]|$')

axs[1].plot(np.angle(X128))
axs[1].set_title('Phase of 128-point DFT')
axs[1].set_xlabel(r'k')
axs[1].set_ylabel(r'$\angle X[k]$')

plt.tight_layout()
plt.show()