import pandas as pd

df = pd.read_csv('http://python.zach.lol/access.log',
              sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
              engine='python',
              usecols=[0, 3, 4, 5, 6, 7, 8],
              names=['ip', 'timestamp', 'request_method', 'status', 'size', 'unknown', 'request_agent'],
              na_values='-',
              header=None,
              index_col=False)

print(df.tail(5))