# -----------------------------------
# TITLE:    Week 2 - Data Types
# AUTHOR:   Clint MacDonald
# DATE:     Jan. 14, 2025
# PURPOSE:  To demonstrate the basic data types in Python
# -----------------------------------

# -----------------------------------
# Main Data Types
# - String - alphanumeric characters, enclose strings inside of double quotes
# - Integer - whole numbers
# - decimal - fractions, numbers with decimal places, large limit on the number of decimal places
# - float - floating point numbers, like decimals but less precise and less number of decimal places
# - Boolean - True or False, Yes or No, 1 or 0 (take exactly 1 bit of memory)


# - Memory
# - 1 bit = 1 binary digit (0 or 1)
# - 1 byte = 8 bits (256 possible values)
# - 1 kilobyte (KB) = 1024 bytes
# - 1 megabyte (MB) = 1024 kilobytes
# - 1 alphanumeric character takes 1 byte of memory (based on the character code, ASCII being the most popular)

# - variable declaration
# integers
xi = 2
yi = 6
# floats
xf = 2.1
yf = 6.3
# strings
xs = "2"
ys = "6"
# Boolean
xb = True
yb = False

# do some calculations
print(xi + yi) # addition
print(xf + yf) # addition
print(xs + ys) # string concatenation
print(xb + yb) # boolean operation

# mixing them
# print(xi + ys) # error
print (xi + int(ys)) # cast string to integer

# print(xs + yi) # error
print(xs + str(yi)) # cast integer to string

# floats
print(xf + yf)
print("The answer is: %f" % (xf + yf))
print("The answer is: %.2f" % (xf + yf))

# division
print(7 / 3) # 2.3333333333333335
print(7 // 3) # 2

# output 7/3 formatted with 3 decimal places
print("The answer is: %.3f" % (7 / 3))
print("The answer is: %.3f" % (8 / 3))

#print(("%.3f" % (7 / 3)) + 2) # error
print(float("%.3f" % (7 / 3)) + 2) # cast string to float
print(round((7 / 3), 3) + 2) # round to 3 decimal places

# formatting strings with Multiple variables
print("Number 1: %i    Number 2: %i" % (xi, yi))

fname = "Clint"
lname = "MacDonald"
print("My name is: %s %s" % (fname, lname))

