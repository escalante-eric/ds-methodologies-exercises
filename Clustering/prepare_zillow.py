import acquire_zillow

import pandas as pd
import numpy as np



### Dropping multiple columns that we will not use in our model, descriptions of why are in the Jupyter file
def drop_columns(df):
    return df.drop(columns=['heatingorsystemdesc', 'censustractandblock',
                     'regionidcity', 'finishedsquarefeet12',
                     'rawcensustractandblock', 'propertyzoningdesc',
                     'transactiondate',
                     'calculatedbathnbr','fullbathcnt',
                     'propertycountylandusecode', 'taxamount'])

### Our focus will be on the rows with the unit count of less than 2; we also want to look at the units that actually have a bedroom count and a calculated square feet of over 500 square feet
def drop_units(df):
    unit_one = df[(df['unitcnt'] >= 2) & (df['bedroomcnt'] >= 2) & (df['calculatedfinishedsquarefeet'] >= 500)].index 
    df = df.drop(unit_one, inplace=True)
    return df

### Run the first function that returns missing value totals by column: Does the attribute have enough information (i.e. enough non-null values) to be useful? Choose your cutoff and remove columns where there is not enough information available. Document your cutoff and your reasoning.
def replace_null_data(df, column_name, numerical = True):
    if numerical == True:
        df[column_name] = df[column_name].fillna(df[column_name].mean())
    else:
        df[column_name] = df[column_name].fillna(df[column_name].mode()[0])
    
    return df

### Write or use a previously written function to return the total missing values and the percent missing values by column.
def null_percent_col(df):
    return df.isnull().sum() / df.shape[0] * 100.00

### Write or use a previously written function to return the total missing values and the percent missing values by row.
def null_percent_row(df):
    return df.isnull().sum() / df.shape[1] * 100.00

### Write a function that will take a dataframe and list of column names as input and return the dataframe with the null values in those columns replace by 0.
def replace_with_zero(df, column_name):
    df[column_name] = df[column_name].fillna(0)
    return df

### We will prep a few functions in prepare.py; however we will use most of the functions in the Jupyter file
def prep_zillow(df):
    df = df.pipe(drop_columns).pipe(drop_units)
    return df

df = acquire_zillow.read_zillow_csv()
print(df.shape)s