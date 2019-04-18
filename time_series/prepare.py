import pandas as pd
from datetime import timedelta, datetime
import numpy as np
from scipy import stats

import itertools

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

from acquire import get_all_data


def prep_sale_data(df: pd.DataFrame):
    '''
    Function to convert a date to adatetime data type and change a datetime to UTC; 
    It will also sort the dates and set the index as the sale date
    '''
    df['sale_date'] = pd.to_datetime(df['sale_date'], utc=True)
    
    return df

def set_date_index(df):

    return df.set_index('sale_date')

def date_breakdown(df):
    '''
    Function creates 6 additional columns: year, quarter, month, day of month, day of week, weekend vs. weekday using basic date and time types
    '''
    df['year'] = df.sale_date.dt.year
    df['quarter'] = df.sale_date.dt.quarter
    df['month'] = df.sale_date.dt.month
    df['day_of_month'] = df.sale_date.dt.day
    df['day_of_week'] = df.sale_date.dt.weekday_name
    df['weekend vs. weekday'] = df['day_of_week'] < 'Friday'

    return df

def create_columns(df):
    '''
    Feature created: 'sales_total' - creates a new feature that multiplies sale amount and item price
    Feature created: 'day_over_day' - result of current sales - the previous days sales
    Feature created: 'sale_date' - converts sale date info into the UTC timezone
    '''
    df['sales_total'] = df['sale_amount'] * df['item_price']
    df['day_over_day'] = df['sales_total'].diff()

    return df

def prep_store_data():
    '''
    Takes the aquired dataframe and preforms the above functions to create a dataframe we will 
    work with in the next step
    It uses Functions:
        1. prep_sale_data
        2. date_breakdown
        3. create_columns
    '''
    df = prep_sale_data(df)
    df = date_breakdown(df)
    df = create_columns(df)
    df = set_date_index(df)

    return df

