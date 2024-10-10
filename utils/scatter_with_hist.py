#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def scatter_with_hist(ax, X, Y, title='', alpha = 0.5, 
                marker_size = 50, outpath=None, scale='linear', color=None, hist_color=None):
    
    fig = plt.gcf()
    axbbox = np.array(ax.get_position())

    left = axbbox[0,0]
    bottom = axbbox[0,1]
    width = (axbbox[1,0]-axbbox[0,0])*0.9
    height = (axbbox[1,1]-axbbox[0,1])*0.9
    
    ax.set_position([left, bottom, width, height])
    
    ax.set_axisbelow(True)
    
    rect_histx = [left, bottom + height, width, 0.1]
    ax_histx = fig.add_axes(rect_histx, sharex=ax)
    ax_histx.axis('off')
    
    rect_histy = [left + width, bottom, 0.1, height]
    ax_histy = fig.add_axes(rect_histy, sharey=ax)
    ax_histy.axis('off')

    ax.scatter(X, Y, s=marker_size, alpha=alpha, color=color)

    ax_histx.set_title(title)
    
    ax.set_xscale(scale)
    ax.set_yscale(scale)
    
    if hist_color is None and (not color is None):
        hist_color=color
    
    if scale == 'log':
        ax_histx.hist(X, bins=np.geomspace(X.min(), X.max(),50), color=hist_color)
        ax_histy.hist(Y, bins=np.geomspace(Y.min(), Y.max(),50), orientation='horizontal', color=hist_color)

    else:
        ax_histx.hist(X, bins=50, color=hist_color)
        ax_histy.hist(Y, bins=50, orientation='horizontal', color=hist_color)
