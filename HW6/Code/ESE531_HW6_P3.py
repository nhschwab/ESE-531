# ESE 531: HW6 Problem 3

# Frequency Response of a Notch Filter

# libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# part b

# define frequency response function
def H(w, w0):
    return ((1 - np.exp(-1j * (w - w0))) * (1 - np.exp(-1j * (w + w0))) / 
            ((1 - 0.9 * np.exp(-1j * (w - w0))) * (1 - 0.9 * np.exp(-1j * (w + w0)))))

# compute frequency response for w0 = 2pi/5
w = np.arange(-np.pi, np.pi, 1 / (1000 * np.pi))
freq_response = H(w, 2 * np.pi / 5)

# plot the magnitude and phase response
fig, axs = plt.subplots(2)

axs[0].plot(w, np.abs(freq_response))
axs[0].set_title("Magnitude Response")
axs[0].set_xlabel(r"$\omega$")
axs[0].set_ylabel(r"$|H(e^{j\omega})|$")

axs[1].plot(w, np.angle(freq_response))
axs[1].set_title("Phase Response")
axs[1].set_xlabel(r"$\omega$")
axs[1].set_ylabel(r"$\angle H(e^{j\omega})$")

fig.tight_layout()
plt.show()

# part d

# frequency response of notch filter with w0 = 3pi/50
w = np.arange(-np.pi, np.pi, 1 / (1000 * np.pi))
freq_response = H(w, 3 * np.pi / 25)

# plot the magnitude and phase response
fig, axs = plt.subplots(2)

axs[0].plot(w, np.abs(freq_response))
axs[0].set_title("Magnitude Response")
axs[0].set_xlabel(r"$\omega$")
axs[0].set_ylabel(r"$|H(e^{j\omega})|$")

axs[1].plot(w, np.angle(freq_response))
axs[1].set_title("Phase Response")
axs[1].set_xlabel(r"$\omega$")
axs[1].set_ylabel(r"$\angle H(e^{j\omega})$")

fig.tight_layout()
plt.show()

# part e

# generate 60-Hz sinusoid and input to filter from part d
Ts = 1e-3 # sec
n = np.arange(0, 150, 1)
f0 = 60 # Hz
fs = 1000 # Hz
sine_wave = np.sin(2 * np.pi * f0 / fs * n)

w0 = 3 * np.pi / 25
y = lfilter([1, -2 * np.cos(w0), 1], [1, -1.8 * np.cos(w0), 0.81], sine_wave)

# plot the input and output signals
fig, axs = plt.subplots(2)

axs[0].stem(n, sine_wave)
axs[0].set_title("Input Sinusoid")
axs[0].set_xlabel("n")
axs[0].set_ylabel("x[n]")

axs[1].stem(n, y)
axs[1].set_title("Output Signal")
axs[1].set_xlabel("n")
axs[1].set_ylabel("y[n]")

fig.tight_layout()
plt.show()

# part f

# to measure the transcient response duration, we can find the index n at which the 
# ouput response is less than 1% of the input amplitude, and then convert that discrete index
# to a time measurement

ratio_array = np.abs(y / sine_wave)

# binarize ratio_array at a threshold of 0.01
threshold = 0.01
binary_array = np.where(ratio_array > 0.01, 0, 1)

# ignore the first value since 0/0 yields nan
# find the first instance of 1, which corresponds to where in the array the threshold is passed
transcient_index = np.where(binary_array == 1)[0][1]

# sampling period is 1 ms
transcient_time = float(transcient_index) # ms
print(f"The transcient duration is {transcient_time} ms")


