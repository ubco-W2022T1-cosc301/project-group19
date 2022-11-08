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
        .rename(columns = {"DISTRICT_NAME":"School District"})
        .rename(columns = {"YEAR_6_OF_COHORT":"Year"})
        .rename(columns = {"ESTIMATED_COMPLETION_RATE":"Estimated Completion Rate"})
        .sort_values(by=["School District"], ascending=True)
    )
#Rename columns
#Sort values    
        #.sort_values(by=["DISTRICT_NAME"], ascending=True)
           
#Delete unneeded values
    df1 = df1[df1['School District'].str.contains('NaN')==False]
    df1 = df1[df1['Estimated Completion Rate'].str.contains('Msk')==False]

#Shorten year column   
    df1['Year'] = df1["Year"].str.slice(0,-5) 

#Change year column to int
    df1['Year'] = df1["Year"].astype(int)         

    return df1 