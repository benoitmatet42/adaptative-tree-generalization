#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from time import time
from tqdm import tqdm

import datetime

class Chrono:
    def __init__(self, msg=None, verbose=True):
        self.time_start = time()
        self.verbose = verbose
        if msg:
            now = datetime.datetime.now()
            timestr = "{:02d}:{:02d}:{:02d}".format(now.hour, now.minute, now.second)
            print(str(timestr) + "\t"+ str(msg))

    def format_time(self, dt=None):
        dt = int(time() - self.time_start)
        return "{:02d}:{:02d}:{:02d}".format(dt//3600, (dt%3600)//60, dt%60)

    def tprint(self, msg):
        """deprecated, use write instead"""
        if self.verbose:
            print(self.format_time() + "\t"+ str(msg))
            
    def write(self, msg):
        if self.verbose:
            tqdm.write(self.format_time() + "\t"+ str(msg))

    def warn(self, msg):
        if self.verbose:
            print('\x1b[41m' + self.format_time() + "\t"+ str(msg) + '\x1b[0m')

    def done(self, message=None):
        self.write('Work complete !')

if __name__ == "__main__":
    from time import sleep
    c = Chrono("Beginning test...")
    sleep(0.5)
    c.tprint('waiting...')
    sleep(0.5)
    c.done()
    