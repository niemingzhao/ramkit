# -*- coding: utf-8 -*-

"""
Baseline Processing Functions.

>>> import ramkit as rk
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, signal, sparse, special

from .filters import smooth

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def baseline(x, n=21, method='SWMA', **kwargs):
    """
    Estimate Baseline.

    Parameters
    ----------
    x : 1d-ndarray
        Input data.
    n : int
        Size of segment, only for 'SWMA' method.
    method : str {'SWMA', 'arPLS'}
        Method to use for estimation.
    kwargs :
        Keyword arguments passed to method used for estimation.
        For 'arPLS' method:
        * 'lam' -- float, the lambda smoothness parameter, typical values are
        between 10**2 to 10**9, default is 10**5
        * 'ratio' -- float, the ratio parameter, default is 10**-6

    Returns
    -------
    result : 1d-ndarray
        Output baseline data.
    """
    if method == 'SWMA':
        x, win = smooth(x, n), 3
        x_c, x_t = (x,) * 2
        while True:
            x_t = x_c.copy()
            x_c = signal.savgol_filter(x_t, win, 0)
            res = x_t - x_c
            std = np.std(res, ddof=1)
            cur = np.where(res > std)
            if not len(cur[0]):
                break
            x_t[cur] = x_c[cur]
            x_c, win = x_t, win + 2
        baseline = x_c
    elif method == 'arPLS':
        lam = kwargs.get('lam', 1e5)
        ratio = kwargs.get('ratio', 1e-6)
        N = len(x)
        D = sparse.csc_matrix(np.diff(np.eye(N), 2))
        w = np.ones(N)
        while True:
            W = sparse.spdiags(w, 0, N, N)
            Z = W + lam * D.dot(D.transpose())
            z = sparse.linalg.spsolve(Z, w * x)
            d = x - z
            dn = d[d < 0]
            m = np.mean(dn)
            s = np.std(dn)
            wt = 1 / (1 + np.exp(2 * (d - (2 * s - m)) / s))
            if np.linalg.norm(w - wt) / np.linalg.norm(w) < ratio:
                break
            w = wt
        baseline = z
    else:
        baseline = x.copy()
    return baseline
