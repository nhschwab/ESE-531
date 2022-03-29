# PART A: FIR FILTER DESIGN USING TRUNCATION
# author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from scipy.io.wavfile import write

'''
LPFtrunc(N)

arguments:

    N: size of impulse response

return:

    h: truncated and shifted impulse response of size N for a LPF filter w/ cutoff wc = 2.0

'''
def LPFtrunc(N):

    # cutoff frequency value
    wc = 2.0 

    # generate an impulse response for values -N/2 to N/2
    h = np.array([(wc/np.pi)*np.sinc(wc*n/np.pi) for n in np.arange(-N/2, N/2)])

    # h = np.concatenate((np.zeros(N), h))
    return h


# main function for part a
def part_a1():

    # use LPFtrunc(N) to generate an impulse response for N=21 and N=101
    # compute the DTFT and plot the magnitude response normalized and in dB

    N_list = [21, 101]

    for N in N_list:
        h = LPFtrunc(N)
        
        # use numpy to compute DTFT and frequency samples of impulse response
        H = np.roll(np.fft.fft(h, 512), int(512/2))
        w = np.linspace(-np.pi, np.pi, 512)

        # plot the normalized magnitude response and dB response
        plt.plot(w, np.abs(H))
        plt.title(r'$|H(e^{j\omega})|$, N=%d' % (N))
        plt.xlabel(r'$\omega$')
        plt.ylabel('Normalized Magnitude')
        plt.show()

        plt.plot(w, 20*np.log10(np.abs(H)))
        plt.title(r'$|H(e^{j\omega})|$, N=%d' % (N))
        plt.xlabel(r'$\omega$')
        plt.ylabel('dB')
        plt.show()

# main function for part b
def part_a2():

    # read in noisy speech file
    noisy_speech = scipy.io.loadmat('Project1/nspeech2.mat')['nspeech2'].flatten()

    noisy_speech_spec = np.roll(np.fft.fft(noisy_speech, 512), int(512/2))
    w = np.linspace(-np.pi, np.pi, 512)

    # plot noisy speech
    plt.plot(w, noisy_speech_spec)
    plt.title('Noisy Speech Spectrum')
    plt.xlabel('w')
    plt.ylabel(r'$|X(e^{j\omega})|$')
    plt.show()

    # generate two LPF impulse responses
    h21 = LPFtrunc(21)
    h101 = LPFtrunc(101)

    # convolve noisy speech with both impulse responses
    filtered_speech21 = np.convolve(noisy_speech, h21)   
    filtered_speech101 = np.convolve(noisy_speech, h101)

    # plot the filtered speech
    filtered_speech21_spec = np.roll(np.fft.fft(filtered_speech21, 512), int(512/2))
    plt.plot(w, np.abs(filtered_speech21_spec))
    plt.title('Filtered Speech Spectrum (N=21)')
    plt.xlabel('w')
    plt.ylabel(r'$|X(e^{j\omega})|$')
    plt.show()

    filtered_speech101_spec = np.roll(np.fft.fft(filtered_speech101, 512), int(512/2))
    plt.plot(w, np.abs(filtered_speech101_spec))
    plt.title('Filtered Speech Spectrum (N=101)')
    plt.xlabel('w')
    plt.ylabel(r'$|X(e^{j\omega})|$')
    plt.show()

    # write the speech to .wav files
    write('noisy_speech.wav', 10000, 3*noisy_speech)
    write('filtered_speech21.wav', 10000, 3*filtered_speech21) 
    write('filtered_speech101.wav', 10000, 3*filtered_speech101)


if __name__ == "__main__":
    part_a2()


