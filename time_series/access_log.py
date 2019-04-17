import pandas as pd
from datetime import datetime

df = pd.read_csv('http://python.zach.lol/access.log',          
              engine='python',
              header=None,
              index_col=False,
              names=['ip', 'timestamp', 'request_method', 'status', 'size', 'request_agent'],
              sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
              na_values='-',
              usecols=[0, 3, 4, 5, 6, 8])

df.timestamp = df.timestamp.str.replace('[', '')
df.timestamp = df.timestamp.str.replace(']', '')
df.timestamp= pd.to_datetime(df.timestamp.str.replace(':', ' ', 1)) 

df.request_method = df.request_method.str.replace('"', '')

df = df.set_index('timestamp')
df = df.tz_localize('utc').tz_convert('America/Chicago')

print(df.head())