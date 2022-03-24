# PART B: MULTI-CHANNEL FIR FILTER-BANK IN ONE DIMENSION
# author: Noah Schwab

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import remez as remez
from scipy.signal import freqz as freqz

'''
pr_fb(x)

arguments:

    x: input signal

return:

    y: perfectly reconstructed signal
'''
def pr_fb():
    return 