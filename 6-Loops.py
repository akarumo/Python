# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:26:16 2018

@author: aditya
"""


# while loop
# print odd numbers in 1-10

i= 1
while(i<10) :
    print(i)
    i+=2;


# print odd numbers in 1-10 but skip printing number 7

i= 1
while(i<10) :
    if(i == 7):
        i= i+2
        continue
    else:
        print(i)
        i= i+2

# pass keyword is used when a statement is required syntactically but 
# we don't need to do anything

i=5
if(i>10):
    pass
else:
    print('i has value 5 and not greater than 10')

# print list of numbers
for i in 100,929,89,1,44,:
    print(i)
    
# print a list containing heterogenous data
for i in 120, 'adi', 2.45:
    print(i)
    
# print range of values
for i in range(8):
    print(i)
    
# range: start, stop indices and stepping value
for i in range(1,10,2):
    print(i)

# comma separated multiples of 5 within 40
for i in range(0,40,5):
    print(i, end=',')
    
# print numbers in reverse 1-10
for i in range(10,0,-1):
    print(i, end=',')

# print list of Alphabets in upper case
alphabets= "abcdefghi"

# string is an iterable object and can be used in for loop
for i in alphabets:
    print(i.upper(), end=',')


for i in "Hello!", "welcome", "to", "Python", "Programming" :
    print(i, end=' ')