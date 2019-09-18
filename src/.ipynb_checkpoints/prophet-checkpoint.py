import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from fbprophet import Prophet
import logging
from sklearn.cluster import DBSCAN
from sklearn.metrics import mean_squared_error

def make_comparison_dataframe(historical, forecast):
    '''
    join the history with the forecast.
    the resulting dataset will contain columns 'yhat', 'yhat_lower', 'yhat_upper', and 'y'.
    '''
    return forecast.set_index('ds')[['yhat','yhat_lower','yhat_upper']].join(historical.set_index('ds'))


def calculate_forecast_errors(df, prediction_size):
    '''Calculate MAPE and MAE of the forecast
    Input: df: joined dataset with 'y' and 'yhat' columns
    prediction_size: # days at the end to predict
    '''
    # make a copy
    df = df.copy()
    
    # calculate valuess of e_i and p_i according to the formulas
    df['e'] = df['y'] - df['yhat']
    df['p'] = 100 * df['e'] / df['y']
    
    # cut out prediction data
    predicted_part = df[-prediction_size:]
    
    # define function that averages absolute error values over predicted part
    error_mean = lambda error_name: np.mean(np.abs(predicted_part[error_name]))
    
    # calculate MAPE and MAE and return the resulting dictionary of errors
    return {'MAPE': error_mean('p'), 'MAE': error_mean('e')}

def RMSE(df, prediction_size):
    '''Calculate RMSE of the forecast and train set
    Input: df: joined dataset with 'y' and 'yhat' columns
    prediction_size: # days at the end to predict
    '''
    train='Train RMSE '+ str(np.sqrt(mean_squared_error(df[:-prediction_size]['y'], df[:-prediction_size]['yhat'])))
    test='Test RMSE '+ str(np.sqrt(mean_squared_error(df[-prediction_size:]['y'], df[-prediction_size:]['yhat'])))
    
    return train, test
    
    