#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import warnings
import numpy as np

mode_dict_emo = {np.nan:'',
        0:'👣',
         1:'🚲',
         2:'🚗',
         3:'🚌'
        }

motif_dict_emo = {np.nan:'',
          0:'🏠',
         1:'🏭',
         2:'📚',
         3:'🛍️',
         4:'🍻'}

def agenda_display(df, size=10):
    mode_dict = {np.nan:'',
            0:'👣',
             1:'🚲',
             2:'🚗',
             3:'🚌'
            }

    motif_dict = {np.nan:'',
              0:'🏠',
             1:'🏭',
             2:'📚',
             3:'🛍️',
             4:'🍻'}

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        viz = df.copy()
        for col in viz.columns:
            if 'mode' in col:
                viz[col] = viz[col].replace(mode_dict)
            elif 'motif' in col:
                viz[col] = viz[col].replace(motif_dict)
            elif 'time' in col:
                viz[col] = (viz[col].astype(str) + 'h').replace({'nanh':''}).str.replace('\.0','')
                
            
        def custom_styles(val):
            styles=[]
            if val.name.endswith('mode') or val.name.endswith('motif'):
                styles = ['font-size: {}pt'.format(size)] * len(val)
            else:
                styles = ['font-size: 10pt'] * len(val)
        
            return styles
    
        display(viz.style.apply(custom_styles))