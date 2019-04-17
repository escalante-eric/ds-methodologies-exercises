import pandas as pd
import numpy as np

from functools import reduce
from datetime import datetime

import itertools
import requests
import json

def get_items():
    base_url = 'https://python.zach.lol'
    response = requests.get(base_url + '/api/v1/items')
    data = response.json()
    items = data['payload']['items']

    while data['payload']['page'] <= data['payload']['max_page']:
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        items += data['payload']['items']
        if data['payload']['next_page'] == None:
            break
    df = pd.DataFrame(items)
    df.to_csv('items.csv', index=False)
    
    return df

def get_stores():
    base_url = 'https://python.zach.lol'
    response = requests.get(base_url + '/api/v1/stores').json()
    df = pd.DataFrame(response['payload']['stores'])
    df.to_csv('stores.csv', index=False)

    return df

def get_sales():
    base_url = 'https://python.zach.lol'
    response = requests.get(base_url + '/api/v1/sales')
    data = response.json()
    sales = data['payload']['sales']

    while data['payload']['page'] <= data['payload']['max_page']:
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        sales += data['payload']['sales']
        if data['payload']['next_page'] == None:
            break
    df = pd.DataFrame(sales)
    df.to_csv('sales.csv', index=False)

    return df

def get_all_data():
    sales = get_sales()
    stores = get_stores()
    items = get_items()

    sales.rename(columns={'store': 'store_id', 'item': 'item_id'}, inplace=True)
    df = pd.merge(sales, items, on='item_id')
    df = pd.merge(df, stores, on='store_id')

    return df