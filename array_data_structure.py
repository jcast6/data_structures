''''
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

from array import *

arr1 = array('i', [10, 20, 30, 40])

for x in arr1:
    print(x)

print('\naccessing array element: ')
print(arr1[0])
print(arr1[2])

print('\ninsertion operation: ')
arr1.insert(1, 60)

for x in arr1: 
    print(x)

print('\ndeletion operation: ')
arr1.remove(40)

for x in arr1:
    print(x)

print('\nsearch operation: ')
searched_element = 20
print ('searched element: ',searched_element, ' index:', arr1.index(20))
