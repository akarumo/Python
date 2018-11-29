# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:06:51 2018

@author: adkarumo
"""

# can't use + operand over an int and str
print(1+'a')

# prints python 4 times
print('Python '*4)

var1= 'Hello '
var2= 'World!'

# dir: inbuilt function in Python 3, returns list of attributes and methods of any object
print(dir(var1))

# help: inbuilt function to see help on an object
print(help(var1.capitalize))

# add first str and second str
var1.__add__(var2)
# look for existence of a character
var1.__contains__('o')
# length of a string
var1.__len__()

print(help(var1.join))

weekday_list= ['Mon','Tue','Wed','Thu','Fri']

', '.join(weekday_list)

var3= var1.__add__(var2)

# count occurences of a character
var3.count('l')
# find position of a character
var3.find('e')

# multiple statements in a single line separated by a semi-colon
print(var3.find('o')); print("find char 'o' completed")

# print content of multiple variables 
print(var1, var2)
print("variable1 holding data: ",var1," variable2 holding data: ",var2)
print("variable1 holding data: %s and variable2 holding data: %s" %(var1,var2))
print("variable1 holding data: {} and variable2 holding data: {}".format(var1,var2))
print("variable1 holding data: %s. And it is of length: %d" %(var1,len(var1)))




