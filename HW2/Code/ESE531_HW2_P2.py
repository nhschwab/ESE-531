# ESE 531, HW2 Problem 2

# libraries
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# domain of signal
N = 100

# compute the DTFT of x[n] = (0.9)^n * u[n]
x = np.array([(0.9 ** n) for n in range(0, N + 1)])
w, X = signal.freqz(x, whole=True)

# part a

# shift vectors from [0, 2pi] to [-pi, pi)
X = np.roll(X, int(len(X)/2))
w = np.linspace(-np.pi, np.pi, len(X))

# plot the magnitude 
plt.plot(w, np.abs(X))
plt.title("Magnitude of $X(e^{j\omega}$) vs. $\omega$")
plt.xlabel("$\omega$")
plt.ylabel("$|X(e^{j\omega})|$")
plt.show()

# plot the phase
plt.plot(w, np.angle(X))
plt.title("Phase of $X(e^{j\omega}$) vs. $\omega$")
plt.xlabel("$\omega$")
plt.ylabel("$\measuredangle X(e^{j\omega})$")
plt.show()

# part b and c
# formula for magnitude and phase of DTFT of x using tranforms pairs
X_d_mag = [1 / np.sqrt(1.81 - 1.8*np.cos(o)) for o in w]
X_d_phase = [-np.arctan(0.9 * np.sin(o) / (1 - 0.9*np.cos(o))) for o in w]

# plot the magnitude
plt.plot(w, X_d_mag)
plt.title("Magnitude of $X_d(e^{j\omega}$) vs. $\omega$")
plt.xlabel("$\omega$")
plt.ylabel("$|X_d(e^{j\omega})|$")
plt.show()

# plot the phase
plt.plot(w, X_d_phase)
plt.title("Phase of $X_d(e^{j\omega}$) vs. $\omega$")
plt.xlabel("$\omega$")
plt.ylabel("$\measuredangle X_d(e^{j\omega})$")
plt.show()


