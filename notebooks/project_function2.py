import pandas as pd

def load_and_process(file):
    myData = pd.read_csv(file)
    
#Drop unneeded columns
    df1 = (myData.copy().drop("PUBLIC_OR_INDEPENDENT", axis = 1)
        .drop("DISTRICT_NUMBER", axis = 1)
        .drop("FACILITY_TYPE", axis = 1)
        .drop("MODEL_TYPE", axis = 1)
        .drop("COHORT_COUNT", axis = 1)
        .drop("SUCCESS_COUNT", axis = 1)
        .drop("ESTIMATED_OUTMIGRANTS", axis = 1)
        .drop("DATA_LEVEL", axis = 1)
        .drop("SUB_POPULATION", axis = 1)
        .drop("COMPLETION_RATE_MODEL", axis = 1)
    )
    df2 = (
        df1
#Rename columns
        .rename(columns = {"DISTRICT_NAME" : "School District"})
        .rename(columns =  {"YEAR_6_OF_COHORT" : "Year"})
        .rename(columns =  {"ESTIMATED_COMPLETION_RATE" : "Estimated Completion Rate"})
 
#Sort values    
        #.sort_values(by=["DISTRICT_NAME"], ascending=True)
           
    )
#Delete unneeded values
    df2 = df2[df2['DATA_LEVEL'].str.contains('DISTRICT LEVEL')==True]
    df2 = df2[df2['SUB_POPULATION'].str.contains('ALL STUDENTS')==True]
    df2 = df2[df2['DISTRICT_NAME'].str.contains('NaN')==False]
    df2 = df2[df2['COMPLETION_RATE_MODEL'].str.contains('SIX YEAR DOGWOOD COMPLETION RATE')==True]
    df2 = df2[df2['ESTIMATED_COMPLETION_RATE'].str.contains('Msk')==False]

#Shorten year column   
    df2 = df2["Year"].str.slice(0,-5) 

#Change year column to int
    df2 = df2["Year"].astype(int)         

    return df2 