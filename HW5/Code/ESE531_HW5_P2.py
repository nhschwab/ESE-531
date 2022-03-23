# ESE 531: HW5 Problem 2

# Group Delay 

# libraries
import numpy as np
import matplotlib.pyplot as plt

'''
function: gdel

arguments:

    x: signal x[n] at the times (n)
    n: vector of time indices
    Lfft: length of the FFT used

returns:

    gd: Group delay values on [pi, pi)
    w: list of frequencies over [-pi, pi)
'''
def gdel(x, n, Lfft):

    X = np.fft.fft(x, Lfft)
    dXdw = np.fft.fft(n * x, Lfft)
    gd = np.fft.fftshift(np.real(dXdw / X))
    w = (2 * np.pi / Lfft) * np.arange(0, Lfft) - np.pi

    return gd, w


if __name__ == "__main__":

    # generate a shifted unit impulse signal
    n = np.arange(-64, 64, 1)
    delta1 = np.zeros(128)
    delta2 = np.zeros(128)
    delta1[64 + 5] = 1
    delta2[64 - 5] = 1

    # generate and plot group delay
    gd1, w1 = gdel(delta1, n, 128)
    gd2, w2 = gdel(delta2, n, 128)

    # plot the delta functions with corresponding group delays

    fig, axs = plt.subplots(2)

    axs[0].stem(n, delta1)
    axs[0].set_title('Shifted Unit Impulse')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel(r'$\delta[n - 5]$')

    axs[1].plot(w1, gd1)
    axs[1].set_title(r'Group Delay of Shifted Unit Impulse $\delta[n - 5]$')
    axs[1].set_xlabel(r'$\omega$')
    axs[1].set_ylabel(r'$\tau(\omega)$')

    fig.tight_layout()
    plt.show()

    fig, axs = plt.subplots(2)

    axs[0].stem(n, delta2)
    axs[0].set_title('Shifted Unit Impulse')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel(r'$\delta[n + 5]$')

    axs[1].plot(w2, gd2)
    axs[1].set_title(r'Group Delay of Shifted Unit Impulse $\delta[n + 5]$')
    axs[1].set_xlabel(r'$\omega$')
    axs[1].set_ylabel(r'$\tau(\omega)$')
    
    fig.tight_layout()
    plt.show()