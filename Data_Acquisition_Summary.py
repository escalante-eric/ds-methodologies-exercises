
### Methodologies Exercises ###

## 1. Use the pydataset module to load the iris data set into a dataframe, df_iris
    # print the first 3 rows
    # print the number of rows and columns (shape)
    # print the column names
    # print the data type of each column
    # print the summary statistics for each of the numeric variables. Would you recommend rescaling the data based on these statistics?

import pandas as pd

from pydataset import data

### Function to print unique values; does not return a dataframe ###
def print_unique(df):
    print('\nUnique Values\n')
    col_names = df.columns.values
    for col in col_names:
        print(f'{col}: {pd.Series(df[col].value_counts().index.values).unique()[:5]}')

df_iris = data('iris')
print('\nFirst 3 rows: \n{}'.format(df_iris.head(3)))
print('\nNumber of Rows, Columns: \n{}'.format(df_iris.shape))
print('\nColumn Names: \n{}'.format(df_iris.columns))
print('\nData Type of each Column: \n{}'.format(df_iris.dtypes))
print('\nSummary Statistics: \n{}'.format(df_iris.describe()))

## 2. Read the data tab from the stats module dataset, Excel_Stats.xlsx, into a dataframe, df_excel
    # assign the first 100 rows to a new dataframe, df_excel_sample
    # print the number of rows of your original dataframe
    # print the first 5 column names
    # print the column names that have a data type of object
    # compute the range for each of the numeric variables.

pd.read_excel('Excel_Stats.xlsx', sheet_name='Data',nrows=100)
df_excelsheet = pd.read_excel('Excel_Stats.xlsx', sheet_name='Data',nrows=100)
print('\nNumber of rows in dataframe: {}'.format(df_excelsheet.shape[0]))
print('\nFirst Five Column Names: \n{}'.format(df_iris.columns[:5]))
df_excelsheet.select_dtypes(include=['object']).columns
df[df.select_dtypes('number').columns].apply(lambda s: s.max() - s.min())

## 3. Read train.csv from google drive (shared through classroom in topic 'Classification') into a dataframe labeled df_google
    # print the first 3 rows
    # print the number of rows and columns
    # print the column names
    # print the data type of each column
    # print the summary statistics for each of the numeric variables
    # print the unique values for each of your categorical variables
    
sheet_url = 'https://docs.google.com/spreadsheets/d/1Uhtml8KY19LILuZsrDtlsHHDC9wuDGUSe8LTEwvdI5g/edit#gid=341089357'    

csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df_googlesheet = pd.read_csv(csv_export_url)
print('\nFirst 3 rows: \n{}'.format(df_googlesheet.head(3)))
print('\nNumber of Rows, Columns: \n{}'.format(df_googlesheet.shape))
print('\nColumn Names: \n{}'.format(df_googlesheet.columns))
print('\nData Type of each Column: \n{}'.format(df_googlesheet.dtypes))
print('\nSummary Statistics: \n{}'.format(df_googlesheet.describe()))
print_unique(df_googlesheet) 

## 4. In mysql workbench or a terminal, write a query to select all the columns of the passengers table from the titanic database. Export that table to a csv you store locally. Read that csv into a dataframe df_csv.
   #  print the head and tail of your new dataframe
    # print the number of rows and columns
    # print the column names
    # print the data type of each column
    # print the summary statistics for each numeric variable
    # print the unique values for each categorical variables. If there are more than 5 distinct values, print the top 5 in terms of prevelence or frequency.

import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

print ('the head and tail of df: {}'.format(df.head().append(df.tail())))
print('\nNumber of Rows, Columns: \n{}'.format(df.shape))
print('\nSummary Statistics: \n{}'.format(df.describe()))
print('\nColumn Names: \n{}'.format(df.columns))
print('\nData Type of each Column: \n{}'.format(df.dtypes))
print_unique(df) 




    