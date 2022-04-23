# ESE 531, Project 2 Part A
# Author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# main function
def main():

    # produce random signal of length 1000 with amplitude +/- 1
    s = np.empty(1000)
    for i in range(1000):
        if np.random.rand() < 0.5:
            s[i] = 1
        else:
            s[i] = -1
    
    # define unit-impulse response
    h = np.array([0.3, 1, 0.7, 0.3, 0.2])

    # compute convolution and generate random gaussian noise 
    x = np.convolve(s, h, mode='same')

    target_snr_db = 20
    x_avg_db = 10 * np.log10(np.mean(x)**2)
    noise_avg_db = x_avg_db - target_snr_db
    noise_avg_pwr = 10 ** (noise_avg_db / 10)
    w = np.random.normal(loc=0, scale=np.sqrt(noise_avg_pwr), size=len(x))

    x = x + w

    # now implement the adaptive equalizer

    # the desired signal will b a delayed version of the original signal
    # delay by two units
    d = np.pad(s, (2,0))[:-2]

    # learning parameters
    mu = 0.0075
    M = 20

    # initialize empty filter of length M+1
    g = np.ones(M)

    # error array
    e_array = []

    for n in range(M,1000):
        
        # pass the channel output through the adaptive filter
        y = np.inner(g, np.flip(x[n-M:n]))

        # execute parameter update via LMS
        e = d[n] - y
        e_array.append(e)
        g = g + 2 * mu * e * np.flip(x[n-M:n])
       

    # plt.plot(s, '.')
    # # plt.show()

    # plt.plot(x, '.')
    # plt.show()

    # plt.plot(np.sign(np.convolve(x, g, mode='same')), '.')
    # plt.show()
    # plt.plot(d)
    # plt.plot(x)
    # plt.plot(np.abs(d - np.convolve(np.convolve(s, h, mode='same'), g, mode='same')))
    plt.plot(np.abs(e_array))
    plt.show()


if __name__ == "__main__":
    main()