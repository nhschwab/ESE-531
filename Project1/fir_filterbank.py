# PART B: MULTI-CHANNEL FIR FILTER-BANK IN ONE DIMENSION
# author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin as firwin
from scipy.signal import freqz as freqz

'''
downsample(x, m)

arguments:

    x: input signal

    m: downsampling rate

return:

    y: downsampled signal

'''
def downsample(x, m):

    y = np.array([x[i] for i in np.arange(0, len(x), m)])

    return y

'''
upsample(x, l):

arguments:

    x: input signal

    m: upsampling rate

return:

    y: upsampled signal

'''
def upsample(x, l):

    h = np.sinc([i / l for i in range(len(x))])
    y = np.convolve(x, h)

    return y

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
    plt.plot(w, np.abs(H0), label=r'$|H_{0}(e^{j\omega})|$')
    # plt.show()

    # define high-pass filter impulse response h1 according to quadrature mirror design
    h1 = np.exp([1j * np.pi * n for n in range(len(h0))]) * h0
    _, H1 = freqz(h1, [1], worN=512, whole=True)
    H1 = np.roll(H1, int(512/2))
    plt.plot(w, np.abs(H1),  label=r'$|H_{1}(e^{j\omega})|$')

    plt.xlabel(r'$\omega$')
    plt.legend()
    plt.show()

    # define synthesis filters
    g0 = 2 * h0
    g1 = -2 * h1

    _, G0 = freqz(g0, [1], worN=512, whole=True)
    G0 = np.roll(G0, int(512/2))

    _, G1 = freqz(g1, [1], worN=512, whole=True)
    G1 = np.roll(G1, int(512/2))

    plt.plot(w, np.abs(G0), label=r'$|G_{0}(e^{j\omega})|$')
    plt.plot(w, np.abs(G1), label=r'$|G_{1}(e^{j\omega})|$')

    plt.xlabel(r'$\omega$')
    plt.legend()
    plt.show()

    # apply filters in cascade to reconstruct signal
    v0 = 


    return 


if __name__ == "__main__":
    pr_fb()