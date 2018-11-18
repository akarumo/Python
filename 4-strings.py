# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:18:19 2018

@author: aditya
"""

name = 'Aditya K'
print(type(name))
print('Name: ',name)
print('First character: ', name[0])
print('Nickname:',name[0:3])

# Modify string content
name[0]= 'U'
# modification is not allowed as Strings are immutable

# String concatenation
print(name+'arumori')
# upper case
print(name.upper())

# check instance of
isinstance(name, int)
isinstance(name, str)

