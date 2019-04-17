import pandas as pd

df = pd.read_csv('http://python.zach.lol/access.log',
              sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
              engine='python',
              usecols=[0, 3, 4, 5, 6, 8],
              names=['ip', 'time', 'request', 'status', 'size', 'request_agent'],
              na_values='-',
              header=None,
              index_col=False)

print(df)