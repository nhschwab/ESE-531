# ESE 531: HW3 Problem 2

# libraries 
import numpy as np
import matplotlib.pyplot as plt 

# part a

# generate a simulated sinusoid analog signal 

# parameters
fsim = 80000 # Hz
N_samples = 950
T = N_samples / fsim # sec
fo = 1000 # Hz

x_t = np.cos([2 * np.pi * fo * t for t in np.arange(0, T, 1/fsim)])

# plot analog signal
plt.plot(np.arange(0, T, 1/fsim), x_t)
plt.xlabel("t (sec)")
plt.ylabel("$x(t)$")
plt.title("Simulated Sinusoid Analog Signal")
plt.show()

# part b

# compute and plot continuous FT of the x(t)
def fmagplot(xa, dt):
    L = len(xa)
    Nfft = round(2 ** (np.log2(5 * L)))
    Xa = np.fft.fft(xa, Nfft)
    r = np.arange(0, Nfft/4)
    ff = r / Nfft / dt
    return ff , np.abs(Xa[:len(r)])

x, y = fmagplot(x_t, T)

plt.plot(x, y)
plt.title("Continuous Time FT of Analog Sinusoid")
plt.xlabel("$\Omega$ (kHz)")
plt.ylabel("$|X(j\Omega)|$")
plt.show()

# part c

# generate sampled signal
fs = 8000 # Hz
L = int(fsim / fs)
x_n = np.array([x_t[n] for n in np.arange(0, len(x_t), L)])

plt.stem(x_n)
plt.title("Sampled Sinusoid")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.show()

# part d

# compute and plot the DTFT of discrete signal
X_d = np.fft.fft(x_n, len(x_n))
# X_d = np.roll(X_d, int(len(X_d)/2))

plt.plot(np.arange(0, fs - 1, fs/(len(X_d))), np.abs(X_d))
plt.title("DTFT of Discrete Sinusoid")
plt.xlabel("$\omega$ (Hz)")
plt.ylabel("$X(e^{j\omega})$")
plt.show()
