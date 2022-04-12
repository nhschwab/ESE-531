# ESE 531: HW8 Problem 4
# Author: Noah Schwab

# import libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat as loadmat

# load in tones.mat file
s =loadmat('/Users/noahhschwab/Desktop/ESE-531/HW8/tones.mat')
x = np.ravel(s['y1'])

# compute the 25-point DFT of x and plot its magnitude
X = np.fft.fft(x, n=25)

plt.plot(np.abs(X))
plt.title('25-point DFT of x')
plt.xlabel('k')
plt.ylabel('X[k]')
plt.show()

# compute the 50-point DFT of x and plot its magnitude
X = np.fft.fft(x, n=50)

plt.plot(np.abs(X))
plt.title('50-point DFT of x')
plt.xlabel('k')
plt.ylabel('X[k]')
plt.show()

# compute the 100-point DFT of x and plot its magnitude
X = np.fft.fft(x, n=100)

plt.plot(np.abs(X))
plt.title('100-point DFT of x')
plt.xlabel('k')
plt.ylabel('X[k]')
plt.show()

# compute the 500-point DFT of x and plot its magnitude
X = np.fft.fft(x, n=500)

plt.plot(np.abs(X))
plt.title('500-point DFT of x')
plt.xlabel('k')
plt.ylabel('X[k]')
plt.show()