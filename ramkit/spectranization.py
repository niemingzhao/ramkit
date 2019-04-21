# -*- coding: utf-8 -*-

"""
Spectral Data Conversion and Transform Processing.

>>> import ramkit as rk
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, signal, sparse, special

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def calc_nsd(x, n=21):
    """
    Estimate Noise Standard Deviation of Data.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    n : int
        Size of segment.

    Returns
    -------
    result : float
        Value of noise standard deviation.
    """
    x_diff = np.diff(x, n=2)
    x_frag = np.array_split(x_diff, len(x_diff) // n)
    cursor = np.argmin([np.std(i, ddof=1) for i in x_frag])
    for i in range(n * (cursor + 1), len(x_diff)):
        i_frag = x_diff[i-n:i-1]
        i_frag_avg = np.mean(i_frag)
        i_frag_std = np.std(i_frag, ddof=1)
        if np.abs(x_diff[i] - i_frag_avg) > 3 * i_frag_std:
            x_diff[i] = i_frag_avg
    for i in range(0, n * cursor - 1)[::-1]:
        if n * cursor - 1 < 0:
            break
        i_frag = x_diff[i+1:i+n]
        i_frag_avg = np.mean(i_frag)
        i_frag_std = np.std(i_frag, ddof=1)
        if np.abs(x_diff[i] - i_frag_avg) > 3 * i_frag_std:
            x_diff[i] = i_frag_avg
    return np.std(x_diff, ddof=1) / 6 ** 0.5


def remove_spike(x):
    """
    Remove Spikes of Data.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    x_c = signal.savgol_filter(x, 3, 0)
    res = x - x_c
    std = np.std(res, ddof=1)
    cur = np.where(res > 3.5 * std)
    cur = [range(i - 1, i + 2) for i in cur[0]]
    x_x = np.array(range(len(x)))
    x_m = np.delete(x_x, cur)
    x_n = np.delete(x, cur)
    return np.interp(x_x, x_m, x_n)
