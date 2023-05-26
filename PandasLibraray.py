#Import all libiraries 👇👇
import pandas as pd
import numpy as np
import random as ran
 #Dictonary 👇👇
dict1 = {
    "Name":["Aqeel","Ali","Arooba","Amna"],
    "Marks":[92,45,67,89],
    "City" :["Faisalabad","Lahore","Karachi","Islamabad"]
}

#Making Data Frame of Dictionary 👇👇
df = pd.DataFrame(dict1) #Data Frame -->Two Dimensional Array -->Tabular Spread Sheets Like structre which contain Row and Column
#print(df)

# df.to_csv("Data.csv") # 👈👈 Make Excel Sheets with index
# df.to_csv("Data_Index.csv",index=False) # 👈👈Make Excel Sheets with out index

# print(df.head(2))    #  👈👈 Show Start Some Rows
# print(df.tail(2))    # 👈👈  Show Last Some  Rows
# print(df.describe()) # 👈👈 Perfrom Some Mathematical Operation on data frame which is follow as 👉👉 count,mean,std,min,25%,50%,75%,max
Aqeel = pd.read_csv('Aqeel.csv')
# print(Aqeel)
# Aqeel['Speed'][0] = 50  # 👈👈 Change Value on single index
# print(Aqeel['Speed'])   # 👈👈 Display Single Column
#Aqeel.to_csv('Aqeel.csv')# 👈👈 Make Excel Sheets

ser = pd.Series(np.random.rand(35)) # 👈👈 Make Series --> One Dimensional Array with index. it store a single row or column in data frame
#print(ser)
# print(type(ser)) # 👈👈 Check Type of serires

dataFrame = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))

#print(dataFrame.head())        #  👈👈 Show Start Some Rows
# print(dataFrame.tail())       #  👈👈 Show Start Some Rows
# print(type(dataFrame))        # 👈👈 Check Type of data frame
#print(dataFrame.describe())    # 👈👈 Perfrom Some Mathematical Operation on data frame which is follow as 👉👉 count,mean,std,min,25%,50%,75%,max
#print(dataFrame.index)         # 👈👈 In the form of Row 
#print(dataFrame.columns)       # 👈👈 In the form of Col
#print(dataFrame)
# print(dataFrame.to_numpy())   # 👈👈 Convert To Numpy Array
#print(dataFrame.T)             # 👈👈 Tarnspose
#print(dataFrame.sort_index(axis= 0,ascending=False)) # 👈👈 Axis = 0 == Row
#print(dataFrame.sort_index(axis= 1,ascending=False)) # 👈👈 Axis = 1 == Col
dataFrame.columns = list("ABCDE")     # 👈👈Convert the column name from NUMBER  TO ALPHABETS
#print(dataFrame)
#print(dataFrame.loc[[1,2],['C','D']])# 👈👈 Specific Column Display
#Importnat Note 👇👇👇
    #1)Loc 👉👉 Work on column name and row name
    #2)Iloc 👉👉 Work on Column Index and Row Index 
# print(dataFrame.iloc[1,4])         # 👈👈 Specific Value on the two dimensional element
# print(dataFrame.iloc[[0,1],[1,2]]) # 👈👈 Specific Column
# print(dataFrame)
# print(dataFrame.drop([0,3],inplace=True))     # 👈👈 using inplace delete permanentaly and make change in same data frame directly #  By default axis = 0 # For Delete the row
# dataFrame.reset_index(drop=True,inplace=True) # 👈👈 Reset the index after delete some data permanentaly
# print(dataFrame)
#print(dataFrame[3].isnull())   # 👈👈 When column have some value show false(not null)
#dataFrame.loc[:,[3]] = None    # 👈👈Set the value ny using loc #All value in column 3 make none
#print(dataFrame[3].isnull())   # 👈👈When column have not value show true(null)
# print(dataFrame)
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Alfred'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
#print(df.dropna())               # 👈👈 Drop the rows where at least one element is missing.
#print(df.dropna(how="all"))      # 👈👈 Drop the rows where all elements are missing.
#print(df.dropna(axis='columns')) # 👈👈 Drop the columns where at least one element is missing.
# print(df.drop_duplicates())     # 👈👈 Remove Duplicate items
# print(df.drop_duplicates(subset=['name'],keep='first')) # 👈👈 To remove duplicates and keep by default first occurrences #By default, it removes duplicate rows based on all columns.
# print(df.drop_duplicates(subset=['name'],keep='last'))  # 👈👈 To remove duplicates and keep last occurrences
# print(df.drop_duplicates(subset=['name'],keep= False))  # 👈👈 Drop all duplicates.
# print(df.shape)   # 👈👈 Shape
# print(df.info())  # 👈👈 info about DataFrame
# print(df['name'].value_counts())              # 👈👈 Give Count Of unique Value
#print(df['toy'].value_counts(dropna=False))    # 👈👈 Give Count Of unique Value and show dropna value
# print(df['born'].value_counts(dropna=False))  # 👈👈 Give Count Of unique Value and show dropna value
# print(df.notnull()) # we use also isnull      # 👈👈 Check Null Or Not