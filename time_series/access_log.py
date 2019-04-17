import pandas as pd

df = pd.read_csv('http://python.zach.lol/access.log',          
              engine='python',
              header=None,
              index_col=False,
              names=['ip', 'timestamp', 'request_method', 'status', 'size', 'unknown', 'request_agent'],
              na_values='-',
              sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
              usecols=[0, 3, 4, 5, 6, 7, 8])

print(df.tail(5))