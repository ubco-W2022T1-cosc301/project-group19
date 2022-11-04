import pandas as pd

def dataStripping (dataFrame, column = [], value=[], boolean=True):
    """
    Removes the directed item & returns the newly cleaned df
    Input:
        - dataFrame = the pandas dataframe you need cleaned
        - column = The pandas df column key or many
        - value = The value you want removed or many
        - boolean = True = you want this item only, False = remove it 
    Output: 
        - The newly cleaned pandas Dataframe
    """
    try:
        for i,j in zip(column,value): 
            dataFrame = dataFrame[dataFrame['{}'.format(i)].str.contains('{}'.format(j)) == boolean]

        return dataFrame
    except:
        print("Error! Something is wrong in dataStripping")
        
        
def load_and_process(file):
    data_raw = pd.read_csv(file)
    cleanData = (data_raw.copy()
                 .drop(['FACILITY_TYPE','MODEL_TYPE',"COHORT_COUNT","ESTIMATED_OUTMIGRANTS"],axis=1)
                 .rename(columns={'YEAR_6_OF_COHORT':'YEAR'})
                 .rename(columns={"SUB_POPULATION":"Type of Student"})
                )
    #Fixing the data inside the df to have proper names
    cleanData['Type of Student'] = cleanData['Type of Student'].str.replace('SPECIAL NEEDS','STUDENTS WITH DISABILITIES')
    cleanData['Type of Student'] = cleanData['Type of Student'].str.replace('NON STUDENTS WITH DISABILITIES','STUDENTS WITHOUT DISABILITIES')
    
    #removing msk data
    cleanData = cleanData[cleanData['ESTIMATED_COMPLETION_RATE'].str.contains('Msk') == False]
    #Turning rate into a float from string
    cleanData['ESTIMATED_COMPLETION_RATE'] = cleanData['ESTIMATED_COMPLETION_RATE'].astype(float)
    cleanData = cleanData[cleanData['ESTIMATED_COMPLETION_RATE']>=0]

    #Shortening year from 1997/1998 -> 1997 only
    cleanData['YEAR'] = cleanData['YEAR'].str.slice(0,-5)

    return cleanData
