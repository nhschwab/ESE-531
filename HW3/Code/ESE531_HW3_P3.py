# ESE 531: HW3 Problem 3

# libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheby2
from scipy.signal import freqz

# parameters
fsim = 80000 # Hz
N_samples = 950
T = N_samples / fsim # sec
fo = 1000 # Hz

# continuous signal
x_t = np.cos([2 * np.pi * fo * t for t in np.arange(0, T, 1/fsim)])

# generate sampled signal
fs = 8000 # Hz
L = int(fsim / fs)
x_n = np.array([x_t[n] for n in np.arange(0, len(x_t), L)])

# part a

# design and implement reconstruction filter
fsim = 80000 # Hz
fs = 8000 # Hz
fcut = 2 * (fs / 2) / fsim # Hz

b, a = cheby2(9, 60, fcut)
w, h = freqz(b, a, whole=True)
w -= np.pi
w *= fs / (2 * np.pi)

# plot the magnitude
plt.plot(w, np.abs(h))
plt.title("Magnitude of Reconstruction Frequency Response")
plt.xlabel("$\Omega$ (Hz)")
plt.ylabel("$|X(j\Omega)|$")
plt.show()

# plot the angle
plt.plot(w, np.unwrap(np.angle(h)))
plt.title("Phase of Reconstruction Frequency Response")
plt.xlabel("$\Omega$ (Hz)")
plt.ylabel("$\measuredangle X(j\Omega)$")
plt.show()

# part b

# zero insert operation
x_prime = np.zeros(len(x_t))

# create zero-padded signal
for i, val in enumerate(x_n):
    x_prime[int(i * len(x_t) / len(x_n))] = x_n[i]

# apply cheby2 filter to generate reconstructed output
x_r = np.convolve(x_prime, np.fft.ifft(h), mode='same')

# plot reconstructed signal
plt.plot(np.arange(0, T, 1/fsim), x_r)
plt.xlabel("t (sec)")
plt.ylabel("$x_r(t)$")
plt.title("Reconstructed Sinusoid Analog Signal")
plt.show()

# compute and plot continuous FT of the x(t)
def fmagplot(xa, dt):
    L = len(xa)
    Nfft = round(2 ** (np.log2(5 * L)))
    Xa = np.fft.fft(xa, Nfft)
    r = np.arange(0, Nfft/4)
    ff = r / Nfft / dt
    return ff , np.abs(Xa[:len(r)])

x, y = fmagplot(x_r, T)

plt.plot(x, y)
plt.title("Continuous Time FT of Reconstructed Analog Sinusoid")
plt.xlabel("$\Omega$ (kHz)")
plt.ylabel("$|X(j\Omega)|$")
plt.show()

