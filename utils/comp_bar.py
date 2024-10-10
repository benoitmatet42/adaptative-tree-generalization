#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def comp_bar(ax, bars, colors=None, bar_labels=None, width=0.2, normalize=False, labels=True):
    nbars = len(bars)
    ibar = 0
    if colors is None:
        colors=[None]*len(bars)
    if bar_labels is None:
        bar_labels = np.arange(len(bars))
        
    for i, bar in enumerate(bars):
        if normalize:
            bar = bar/bar.sum()
        barplot = ax.bar(np.arange(len(bar))-(nbars-1)*width/2 + width*ibar, 
                      bar, 
                      width=width, label=bar_labels[i], color=colors[i])
        if labels:
            ax.bar_label(barplot, fmt='%.2g')
        ibar+=1
    
    ax.legend()
    ax.spines.top.set_visible(False)
    ax.spines.right.set_visible(False)
    