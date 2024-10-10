#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import numba
from numba import njit

@njit
def nptile(a, n):
    """
    re-implement np.tile because it's not managed by numba
    """
    return a.repeat(n).reshape((-1, n)).T.flatten()
