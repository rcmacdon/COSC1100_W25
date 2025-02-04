# # ----------------------------------
# # Title: Try-Catch-Finally
# # Author: Clint MacDonald
# # Date: Feb. 4, 2025
# # Purpose: To demonstrate the use of the Try structure in programming
# # ----------------------------------

# # try-catch-finally structure
# # in Python: try-except-finally

# try:
#     userInt = int(input("Enter a number: "))
#     print("you entered an Integer: ", userInt)
# except ValueError as e:
#     print("That was not an integer")
#     print(e)

# print("-"*40)

# # ----------------------------------
# # try-catch-finally structure
# # in Python: try-except-finally
# try:
#     userInt = int(input("Enter a number: "))
#     print("you entered an Integer: ", userInt)
# except Exception as e:
#     print("That was not an integer")
#     print(e)
# finally:
#     print("This will always print")

# print("-"*40)

# # ----------------------------------    
# # try-catch-finally structure with multiple exceptions
# try:
#     userInt = int(input("Enter a number: "))
#     print("you entered an Integer: ", userInt)
#     print(5/1)
#     print("division successful")
# except ValueError as v:
#     print("That was not an integer")
#     print(v)
# except ZeroDivisionError as z:
#     print("You can't divide by zero")
#     print(z)
# except Exception as e:
#     print("Something went wrong")
#     print(e)
# finally:
#     print("This will always print")

# print("-"*40)

# # ----------------------------------
# # pseudocode of real finally example
# # ----------------------------------
# # try:
# #     # open file
# #     # do something with file (read it)
# # except Exception as e:
# #     print("Something went wrong")
# #     print(e)
# # finally:
# #     # close file
# # ----------------------------------


# # nested Try blocks
# try:
#     userInt = int(input("Enter a number: "))
#     print("you entered an Integer: ", userInt)

#     try:
#         print(5/0)
#         print("division successful")
#     except ZeroDivisionError as z:
#         print("You can't divide by zero")
#         print(z)
# except ValueError as v:
#     print("That was not an integer")
#     print(v)
# except Exception as e:
#     print("Something went wrong")
#     print(e)
# finally:
#     print("This will always print")

# # ----------------------------------
# # custom exceptions
# # ----------------------------------

# x = 17
# y = 15

# try:
#     if (x>y):
#         raise Exception("x is greater than y")
#     elif (x<y):
#         print("success")

#     # do stuff

# except Exception as e:
#     print(e)
# finally:
#     print("This will always print")

# ----------------------------------
# custom exceptions - example - pick a number between 1 and 10

try:
    userInt = int(input("Enter a number between 1 and 10: "))

    if (userInt < 1):
        raise Exception("Number out of range -- too small")
    elif (userInt > 10):
        raise Exception("Number out of range -- too large")
                        
    print("you entered: ", userInt)
except ValueError as v:
    print("That was not an integer")
    print(v)
except Exception as e:
    print("Range Error")
    print(e)
finally:
    print("This will always print")

print("-"*40)