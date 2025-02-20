# -----------------------------------
# TITLE:    Week 3 - Variable Names
# AUTHOR:   Clint MacDonald
# DATE:     Jan. 21, 2025
# PURPOSE:  To demonstrate the basics fo variable naming and style guide
# -----------------------------------

# Variable names are used to store data in a program. 
#     They are used to reference data in memory.

# appropriate for the student's first name
first_name = "Clint"        # Decent
student_fname = "Clint"     # Unacceptable - no shortcuts, no abbreviations
student_name = "Clint"      # Bad - too generic
studentFirstName = "Clint"  # Good, camel case
StudentFirstName = "Clint"  # Unacceptable, pascal case
student_first_name = "Clint"# Good
studentfirstname = "Clint"  # Bad - no camelCase
fName = "Clint"             # Bad - abbreviation
Std_First_Name = "Clint"    # Bad - abbreviation, first letter is capitalized

# Camel Case = first letter of each word is capitalized except the first word
# Pascal Case = first letter of each word is capitalized
# Snake Case = words are separated by underscores

# in software, names that start with lower case letters are typically 
# storage locations

# in software, names that start with UPPER case letters are typically
# methods or objects

# -----------------------------------
# give a good variable name for:

# your Mom's birthday!
mother_birthday = "May 5, 1960"
motherBirthday = "May 5, 1960"

# your favorite color
favorite_color = "blue"
favoriteColour = "blue"

# the value of the mathematical term pi
pi = 3.14159 # incorrect
PI = 3.14159 # correct - CONSTANT
Pi = 3.14159 # incorrect

# the speed of light
speed_of_light = 299792458
lightSpeed = 299792458
c = 299792458

# the number of days in a week
days_in_week = 7 # acceptable with context
DAYS_IN_WEEK = 7  # correct - CONSTANT

# formula for converting Celsius to Fahrenheit
celsius = -14
fahrenheit = (9 / 5) * celsius + 32
fahrenheit = round( (9 / 5) * celsius + 32, 2)

# x squared
x = 5
x_squared = x ** 2
x_squared = x * x
x_squared = x ^ 2

# pythagorean theorem
a = 5
b = 12

c = (a ** 2 + b ** 2) ** 0.5
#c  = (math.pow(a, 2) + math.pow(b, 2)) ** 0.5
#c = math.sqrt( math.pow(a, 2) + math.pow(b, 2) )


print("----------------------------------")
# characters in a string

# a string is in fact an array of characters
# each character has an index number starting at 0
professors_name = "Clint MacDonald"
print(professors_name[0]) # C
print(professors_name[1]) # l
print(professors_name[9]) # D

print(professors_name[-1]) # d
print(professors_name[:-1]) # Clint MacDonal

# print letters 3 through 6 of a string
print(professors_name[3:7]) # nt M  
#       note the first one is inclusive, and last is exclusive

print("----------------------------------")