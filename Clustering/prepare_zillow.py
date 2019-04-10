import acquire_zillow

import pandas as pd
import numpy as np

df = acquire_zillow.read_zillow_csv()

def remove_columns(df, cols_to_remove):
    df = df.drop(columns=cols_to_remove)
    return df

def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def only_one_unit():
    unit_one = df[(df['unitcnt'] == 1) & (df['bedroomcnt'] >= 1)].index    
    return df.drop(unit_one, inplace=True)

def remove_proerty_land():
    df[df.propertylandusedesc != 'Duplex (2 Units, Any Combination)']
    df[df.propertylandusedesc != 'Quadruplex (4 Units, Any Combination)']
    df[df.propertylandusedesc != 'Triplex (3 Units, Any Combination)']
    return df

def data_prep(df, cols_to_remove=[], prop_required_column=.5, prop_required_row=.75):
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)
    df = df.dropna(axis=0, subset=['longitude'])
    return df

data_prep(df, cols_to_remove=['airconditioningtypeid', 'architecturalstyletypeid', 'buildingclasstypeid','buildingqualitytypeid', 'propertylandusetypeid', 'typeconstructiontypeid', 'storytypeid', 'heatingorsystemtypeid'])

print(df.propertylandusedesc.value_counts())

print(df.shape)

'''
### use this later in exploration.py
bycounty = df.groupby('regionidcounty')
print(bycounty['logerror'].describe())
'''