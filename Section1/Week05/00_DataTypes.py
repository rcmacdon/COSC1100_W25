# # --------------------------------
# # Title: Extended Data Types
# # Author: Clint MacDonald
# # Date: Feb. 4, 2025
# # Purpose: To demonstrate the use of data type tools in Python
# # --------------------------------

# # play with data types
# myInt = 5
# myFloat = 5.0
# myString = "hello"

# # print the data types

# print(type(myInt))
# print( (type(myInt) == int) )

# print(type(myFloat))
# print(type(myString))

# # --------------------------------
# # Type Checking
# if (type(myInt) == int):
#     print("myInt is an int")

# if (type(myFloat) == float):
#     print("myFloat is a float")

# if (myInt == myFloat):
#     print("myInt and myFloat are equal")

# # python only
# if (isinstance(myInt, int)):
#     print("myInt is an int")

# # --------------------------------

# myNumber = "5"   # string
# print(type(myNumber))

# # check if the string can be converted to an int?
# if (myNumber.isdigit()):
#     myNumber = int(myNumber)

# print(type(myNumber))


# # --------------------------------
# # Try Catch Finally structure

# # in Python - Try Except Finally

# try:
#     userInt = int(input("Enter a number: "))
#     print("Conversion Successful")
# except Exception as e:
#     print("Conversion Failed")
#     print(e)

# print("-"*60)


# # --------------------------------
# # add the finally
# try:
#     userInt = int(input("Enter a number: "))
#     print("Conversion Successful")  
# except Exception as e:
#     print("Conversion Failed")
#     print(e)
# finally:
#     print("This will always run")

# print("-"*60)


# # --------------------------------
# # pseudocode of an example of finally
# # try:
#     # open file
#     # read file
# # except:
#     # print error message
# # finally:
#     # close file


# # --------------------------------
# # try catch with multiple exceptions
# try:
#     userInt = int(input("Enter a number: "))
#     print("Conversion Successful")
#     print(10 / userInt)
# except ValueError as v:  # specific exception
#     print("Conversion Failed")
#     print("You did not enter a number")
#     print(v)
# except ZeroDivisionError as z:  # specific exception
#     print("Conversion Failed")
#     print("You cannot divide by zero")
#     print(z)
# except Exception as e:  # catch all
#     print("General Error")
#     print(e)
# finally:
#     print("This will always run")

# # --------------------------------
# # Nested Try Catch
# try:
#     userInt = int(input("Enter a number: "))
#     print("Conversion Successful")
    
#     try:
#         print(10 / userInt)
#         print("Division Successful")
#     except ZeroDivisionError as z:  # specific exception
#         print("Division Failed")
#         print("You cannot divide by zero")
#         print(z)
#     except Exception as e:  # catch all
#         print("General Error")
#         print(e)
# except ValueError as v:
#     print("Conversion Failed")
#     print("You did not enter a number")
#     print(v)
# finally:
#     print("This will always run")


# --------------------------------
# throwing exceptions
x = 17
y = 15

try:
    if (x > y):
        raise Exception("x cannot be greater than y")
    else:
        raise Exception("It actually worked and should not of raised an exception")
    
    # do the stuff
    
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    print("This will always run")

