# PART B: MULTI-CHANNEL FIR FILTER-BANK IN ONE DIMENSION
# author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin as firwin
from scipy.signal import freqz as freqz

'''
pr_fb(x)

arguments:

    x: input signal

return:

    y: perfectly reconstructed signal
'''
def pr_fb():

    # first design h0, the impulse response of a low-pass filter which passes
    # frequncies 0 to pi/2

    fs = 2 * np.pi
    cutoff = np.pi / 2
    numtaps = 19 # must be odd to be Type I FIR Filter

    # low-pass FIR filter using Hamming window
    h0 = firwin(numtaps, cutoff, fs=fs)
    _, H0 = freqz(h0, [1], worN=512, whole=True)
    H0 = np.roll(H0, int(512/2))
    w = np.linspace(-np.pi, np.pi, 512)
    plt.plot(w, np.abs(H0))
    # plt.show()

    # define high-pass filter impulse response h1 according to quadrature mirror design
    h1 = np.exp([1j * np.pi * n for n in range(len(h0))]) * h0
    _, H1 = freqz(h1, [1], worN=512, whole=True)
    H1 = np.roll(H1, int(512/2))
    plt.plot(w, np.abs(H1))
    plt.show()


    return 


if __name__ == "__main__":
    pr_fb()