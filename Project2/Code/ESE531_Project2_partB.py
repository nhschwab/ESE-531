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
    x = np.convolve(s, h)
    
    target_snr_db = 20
    x_avg_db = np.mean(10 * np.log10(x**2))
    noise_avg_db = x_avg_db - target_snr_db
    noise_avg_pwr = 10 ** (noise_avg_db / 10)
    w = np.random.normal(loc=0, scale=np.sqrt(noise_avg_pwr), size=len(x))

    x = x + w

    # now implement the adaptive equalizer

    


if __name__ == "__main__":
    main()