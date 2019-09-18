import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
from pywaffle import Waffle

def date_split(string):
    '''
    extracts date from input string
    Input: String
    Output: date object
    '''
    dtobj = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return dtobj.date()

def time_split(string):
    '''
    extracts time from input string
    Input: String
    Output: date object
    '''
    dtobj = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return dtobj.time()


def dailyagg(df):
    '''
    Description: Aggregate df by day and prepare for Time Series analysis and Prophet
    Input: Pandas DataFrame
    Output: df aggregated by date
    '''
    df = df.set_index(pd.DatetimeIndex(df['date']))
    df = pd.DataFrame(df.resample('D').count())
    df = df.drop(['date'], axis=1)
    df.reset_index(inplace=True)
    df = df[['date', 'INCIDENT_NUMBER']]
    df.columns = ['ds', 'y']
    return df


def weeklyagg(df):
    '''
    Description: Aggregate df by week and prepare for Time Series analysis and Prophet
    Input: Pandas DataFrame
    Output: df aggregated by date
    '''
    df = df.set_index(pd.DatetimeIndex(df['date']))
    df = pd.DataFrame(df.resample('W').count())
    df = df.drop(['date'], axis=1)
    df.reset_index(inplace=True)
    df = df[['date', 'INCIDENT_NUMBER']]
    df.columns = ['ds', 'y']
    return df


def monthlyagg(df):
    '''
    Description: Aggregate df by month and prepare for Time Series analysis and Prophet
    Input: Pandas DataFrame
    Output: df aggregated by date
    '''
    df = df.set_index(pd.DatetimeIndex(df['date']))
    df = pd.DataFrame(df.resample('M').count())
    df = df.drop(['date'], axis=1)
    df.reset_index(inplace=True)
    df = df[['date', 'INCIDENT_NUMBER']]
    df.columns = ['ds', 'y']
    return df