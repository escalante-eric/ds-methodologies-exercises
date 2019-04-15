import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def zillow_properties_2016():
    return pd.read_sql('SELECT pro.*, pre.parcelid, pre.logerror, pre.transactiondate,                               actype.airconditioningdesc,\
                        arctype.architecturalstyledesc, bldtype.buildingclassdesc,heatype.heatingorsystemdesc, protype.propertylandusedesc, stype.storydesc, ttype.typeconstructiondesc\
                        FROM predictions_2016 pre\
                        INNER JOIN properties_2016 pro ON pre.parcelid = pro.parcelid\
                        LEFT JOIN airconditioningtype actype USING (airconditioningtypeid)\
                        LEFT JOIN architecturalstyletype arctype USING (architecturalstyletypeid)\
                        LEFT JOIN buildingclasstype bldtype USING (buildingclasstypeid)\
                        LEFT JOIN heatingorsystemtype heatype USING (heatingorsystemtypeid)\
                        LEFT JOIN propertylandusetype protype USING (propertylandusetypeid)\
                        LEFT JOIN storytype stype USING (storytypeid)\
                        LEFT JOIN typeconstructiontype ttype USING (typeconstructiontypeid)', 
    get_connection('zillow'))

def zillow_properties_2017():
    return pd.read_sql('SELECT pro.*, pre.parcelid, pre.logerror, pre.transactiondate,                              actype.airconditioningdesc,\
                        arctype.architecturalstyledesc, bldtype.buildingclassdesc,heatype.heatingorsystemdesc, protype.propertylandusedesc, stype.storydesc, ttype.typeconstructiondesc\
                        FROM predictions_2017 pre\
                        INNER JOIN properties_2017 pro ON pre.parcelid = pro.parcelid\
                        LEFT JOIN airconditioningtype actype USING (airconditioningtypeid)\
                        LEFT JOIN architecturalstyletype arctype USING (architecturalstyletypeid)\
                        LEFT JOIN buildingclasstype bldtype USING (buildingclasstypeid)\
                        LEFT JOIN heatingorsystemtype heatype USING (heatingorsystemtypeid)\
                        LEFT JOIN propertylandusetype protype USING (propertylandusetypeid)\
                        LEFT JOIN storytype stype USING (storytypeid)\
                        LEFT JOIN typeconstructiontype ttype USING (typeconstructiontypeid)', 
    get_connection('zillow'))

### Function is used to join the two created data frames together and returns a CSV of the merged dataframes
def get_zillow_csv():
    df_2016 = zillow_properties_2016()
    df_2017 = zillow_properties_2017()
    zillow = df_2016.append(df_2017, ignore_index=True)
    return zillow.to_csv(r'../Clustering/zillow_properties.csv', index=False)

### Function is to read the actual CSV so that we do not continue to build duplicated csv files
def read_zillow_csv():
    return pd.read_csv("./zillow_properties.csv", low_memory=False, index_col ='parcelid')