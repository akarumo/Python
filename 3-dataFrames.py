# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:14:35 2018

@author: aditya
"""

import pandas as pd
print(pd.__version__)

# Kaggle: Titanic: Machine Learning from Disaster 
# read the data set downloaded from Kaggle, train.csv
titanic_train= pd.read_csv("C:\\Users\\aditya\\Documents\\0 Kaggle\\Titanic\\train.csv")

print(type(titanic_train))

# explore the data frame
titanic_train.shape # displays no. of rows, columns
titanic_train.info() # non-null objects count, data types
titanic_train.describe() # statistical 

# access data frame columns
titanic_train['Age']
# or
titanic_train.Age
# access multiple columns
temp= titanic_train[['Age','Sex']]
print(type(temp))

# access a specific row from the data frame use iloc method
titanic_train.iloc[800]
# access range of rows 
titanic_train.iloc[800:811]
# access last record using negative 1
titanic_train.iloc[-1]
# access last but one record using negative 2
titanic_train.iloc[-2]
# fetch top n records
titanic_train.head(5)
# fetch bottom n records
titanic_train.tail(5)
# access specific column use .loc method
titanic_train.loc[10:20, 'Name']
# filter records while accessing
titanic_train.loc[titanic_train.Age>65, ['Name','Age']]
# filter records using & (AND) operator
# enclose the conditions in brackets and use &
titanic_train.loc[(titanic_train.Sex=='female') & (titanic_train.Fare>250), 'Name']
# filter records using | (OR) operator
titanic_train.loc[(titanic_train.Parch>5) | (titanic_train.Fare>250 ), ['Name','Parch','Fare']]
# filter records using multiple or conditions
titanic_train.loc[(titanic_train.Cabin=='A10') | (titanic_train.Cabin=='A14') | (titanic_train.Cabin=='B82 B84')  , ['Name','Cabin']]
# instead of having multiple OR conditions, we could use isin
titanic_train.loc[titanic_train.Cabin.isin(['A14','A10','B82 B84']),['Name','Cabin']]

# TODO find rows with Name starting with Andersson
#titanic_train.loc[(titanic_train.Name.str.find('Andersson',0)), ['Name']]

# Grouping data using groupby
titanic_train.groupby('Pclass').size()
titanic_train.groupby(['Pclass','Sex']).size()
titanic_train.groupby(['Pclass','Sex','Embarked']).size()

# Group and find mean
titanic_train.groupby(['Embarked','Pclass']).mean() # returns all numeric columns
titanic_train.groupby(['Embarked','Pclass']).mean()['Fare'] # show only Fare column
# axis = 0 indicates, calculate mean on each column for all rows in this example
# axis = 1 indicates, calculate on each row for all columns
titanic_train.groupby(['Embarked','Pclass'],axis=0).mean()

# A better explanation of axis = 0 and axis = 1 below:

# =============================================================================
# +------------+---------+--------+
# |            |  A      |  B     |
# +------------+---------+---------
# |      0     | 0.626386| 1.52325|----axis=1----->
# +------------+---------+--------+
#              |         |
#              | axis=0  |
#              ↓         ↓
# =============================================================================

