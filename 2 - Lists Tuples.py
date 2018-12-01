# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:14:46 2018

@author: aditya
"""

# to create a list, enclose elements within square brackets
list1 = [1,2,3]
print(list1)
print(type(list1))

# we can unpack a list by specifying variables equal to number of elements in list
a, b, c = list1
print(a, b, c)

# lists can hold heterogenous data
# accessing elements from a list
list2= [1,'two', 3.0, True]
# access first element by index zero
print(list2[0])
# check list's length
print(len(list2))
# access last element in the list of 4 elements by index 3
print(list2[3]) 
# Use negative indexing to traverse from right side
print(list2[-1])
print(list2[-4])
# we can slice a list by using : operator
print(list2[0:4]) # this fetches items in the list: start and end-1 indices
list3= ['Python','R','Java','Ruby','C','C++','C#']
# add an element
list3.append('PHP')
print(list3)
list3Copy= list()
# delete an element at index
del list3[7]
print(list3)
# pop removes last element
list3Copy.append(list3.pop())
print(list3)
# pop an element at an index
list3Copy.append(list3.pop(2))
print(list3, list3Copy)
# concatenate two lists
list3= list3+ list3Copy
print(list3)
# extend a list by adding another list
list4 = ['PHP','Swift']
list3.extend(list4)
print(list3)


# ------- TUPLES --------------------

# Unlike list, tuple is immutable
# to create a tuple, enclose elements within parenthesis
tuple1 = (1,2,3)
print(tuple1)
print(type(tuple1))
# deleting an element in tuple is not allowed. Will throw an error
del tuple1[1]

# ------ SETS ----------------------

# Set arranges the elements in ascending order, removes duplicates
# Sets use curly braces
set1= {7,4,1,1,9,2,2}
print(set1)

# Sets do not support indexing and also cannot be sliced
# to remove an item from the set, use discard and specify which item
set1.discard(9)
print(set1)
#discard ignores the existence of the item to be removed
set1.discard(9)
# remove throws an error to remove a non-existing item
set1.remove(9)
set1.remove(2)
print(set1)

# ----- DICTIONARIES ----------------

# Dictionary is a set of key-value pairs within curly braces
dict1= {'One': 1, 'Two': 2, "Three": 3}
print(type(dict1))
# access a dictionary element by key
print(dict1['Three'])
# access a non-existent key by square brackets throws error
print(dict1['Four'])
# a key can be accessed using get method
print(dict1.get('Three'))
# access a key that is non-existent using get method will not throw error
# instead will return None which indicates a 
print(dict1.get('Four'))

# create a dictionary that holds squares of numbers that are keys
dictSquares= {x:x*x for x in range(10)}
print(dictSquares)

# delete a specific element in dictionary
del dictSquares[1]
print(dictSquares)
# delete entire dictionary
del dictSquares
print(dictSquares)

