# ESE 531, Project 2 Part A
# Author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import freqz as freqz

# function for first part of Part A
def part1():

    # define time array 
    t = np.arange(0, 20, 0.01)

    # define input signal and noise signal
    w = 2 * np.pi
    w_noise = 6 * 2 * np.pi 

    x_noise = 2 * np.cos(w_noise * t)
    x = np.cos(w * t)
    input = x + x_noise

    # initialize output signal
    y = np.zeros_like(t)

    # desired output
    f = np.zeros_like(t)

    # initialize decomposed IIR signals
    e = np.zeros_like(t)

    # initialize parameter a
    a = np.zeros_like(t)

    # initialize parameters
    w0 = np.pi / 2
    r = 0.9
    mu = 0.005

    # we pass the system the input signal minus the desired signal (which is the noise),
    # and iteratively update the parameters of the filter to minimize the output
    # the result is a notch filter primed to the noise frequency

    x_n = input - x

    for n in range(len(t)-1):

        # band-stop filter 
        e[n] = x_n[n] + a[n] * x_n[n-1] + x_n[n-2]
        y[n] = e[n] - r * a[n] * y[n-1] - r**2 * y[n-2]

        # update parameter
        a[n+1] = a[n] - mu * y[n] * x_n[n-1]

        if abs(a[n]) > 2:
            a[n] = 0

        f[n] = x[n] + y[n]

    plt.plot(f, label='Desired Signal Plus Filtered Input')
    plt.plot(x, label='Desired Signal')
    plt.xlabel('n')
    plt.ylabel('signal value')
    plt.legend()
    plt.show()

    plt.plot(y)
    plt.title('Notch Filter Output Signal')
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.show()

    plt.plot(a)
    plt.xlabel('n')
    plt.ylabel('a')
    plt.show()

    # plot spectra of corrupted signal, frequency response of adpated filter, and spectra of the cleaned signal
    X = np.fft.fft(input)
    w = np.linspace(-np.pi, np.pi, len(X))
    plt.plot(w, X)
    plt.title('Corrupted Signal')
    plt.ylabel(r'$X(e^{j \omega})$')
    plt.xlabel(r'$\omega$')
    plt.show()

    # define numerator and denominator parameters of the notch filter
    num = [1, a[-1], 1]
    den = [1, r * a[-1], r**2]

    _, h = freqz(num, den, whole=True)
    omega = np.linspace(-np.pi, np.pi, len(h))
    plt.plot(omega, h)
    plt.title('Frequency Response of Adaptive Notch Filter After Last Iteration')
    plt.ylabel(r'$H(e^{j \omega})$')
    plt.xlabel(r'$\omega$')
    plt.show()

    Y = np.fft.fft(f)
    plt.plot(w, Y)
    plt.title('Clean Signal')
    plt.ylabel(r'$Y(e^{j \omega})$')
    plt.xlabel(r'$\omega$')
    plt.show()

    return None

# function for second part of Part A
def part2():

     # define time array 
    t = np.arange(0, 20, 0.01)

    # define input signal and noise signal
    w = .5 * 2 * np.pi
    w_noise = .25 * 2 * np.pi 

    x_noise = 2 * np.cos(w_noise * 0.5 * t**2)
    x = np.cos(w * t)
    input = x + x_noise

    # initialize output signal
    y = np.zeros_like(t)

    # desired output
    f = np.zeros_like(t)

    # initialize decomposed IIR signals
    e = np.zeros_like(t)

    # initialize parameter a
    a = np.zeros_like(t)

    # initialize parameters
    w0 = np.pi / 2
    r = 0.85
    mu = 0.005

    # we pass the system the input signal minus the desired signal (which is the noise),
    # and iteratively update the parameters of the filter to minimize the output
    # the result is a notch filter primed to the noise frequency

    x_n = input - x

    for n in range(len(t)-1):

        # band-stop filter 
        e[n] = x_n[n] + a[n] * x_n[n-1] + x_n[n-2]
        y[n] = e[n] - r * a[n] * y[n-1] - r**2 * y[n-2]

        # update parameter
        a[n+1] = a[n] - mu * y[n] * x_n[n-1]

        if abs(a[n+1]) > 2:
            a[n] = 0

        f[n] = x[n] + y[n]

    # plot results

    plt.plot(f, label='Desired Signal Plus Filtered Input')
    plt.plot(x, label='Desired Signal')
    plt.xlabel('n')
    plt.ylabel('signal value')
    plt.legend()
    plt.ylim(-2, 2)
    plt.show()

    plt.plot(y)
    plt.title('Notch Filter Output Signal')
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.show()

    plt.plot(a)
    plt.xlabel('n')
    plt.ylabel('a')
    plt.ylim(-2, -1.5)
    plt.show()

    return None

# function for third part of part A
def part3():

    # repeat part a, except we have to interference frequencies, and the adaptive filter
    # is composed of a cascade of two notc filters, one for each interference frequency

    # define time array 
    t = np.arange(0, 20, 0.01)

    # define input and noise signals
    w = .5 * 2 * np.pi
    w_noise1 = 4 * 2 * np.pi 
    w_noise2 = 10 * 2 * np.pi

    x_noise1 = 2 * np.cos(w_noise1 * t)
    x_noise2 = 2 * np.cos(w_noise2 * t)
    x = np.cos(w * t)

    input = x + x_noise1 + x_noise2

     # initialize output signals
    s1 = np.zeros_like(t)
    s2 = np.zeros_like(t)

    # desired output
    f1 = np.zeros_like(t)
    f2 = np.zeros_like(t)

    # initialize decomposed IIR signals
    e1 = np.zeros_like(t)
    e2 = np.zeros_like(t)

    # initialize parameter a
    a1 = np.zeros_like(t)
    a2 = np.zeros_like(t)

    # initialize parameters
    w0 = np.pi / 2
    r = 0.85
    mu = 0.005

    x_n = input - x

    for n in range(len(t)-1):

        # band-stop filter 
        e1[n] = x_noise1[n] + a1[n] * x_noise1[n-1] + x_noise1[n-2]
        s1[n] = e1[n] - r * a1[n] * s1[n-1] - r**2 * s1[n-2]

        # update parameter
        a1[n+1] = a1[n] - mu * s1[n] * x_noise1[n-1]

        if abs(a1[n+1]) > 2:
            a1[n] = 0

        f1[n] = x[n] + s1[n] + x_noise2[n]

    for m in range(len(t)-1):

        # band-stop filter 
        e2[m] = x_noise2[m] + a2[m] * x_noise2[m-1] + x_noise2[m-2]
        s2[m] = e2[m] - r * a2[m] * s2[m-1] - r**2 * s2[m-2]

        # update parameter
        a2[m+1] = a2[m] - mu * s2[m] * x_noise2[m-1]

        if abs(a2[m+1]) > 2:
            a2[m] = 0

        f2[m] = x[m] + s1[m] + s2[m]

    plt.plot(f1, label='Desired Signal Plus Filtered Input from First Adaptive Notch Filter')
    plt.plot(x, label='Desired Signal')
    plt.xlabel('n')
    plt.ylabel('signal value')
    plt.legend()
    # plt.ylim(-2, 2)
    plt.show()

    plt.plot(f2, label='Desired Signal Plus Filtered Input from Second Adaptive Notch Filter')
    plt.plot(x, label='Desired Signal')
    plt.xlabel('n')
    plt.ylabel('signal value')
    plt.legend()
    # plt.ylim(-2, 2)
    plt.show()

    plt.plot(s1)
    plt.show()

    plt.plot(s2)
    plt.show()

    return None


if __name__ == "__main__":
    part3()
