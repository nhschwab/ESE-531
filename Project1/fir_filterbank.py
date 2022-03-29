# PART B: MULTI-CHANNEL FIR FILTER-BANK IN ONE DIMENSION
# author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin as firwin
from scipy.signal import freqz as freqz
from scipy.signal import resample as resample
from scipy.signal import butter, lfilter, dlti, dimpulse

'''
filt_and_down(x, h, m)

arguments:

    x: input signal

    h: impulse response

    m: downsampling rate

return:

    y: filtered and downsampled signal
'''
def filt_and_down(x, h, m):

    N = len(x)
    M = len(h)
    y = resample(np.convolve(h, x, mode='same'), num=int(N/m))

    return y

'''
up_and_filt(x, h, l)

arguments:

    x: input signal

    h: impulse response

    l: upsampling rate

return:

    y: upsampled and filtered signal
'''
def up_and_filt(x, h, l):

    N = len(x)
    M = len(h)
    y = np.convolve(h, resample(x, num=l*N), mode='same')

    return y

'''
pr_fb(x)

arguments:

    x: input signal

return:

    y: perfectly reconstructed signal
'''
def pr_fb(x):

    # first design h0, the impulse response of a low-pass filter which passes
    # frequncies 0 to pi/2

    fs = 2*np.pi
    cutoff = np.pi / 2
    numtaps = 50 # must be odd to be Type I FIR Filter

    # low-pass FIR filter using Hamming window
    # _, h0 = dimpulse(dlti(*butter(N=numtaps, Wn=cutoff, fs=fs)), n=numtaps)
    # h0 =np.squeeze(h0)
    h0 = firwin(numtaps, cutoff, fs=fs)
    w, H0 = freqz(h0, [1], worN=512, whole=True)
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
    g0 = h0
    g1 = h1

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
    v1 = np.roll(filt_and_down(filt_and_down(filt_and_down(x, h0, 2), h0, 2), h0, 2), 700)
    v2 = np.roll(filt_and_down(filt_and_down(filt_and_down(x, h0, 2), h0, 2), h1, 2), 700)
    v3 = np.roll(filt_and_down(filt_and_down(x, h0, 2), h1, 2), 400)
    v4 = np.roll(filt_and_down(x, h1, 2), 50)

    plt.stem(v1)
    plt.title('Lower 1/8 Band')
    plt.xlabel('n')
    plt.ylabel(r'$v_1[n]$')
    plt.show()

    plt.stem(v2)
    plt.title('Second 1/8 Band')
    plt.xlabel('n')
    plt.ylabel(r'$v_2[n]$')
    plt.show()

    plt.stem(v3)
    plt.title('Intermediate-Frequency Band')
    plt.xlabel('n')
    plt.ylabel(r'$v_3[n]$')
    plt.show()

    plt.stem(v4)
    plt.title('High-Frequency Band')
    plt.xlabel('n')
    plt.ylabel(r'$v_4[n]$')
    plt.show()

    # upsample and synthesize the sub-bands

    y1 = up_and_filt(v1, g0, 2)
    y2 = up_and_filt(v2, g1, 2)
    y12 = y1 + y2

    y3 = up_and_filt(v3, g1, 2)
    y123 = y3 + up_and_filt(y12, g0, 2)

    y4 = up_and_filt(v4, g1, 2)
    
    y = up_and_filt(y123, g0, 2) + y4

    plt.stem(np.roll(y, 92), markerfmt='ro', basefmt='r-')
    plt.title('Reconstructed Signal')
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.show()

    return 


if __name__ == "__main__":
    x = np.sin([.02 * np.pi * n for n in np.arange(0, 200)]) + np.sin([0.2 * np.pi * n for n in np.arange(0, 200)])
    plt.stem(x)
    plt.title('Input Signal')
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.show()
    pr_fb(x)