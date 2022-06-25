# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:09:18 2022

@author: miste
"""

import sys
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

dt = datetime.now()
print(dt)
deltaobj = timedelta(days = 100,hours = 10, minutes = 13)
#subtracts 60 seconds and adds 730 days, or two years.
dt = dt + timedelta(seconds= -60, days = 730)
print(dt)
print('type :- ',type(dt))

def my_function(datetime,delta):
    d = datetime + delta
    print(d)
    return d
my_function(dt,deltaobj)