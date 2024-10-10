#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def redistribute_hourly(hours, vols):
    """
    makes 24 points per day out of the temporal agg
    """
    nb_days = int(np.ceil(hours[-1]/24))
    deltas = [int(hours[i+1])-int(hours[i]) for i in range(len(hours)-1)]+[nb_days*24 - hours[-1]]
    vols_redistributed = []
    for i, d in enumerate(deltas):
        vols_redistributed += [vols[i]/d]*d
    return np.array(range(hours[0], nb_days*24)), np.array(vols_redistributed)
