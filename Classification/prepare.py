### Data Preparation
## Do your work for this exercise in a file named prepare.

### 1. Iris Data
    # Use the function defined in acquire.py to load the iris data.

import acquire

df_iris = acquire.get_iris_data()

# Drop the species_id and measurement_id columns.
df_iris.drop(columns=['species_id', 'measurement_id'], inplace=True)

# Rename the species_name column to just species.
df_iris.rename(columns={'species_name' : 'species'}, inplace=True)

# Encode the species name using a sklearn label encoder. Research the inverse_transform method of the label encoder. How might this be useful?
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
encoder.fit(df_iris.species)
df_iris.species = encoder.transform(df_iris.species)

encoder.inverse_transform(df_iris.species)

# Create a function named prep_iris that accepts the untransformed iris data, and returns the data with the transformations above applied.
def drop_columns(df):
    return df.drop(columns=['species_id','measurement_id'])

def rename_column(df):
    return df.rename(columns={'species_name' : 'species'})

def encode_species(df):
    encoder = LabelEncoder()
    encoder.fit(df.species)
    return df.assign(species=encoder.transform(df.species))

def prep_iris(df):
    return df.pipe(drop_columns)\
        .pipe(rename_column)\
        .pipe(encode_species)

from acquire import get_iris_data
prep_iris(get_iris_data())

### 2. Titanic Data
    # Use the function you defined in acquire.py to load the titanic data set.
    # Write the code to perform the operations below. (Do this yourself, don't copy from the curriculum.)
df_titanic = acquire.get_titanic_data()

# Handle the missing values in the embark_town and embarked columns.
df_titanic.embark_town.value_counts(dropna=False)
df_titanic.embark_town.fillna('Not Located').value_counts()

# Remove the deck column.
df_titanic.drop(columns='deck', inplace=True)

# Use a label encoder to transform the embarked column.
df_titanic.embarked.value_counts(dropna=False)
df_titanic.embarked.fillna('O', inplace=True)

encoder.fit(df_titanic.embarked)
df_titanic.embarked = encoder.transform(df_titanic.embarked)

# Scale the age and fare columns using a min max scaler. Why might this be beneficial? When might you not want to do this?
from sklearn.model_selection import train_test_split

train, test = train_test_split(df_titanic)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(train[['fare', 'age']])

train[['fare', 'age']] = scaler.transform(train[['fare', 'age']])
test[['fare', 'age']] = scaler.transform(test[['fare', 'age']])

# Create a function named prep_titanic that accepts the untransformed titanic data, and returns the data with the transformations above applied.
def handle_missing_values(df):
    return df.assign(
        embark_town=df.embark_town.fillna('Other'),
        embarked=df.embarked.fillna('O')
    )

def drop_columns(df):
    return df.drop(columns='deck')

def encode_embarked(df):
    encoder = LabelEncoder()
    encoder.fit(df.embarked)
    return df.assign(embarked=encoder.transform(df.embarked))

def prep_titanic_data(df):
    return df.pipe(handle_missing_values)\
        .pipe(drop_columns)\
        .pipe(encode_embarked)

#Save your prep_titanic and prep_iris functions in a file named prepare.py so that we can use them later on.

