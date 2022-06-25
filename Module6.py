# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:46:44 2022

@author: miste
"""


import sys
from datetime import datetime
#from datetime import time
#from datetime import date
from datetime import timedelta

#creating an object representing 100 days, 10 hours, 13 minutes
deltaobj = timedelta(days =100,hours = 10,minutes = 13)
def main():
    dt = datetime.now()
    #utc = datetime.utcnow()
    time_string = dt.strftime("%X")
    date_string = dt.strftime("%x")

    """https://strftime.org"""
    #add the timedelta to the datetime and subtract 60 second and added 2 year
    #subtract 60 seconds represented as -60, add 2 years represented as 730 days.
    dtdelta = dt + timedelta(seconds= -60, days = 730)
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            _date, _time, store, item, cost, payment = data
            print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(date_string,time_string,store,item,cost,payment))
    
main()