# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 22:50:44 2023

@author: jha25
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <----format of read_csv
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')
#summary of the data
data.info() 
#playing around with variables

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11-11.73
ProfitPerItem = 21.11 * 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPriceTransaction = NumberOfItemsPurchased * SellingPricePerItem

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# Variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# adding a new column to a data frame

data['CostPerTransaction'] = CostPerTransaction

# another way for SaleperTransaction

data['SalePerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']
data['ProfitPerTransaction'] = data['SalePerTransaction'] - data['CostPerTransaction']
#MarkUP= (Sakes-Cost)/cost


data['MarkUp'] = data['ProfitPerTransaction'] / data['CostPerTransaction']
data['MarkUp'] = (data['SalePerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#Rounding MarkUp

roundmarkup = round(data['MarkUp'], 2)

data['MarkUp'] = round(data['MarkUp'], 2)

#Combining data Fields

my_name = 'Anjali' + ' ' + 'Jha'

my_date = 'Day' + '-' + 'Month' + '-' + 'Year'


#Checking columns data type
print(data['Day'].dtype)

#Change Columns Type

day = data['Day'].astype(str)
year= data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date']=my_date

#Using iloc to view specific columns/rows

data.iloc[0]  #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #Last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column

data.iloc[4,2] #brings in 4th row,2nd column

#using split to split client_keyword field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns for the split columns in Client Keywords
data['ClientAge']=split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#using lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year','Month'], axis=1)

 #Export into a CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)



















































