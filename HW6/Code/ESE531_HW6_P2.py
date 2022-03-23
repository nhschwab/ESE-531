# ESE 531: HW6 Problem 2

# Frequency Response for Difference Equations

# libraries
from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt

# part a

# define numerator and denominator polynomial coefficient arrays
b = [1, 0.5]
a = [1, -1.8 * np.cos(np.pi / 16), 0.81]
w, H = freqz(b, a, worN=512, whole=True)

# plot the magnitude and phase of the frequency response
mag = np.roll(np.abs(H), int(len(w)/2))
phase = np.roll(np.angle(H), int(len(w)/2))
w = np.linspace(-np.pi, np.pi, len(w))

fig, axs = plt.subplots(2)

axs[0].plot(w, mag)
axs[0].set_title('Magntiude Response')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w, phase)
axs[1].set_title('Phase Response')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\angle H(e^{j\omega})$')

fig.tight_layout()
plt.show()

# part b

# redo frequency response only using upper half of unit circle
w2, H2 = freqz(b, a, worN=512, whole=False)

# plot the magnitude and phase of the frequency response
mag2 = np.abs(H2)
phase2 = np.angle(H2)

fig, axs = plt.subplots(2)

axs[0].plot(w2, mag2)
axs[0].set_title('Magntiude Response')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w2, phase2)
axs[1].set_title('Phase Response')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\angle H(e^{j\omega})$')

fig.tight_layout()
plt.show()

# part d

# repeat previous parts with new difference equation
b = [0.16, -0.48, 0.48, -0.16]
a = [1, 0.13, 0.52, 0.3]

w, H = freqz(b, a, worN=512, whole=True)

# plot the magnitude and phase of the frequency response
mag = np.roll(np.abs(H), int(len(w)/2))
phase = np.roll(np.angle(H), int(len(w)/2))
w = np.linspace(-np.pi, np.pi, len(w))

fig, axs = plt.subplots(2)

axs[0].plot(w, mag)
axs[0].set_title('Magntiude Response')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w, phase)
axs[1].set_title('Phase Response')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\angle H(e^{j\omega})$')

fig.tight_layout()
plt.show()

# redo frequency response only using upper half of unit circle
w2, H2 = freqz(b, a, worN=512, whole=False)

# plot the magnitude and phase of the frequency response
mag2 = np.abs(H2)
phase2 = np.angle(H2)

fig, axs = plt.subplots(2)

axs[0].plot(w2, mag2)
axs[0].set_title('Magntiude Response')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w2, phase2)
axs[1].set_title('Phase Response')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\angle H(e^{j\omega})$')

fig.tight_layout()
plt.show()

# part e

# repeat with new difference equation
b = [0.634, 0, -0.634]
a = [1, 0, -0.268]

w, H = freqz(b, a, worN=512, whole=True)

# plot the magnitude and phase of the frequency response
mag = np.roll(np.abs(H), int(len(w)/2))
phase = np.roll(np.angle(H), int(len(w)/2))
w = np.linspace(-np.pi, np.pi, len(w))

fig, axs = plt.subplots(2)

axs[0].plot(w, mag)
axs[0].set_title('Magntiude Response')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w, phase)
axs[1].set_title('Phase Response')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\angle H(e^{j\omega})$')

fig.tight_layout()
plt.show()

# redo frequency response only using upper half of unit circle
w2, H2 = freqz(b, a, worN=512, whole=False)

# plot the magnitude and phase of the frequency response
mag2 = np.abs(H2)
phase2 = np.angle(H2)

fig, axs = plt.subplots(2)

axs[0].plot(w2, mag2)
axs[0].set_title('Magntiude Response')
axs[0].set_xlabel(r'$\omega$')
axs[0].set_ylabel(r'$|H(e^{j\omega})|$')

axs[1].plot(w2, phase2)
axs[1].set_title('Phase Response')
axs[1].set_xlabel(r'$\omega$')
axs[1].set_ylabel(r'$\angle H(e^{j\omega})$')

fig.tight_layout()
plt.show()



