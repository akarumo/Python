# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:32:49 2018

@author: aditya
"""

#understanding basic types int, float, str, bool
#types are inferred by runtime automatically


a = 10
print(type(a))
# python 3 has no size limits on int data type
a1= 10000000000000000000000000000000000000000000000000000000000000000000000000
print(type(a1))

b = 13.6
print(type(b))

# strings can be delimited using single quote or double quotes
c = 'abc'
print(type(c))
c1= "abc"
print(type(c1))
# escaping special characters in a string using \
c2= 'this contains a special character - \''
print(c2)
# to breakup string over more than one line use \
c3= ' first line \
    second line \
    third line \
    fourth line \
    '
print(c3)
# we could also do the above thing by using triple quotes
c4= """ This line spans across
multiple lines
and is delimited
by triple quotes"""
print(c4)
# to introduce newline in a string use \newline
c5= ' first line \n \
second line \n '
print(c5)


d = False 
print(type(d))

# read input from console
e= input("Enter something:")
print(type(e))

