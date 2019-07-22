import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def date_split(string):
    '''
    extracts date from input string
    Input: String
    Output: date object
    '''
    dtobj = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return dtobj.date()

def time_split(string):
    '''
    extracts time from input string
    Input: String
    Output: date object
    '''
    dtobj = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return dtobj.time()


