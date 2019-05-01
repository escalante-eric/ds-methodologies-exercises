import acquire_mall
import pandas as pd


df_mall = acquire_mall.get_mall_customers()
df_mall.set_index('customer_id', inplace=True)

def get_upper_outliers(df, k):
    q1, q3 = df.quantile([.25, .75])
    iqr = q3 - q1
    upper_bound = q3 + k * iqr
    return df.apply(lambda x: max([x - upper_bound, 0]))

def add_upper_outlier_columns(df, k):
    for col in df.select_dtypes('number'):
        df[col + '_outliers'] = get_upper_outliers(df[col], k)
    return df

def summarize_data(df):
    print("\nSummary Stats:\n")
    print(df.describe())
    print(pd.concat([df.head(), df.tail()]))
    df.select_dtypes('number').head()
    for col in df.select_dtypes('number'):
        print(col)
        print(df[col].value_counts(bins=4))
    print(df.isna().sum())


### Use function to find outliers
add_upper_outlier_columns(df_mall, k=1.5)

### Encodes all the categorical columns, and adds the encoded column (i.e. it doesn't remove the original column)
dummy = pd.get_dummies(df_mall['gender'])
df = pd.concat([df_mall, dummy], axis=1)
print(df.head())

### Uses function to give summary of dataframe
# print(summarize_data(df))


