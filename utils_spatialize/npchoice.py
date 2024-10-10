#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import numba
from numba import njit

@njit
def npchoice(a, p):
    """
    re-implement np.random.choice because weighting is not managed by numba.
    Is 2x faster if we don't have to cumsum here, but for our case it's cleaner to put the cumsum here
    and not slower because we never sample twice with the same p
    /!\ Unlike np.choice:
        - sample a unique element of a with probability array p
    """
    # # sadly we can't raise errors in numba
    #if len(a)==0:
    #    raise ValueError('given array is empty !')
    r = np.random.rand()
    return a[np.searchsorted(p.cumsum(), r, side='left')]
