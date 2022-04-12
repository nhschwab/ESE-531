# ESE 531: HW6 Problem 2
# Author: Noah Schwab

# import libraries
import numpy as np 
import time
import matplotlib.pyplot as plt

'''
DFT_A(x)

arguments:

    x: signal to be transformed, assumed to be one period

return

    X: DFT of input signal x, this function executes a nested for loop
'''
def DFT_A(x):

    # N is length of one period of x
    N = len(x)

    # instantiate empty array X to compute values 
    X = np.empty(N, dtype=complex)

    # iterate through each value of k in range N
    t0 = time.time()
    for k in range(N):

        # nested loop to interate through each value of n in range N
        for n in range(N):

            # populate X with DFT value
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    t1 = time.time()
    print(f'Two-Loop Run time: {t1-t0}')

    # return DFT of x, X
    return X

'''
DFT_B(x):

arguments:

    x: signal to be transformed, assumed to be one period

return

    X: DFT of input signal x, this function executes one for loop and an inner product
'''
def DFT_B(x):

    # N is length of one period of x
    N = len(x)

    # instantiate empty array X to compute values
    X = np.empty(N, dtype=complex)

    # iterate through each value of k in range N and compute X[k] via an inner product
    t0 = time.time()
    for k in range(N):
        
        # predefine vector W for inner product
        W = np.array([np.exp(-2j * np.pi * k * n / N) for n in range(N)])

        # comptue inner product
        X[k] = np.dot(x, W)
    t1 = time.time()
    print(f'One-Loop Run time: {t1-t0}')
    
    return X

'''
DFT_C(x):

arguments:

    x: signal to be transformed, assumed to be one period, must be a column vector

return:

    X: DFT of input signal, this function executes a matrix multiplication
'''
def DFT_C(x):
    
    # N is length of one period of x
    N = len(x)

    # predefine matrix W
    W = np.empty((N, N), complex)

    for k in range(N):
        W[k] = [np.exp(-2j * np.pi * k * n / N) for n in range(N)]

    # execute matrix multiplication
    t0 = time.time()
    X = W @ x
    t1 = time.time()
    print(f'No-Loop Run time: {t1-t0}')

    # return transpose to convert X to row vector
    return X.T

def main():


    # test signal
    N = 1000
    x = np.cos([np.pi * n / 100 for n in range(N)])
    plt.title('Test Signal')
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.stem(x)
    plt.show()

    # compute DFT using built-in FFT function
    t0 = time.time()
    X0 = np.fft.fft(x)
    t1 = time.time()
    print(f'FFT Run time: {t1-t0}')


    # compute DFT using my functions
    X1 = DFT_A(x)
    X2 = DFT_B(x)
    X3 = DFT_C(x)

    # plot each DFT to show they are equivalent
    plt.plot(X0)
    plt.title('DFT Computed using FFT')
    plt.xlabel('k')
    plt.ylabel(r'$\tilde{X}$')
    plt.show()

    plt.plot(X1)
    plt.title('DFT Computed using Two Loops')
    plt.xlabel('k')
    plt.ylabel(r'$\tilde{X}$')
    plt.show()

    plt.plot(X2)
    plt.title('DFT Computed using One Loop')
    plt.xlabel('k')
    plt.ylabel(r'$\tilde{X}$')
    plt.show()

    plt.plot(X3)
    plt.title('DFT Computed using No Loops')
    plt.xlabel('k')
    plt.ylabel(r'$\tilde{X}$')
    plt.show()


if __name__ == "__main__":
    main()







