# ESE 531: HW8 Problem 3
# Author: Noah Schwab

# import libraries
import matplotlib.pyplot as plt
import numpy as np

# define sequences x[n] and y[n]
x = np.array([1, 1, 1, 1])
y = np.array([1, 1, 1, 1])

# part a 

# perform linear convolution and plot the result
z = np.convolve(x, y)

plt.stem(z)
plt.title('Linear Convolution of x[n] and y[n]')
plt.xlabel('n')
plt.ylabel(r'$x[n] * y[n]$')
plt.show()

# part c

# compute the circular convolution via the DFT
X = np.fft.fft(x)
Y = np.fft.fft(y)

# product of DFT is equivalent to circular convolution of signal
Z = X * Y
z = np.fft.ifft(Z).real

# plot the result
plt.stem(z)
plt.title('Circular Convolution via the DFT')
plt.xlabel('n')
plt.ylabel('z[n]')
plt.show()

# part d

# we can simply repeat part c, but specify the length of DFT, as the fft function will automatically
# zero pad the signal if N is greater than the length of the signal
X = np.fft.fft(x, n=5)
Y = np.fft.fft(y, n=5)
Z = X * Y
z = np.fft.ifft(Z).real

plt.stem(z)
plt.title('Circular Convolution via the 5-point DFT')
plt.xlabel('n')
plt.ylabel('z[n]')
plt.show()

# we know that the signals must be zero-padded to double their length to produce the linear convolution result
X = np.fft.fft(x, n=8)
Y = np.fft.fft(y, n=8)
Z = X * Y
z = np.fft.ifft(Z).real

plt.stem(z)
plt.title('Circular Convolution via the 8-point DFT')
plt.xlabel('n')
plt.ylabel('z[n]')
plt.show()
