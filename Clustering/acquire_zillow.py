import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def zillow_properties_2016():
    return pd.read_sql('SELECT *\
                        FROM predictions_2016 pre\
                        INNER JOIN properties_2016 pro ON pre.parcelid = pro.parcelid\
                        LEFT JOIN airconditioningtype USING (airconditioningtypeid)\
                        LEFT JOIN architecturalstyletype USING (architecturalstyletypeid)\
                        LEFT JOIN buildingclasstype USING (buildingclasstypeid)\
                        LEFT JOIN heatingorsystemtype USING (heatingorsystemtypeid)\
                        LEFT JOIN propertylandusetype USING (propertylandusetypeid)\
                        LEFT JOIN storytype USING (storytypeid)\
                        LEFT JOIN typeconstructiontype USING (typeconstructiontypeid)', 
    get_connection('zillow'))

def zillow_properties_2017():
    return pd.read_sql('SELECT *\
                        FROM predictions_2017 pre\
                        INNER JOIN properties_2017 pro ON pre.parcelid = pro.parcelid\
                        LEFT JOIN airconditioningtype USING (airconditioningtypeid)\
                        LEFT JOIN architecturalstyletype USING (architecturalstyletypeid)\
                        LEFT JOIN buildingclasstype USING (buildingclasstypeid)\
                        LEFT JOIN heatingorsystemtype USING (heatingorsystemtypeid)\
                        LEFT JOIN propertylandusetype USING (propertylandusetypeid)\
                        LEFT JOIN storytype USING (storytypeid)\
                        LEFT JOIN typeconstructiontype USING (typeconstructiontypeid)', 
    get_connection('zillow'))

df_2016 = zillow_properties_2016()

