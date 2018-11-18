# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:10:50 2018

@author: aditya
"""

import pandas as pd

col1 = [1,2,3,4,5]
col2 = ['Aditya','John','Amy','Joe','Ria']
col3 = ['30k','50k','30k',None,'15k']

# create a data frame from a python dictionary
df= pd.DataFrame({'eid' : col1,'ename' : col2,'salary' : col3})

df.shape
df.info()
df.describe()

# add another column with all zeros
df['col4']= 0
# print the data frame
print(df)

# access columns in the data frame
df.ename
df['salary']
df[['ename','salary']]
# dropping column is inplace and doesn't effect the original unless overwritten
df=df.drop('col4',1)
df

# add a new column Gender
df['gender'] = ['m','m','f','m','f']
df

#slicing rows
df[0:2]
df[2:]
df[:3]

# filtering rows by condition; the condition evaluates to pandas Series
type(df.eid>2)
# print the Series
df.eid>2
# apply condition to data frame
df[df.eid>2]

# select specific rows and columns
# select first two rows
df.iloc[0:2,]
# select only first and third rows
df.iloc[[0,2],]
# select only first and third rows and second column
df.iloc[[0,2],1]
# select only first and third rows and second and fourth columns
df.iloc[[0,2],[1,3]]
# using .loc access four rows and only ename column
df.loc[0:3, ['ename']]
