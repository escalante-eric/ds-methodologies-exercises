### 5. Create a file named acquire.py
## This file should define at least two functions

    # get_titanic_data: returns the titanic data from the codeup data science database as a pandas data frame
    # get_iris_data: returns the data from the iris_db on the codeup data science database as a pandas data frame. The returned data frame should include the actual name of the species in addition to the species_ids

    # We will use these functions in later exercises

import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

df_titanic = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
df_iris = pd.read_sql('SELECT * FROM species JOIN measurements USING (species_id)', get_connection('iris_db'))

print(df_titanic.head())
print(df_iris.head())