#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import numba
from numba import njit

@njit
def up_and_down_explore(start, min_val, max_val):
    """
    Gives a order in which visiting the indices
    if we start at `start` and we want to visit all the indices between `min_val` and `max_val`
    and we want to visit `start`, then the one just above, then just below, then 2 above, then 2 below...
    """
    path = np.empty(max_val-min_val)
    ipath = 0
    step = 1
    hit_max = start >= max_val-1
    hit_min = start <= min_val
    
    while not hit_min and not hit_max:
        path[ipath] = start
        ipath+=1
        hit_max = start >= max_val-1
        hit_min = start <= min_val
        start += step
        step = -1*(step + np.sign(step))

    while not hit_min:
        path[ipath] = start
        ipath+=1
        hit_min = start <= min_val
        start -= 1
            
    while not hit_max:
        path[ipath] = start
        ipath+=1
        hit_max = start >= max_val-1
        start += 1
    return path    