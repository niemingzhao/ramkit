# -*- coding: utf-8 -*-

"""
Wave Filtering Functions (Smoothing etc.).

>>> import ramkit as rk
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, signal, sparse, special

from .spectranization import calc_nsd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def smooth(x, n=21):
    """
    Smooth Data.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    n : int
        Size of segment.

    Returns
    -------
    result : 1d-ndarray
        Output data.
    """
    x_c, x_t = (x,) * 2
    while True:
        x_t = x_c.copy()
        x_c = signal.savgol_filter(x_t, 3, 0)
        nsd = calc_nsd(x_t, n)
        res = np.sum((x_t - x_c) ** 2 / nsd ** 2)
        if res >= len(x_t):
            break
    return x_c
