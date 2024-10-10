#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import numba
from numba import njit

@njit
def npjoin(a_keycol, a, b_keycol, b, outer_value):
    """
    a_keycol, b_keycol, a, b : all are np.array
    Interpreted as 2 arrays of 2 columns
    sql-style outer join np.arrays a and b on columns akey and bkey
    assume a is sorted by akey and b by bkey
    assume keys do not have repeating values
    Outer join but missing keys are not assigned NaN, rather a (small) value
    Because we may have no key in common
    also it smoothes a bit the impossible flows
    return np of 3 columns :
        key, aval, bval
    """
    r = np.empty((a.shape[0]+b.shape[0], 3))
    ia = 0
    ib = 0
    ir = 0
    while ia<len(a) and ib<len(b):
        if a_keycol[ia]<b_keycol[ib]:
            r[ir, 0] = a_keycol[ia]
            r[ir, 1] = a[ia]
            r[ir, 2] = outer_value
            ia += 1
            ir += 1
            
        elif a_keycol[ia]>b_keycol[ib]:
            r[ir, 0] = b_keycol[ib]
            r[ir, 1] = outer_value
            r[ir, 2] = b[ib]
            ib += 1
            ir += 1

        else:
            r[ir, 0] = a_keycol[ia]
            r[ir, 1] = a[ia]
            r[ir, 2] = b[ib]
            ir += 1
            ia += 1
            ib += 1
    
    while ia<len(a):
        r[ir, 0] = a_keycol[ia]
        r[ir, 1] = a[ia]
        r[ir, 2] = outer_value
        ia += 1
        ir += 1
    
    while ib<len(b):
        r[ir, 0] = b_keycol[ib]
        r[ir, 1] = outer_value
        r[ir, 2] = b[ib]
        ib += 1
        ir += 1

    return r[:ir]
