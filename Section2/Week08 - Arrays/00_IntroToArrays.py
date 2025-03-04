# ----------------------------------------------------------
# Title:    Introduction to Arrays and Lists (Containers)
# Author:   Clint MacDonald
# Date:     March 4, 2025
# Purpose:  Learning the Basics of Arrays/Lists
# ----------------------------------------------------------

#region Introduction to Arrays
# ----------------------------------------------------------
'''
What is an Array?
Is a way to store multiple values within one container.  In Python arrays are actually stored as lists.
------------------------------------
Definitions:
Array:      A way to store multiple values within one container - name of the array is the pointer to the starting memory address
Element:    Each value in the array
Index:      The position of the element in the array (Starts at 0)
------------------------------------
An array is a collection of items stored at continuous memory locations.
The idea is to store multiple items of the same type together.
This makes it easier to calculate the position of each element by
simply adding an offset to a base value,
i.e., the memory location of the first element of the array (generally denoted by the name of the array).
------------------------------------
for example: an integer uses 4 bytes of memory and can be represented by  |____| where each _ is a byte of memory.
An array of 5 integers can be represented as follows:
|____|____|____|____|____| - a series of consecutive memory locations of 4 bytes each
If the base address of the array is 2000 and the size of an integer is 4 bytes, then the memory locations of the array
would be as follows:
|2000|2004|2008|2012|2016|  where the name of the array represents the base starting address of the array.
------------------------------------
In Python, the concept of an array technically does not exist, but are in fact lists
which can be used to simulate arrays.  So when we say arrays, we are referring to lists in Python. In other languages, such as C, C++, Java, etc., arrays are a built-in data type and lists are a slightly different type of container.
------------------------------------
Array Basics
- A list is a collection of objects that are ordered and changeable.
- Lists are defined by enclosing the index numbers in square brackets [].
- The elements in a list/array are indexed starting at 0.
- We can access any element in a list using the associated index
- The index of the first element is 0, the second is 1, and so on....
'''

# ----------------------------------------------------------
#endregion

#region Array Declarations
# ----------------------------------------------------------
# Example
# create an array of integers and output the element in the array

myArray1 = []                               # defining an empty list
myArray2 = [ 10, 20 , 30, 40 ,50 ]          # a list of 5 integers
myArray3 = [ "apple", "banana", "cherry" ]  # a list of 3 strings
myArray4 = [ 10, "apple", 20.5 ]            # a list of mixed data types

# ----------------------------------------------------------
#endregion

#region Output of Arrays
# ----------------------------------------------------------
print(myArray2)         # prints [10, 20, 30, 40, 50]
print(myArray2[2])      # prints 30
#print(myArray2[5])      # ERROR - index out of range

for value in myArray2:
    print(value)

# ----------------------------------------------------------
#endregion

#region Updating and Manipulating Elements of an Array
# ----------------------------------------------------------
print('-'*40)
print(myArray3)
# change an element value
myArray3[1] = "orange"
print(myArray3)

# add a new element
myArray3.append("kiwi")
print(myArray3)

# delete Array elements
myArray3.pop()  # remove the last element
print(myArray3)

myArray3.pop(1)
print(myArray3)

# Slicing Arrays
print('-'*40)
myArray5 = [1,2,3,4,5,6,7,8,9,10]
print(myArray5)
print(myArray5[2:5])
myArray6 = myArray5[:5]
print(myArray5)
print(myArray6)
print(myArray5[5:])

# ----------------------------------------------------------
#endregion

#region Sorting Arrays
# ----------------------------------------------------------
print('-'*40)
myArray7 = [4,2,1,3,5]
myArray8 = ["banana", "apple", "kiwi", "cherry"]

print(myArray7)
print(myArray8)

myArray7.sort()
myArray8.sort()

print(myArray7)
print(myArray8)

# ----------------------------------------------------------
#endregion

#region Looping through arrays
# ----------------------------------------------------------
print('-'*40)
myArray9 = [ 4, 6, 7, 2, 9, 1, 3, 8, 5, 10 ]

for value in myArray9:
    print(value)

print('-'*40)
arrayLength = len(myArray9)
print(arrayLength)

for i in range(arrayLength):
    print(myArray9[i])

# ----------------------------------------------------------
#endregion

#region Array Methods
# ----------------------------------------------------------
'''
append()    Adds an element at the end of the list
clear()     Removes all the elements from the list
copy()      Returns a copy of the list
count()     Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()     Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()       Removes the element at the specified position
remove()    Removes the first item with the specified value
reverse()   Reverses the order of the list
sort()      Sorts the list
len()       Returns the number of elements in the list
list()      Returns a list, i.e. converts a tuple into a list
tuple()     Returns a tuple, i.e. converts a list into a tuple
min()       Returns the smallest element in the list
max()       Returns the largest element in the list
'''
# ----------------------------------------------------------
#endregion

# Tuples/Dictionary Example
print('-'*40)
myScore = {}
myScore['day1'] = 100
myScore['day2'] = 200

print(myScore)