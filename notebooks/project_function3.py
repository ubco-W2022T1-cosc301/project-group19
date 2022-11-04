import pandas as pd

def load_and_process(file):
    df=pd.read_csv(file)

#dropping unneeded columns
    df1=(df.copy().drop("DATA_LEVEL", axis=1)
        .drop("SUB_POPULATION", axis=1)
        .drop("PUBLIC_OR_INDEPENDENT", axis=1)
        .drop("FACILITY_TYPE", axis=1)
    )
    df2 = (
         df1
         #renaming
         .rename(columns = {"YEAR_6_OF_COHORT" : "Year"}) 
         .rename(columns = {"DISTRICT_NUMBER" : "District_Number"})
         .rename(columns = {"DISTRICT_NAME" : "District_Name"})
         .rename(columns = {"COMPLETION_RATE_MODEL" : "Completion_Rate_Model"})
         .rename(columns = {"MODEL_TYPE" : "Learning_Model"})
         .rename(columns = {"MODEL_TYPE" : "Learning_Model"}) 
         .rename(columns = {"COHORT_COUNT" : "Cohort_Number"})
         .rename(columns = {"SUCCESS_COUNT" : "Success_Rate"})
         .rename(columns = {"ESTIMATED_OUTMIGRANTS" : "Estimated_Exiting_Students"})
         .rename(columns = {"ESTIMATED_COMPLETION_RATE" : "Estimated_Successful_in_Cohort"})
    )

    
    #deleting unneeded stuff
    df2= df2[df2[ 'District_Name'].str.contains( 'NaN' )== False]
    df2 =df2[df2[ 'Success_Rate'].str.contains( 'Msk' )== False]
        

    return df2
