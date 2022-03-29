# PART A: FIR DESIGN USING PARKS-McCLELLAN
# author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import remez as remez
from scipy.signal import freqz as freqz


# main function
def part_b():

    # default sampling frequency is 2pi
    fs = 2 * np.pi

    # design specs
    omega_p = 1.8
    omega_s = 2.2
    delta_p = 0.05
    delta_s = 0.005

    # numtaps, parameter should be altered until optimized
    numtaps = 30

    # array of frequencies
    bands = [0, omega_p, omega_s, np.pi]

    # desired values in frequency ranges
    des_response = [1, 0]

    # weighting
    wgt = [delta_s/delta_p, 1]

    # use Parks-McClellan algo to compute impulse response of filter
    h = remez(numtaps, bands, des_response, weight=wgt, fs=fs)

    # compute DTFT of h
    w, H = freqz(h, [1], whole=True)
    H = np.roll(H, int(512/2))
    w = np.linspace(-np.pi, np.pi, 512)

    # plot the frequency response and specs on same graph
    plt.plot(w, np.abs(H))
    plt.axhline(y=1+delta_p, color='r')
    plt.axhline(y=1-delta_p, color='r')
    plt.axhline(y=delta_s, color='r')
    plt.axvline(x=omega_p, color='r')
    plt.axvline(x=omega_s, color='r')
    plt.ylim(0, 1.2)
    plt.title(r'$|H(e^{j\omega})|$')
    plt.xlabel(r'$\omega$')
    plt.ylabel('Normalized Magnitude')
    plt.show()

    # plot the frequency response on dB scale
    plt.plot(w, 20*np.log10(np.abs(H)))
    plt.title(r'$|H(e^{j\omega})|$')
    plt.xlabel(r'$\omega$')
    plt.ylabel('dB')
    plt.show()

    # compute and print filter length, passband ripple, and stopband ripple
    print(f'Filter length: {numtaps}')
    
    passband_ripple = max(np.abs(H)) - 1
    print(f'Passband ripple: {passband_ripple}')

    stopband_vals = np.abs(H)[np.where(w > omega_s)[0]]
    stopband_ripple = max(stopband_vals)
    print(f'Stopband ripple: {stopband_ripple}')


if __name__ == "__main__":
    part_b()



