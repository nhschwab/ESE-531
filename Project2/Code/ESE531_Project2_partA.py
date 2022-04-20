# ESE 531, Project 2 Part A
# Author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt 

# function for first part of Part A
def part1():

    # define time array 
    t = np.arange(0, 20, 0.01)

    # define input signal and noise signal
    w = 3 * 2 * np.pi
    w_noise = 14 * 2 * np.pi 

    x_noise = 6 * np.cos(w_noise * t)
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

    return None

# function for second part of Part A
def part2():

     # define time array 
    t = np.arange(0, 20, 0.01)

    # define input signal and noise signal
    w = 3 * 2 * np.pi
    w_noise = 14 * 2 * np.pi 

    x_noise = 6 * np.cos(w_noise * 0.5 * t**2)
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
    plt.show()

    return None

    # repeat part 1, but noise signal has variable frequency


if __name__ == "__main__":
    part2()
