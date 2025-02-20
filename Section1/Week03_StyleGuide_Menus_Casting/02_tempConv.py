# --------------------------------------
# TITLE:    Week 3 - Temperature Conversion Tool
# AUTHOR:   Clint MacDonald
# DATE:     Jan 23, 2025
# PURPOSE:  to write your first application with planning and coding
# --------------------------------------

# This tool will ask the user for a temperature that is entered using a decimal followed by either a (c, C) or an (f, F) to indicate Celsius or Fahrenheit. The tool will then convert the temperature to the other unit of measure and display the result.

# the degree symbol will be used in the output

# --------------------------------------

# greet the user and explain the tool
print('-'*60)
print(
"""Welcome to the temperature conversion tool by Clint
This tool will convert a temperature from Celsius to Fahrenheit or Fahrenheit to Celsius.
Please enter the temperature followed by a 'C' for Celsius or an 'F' for Fahrenheit.  Do not use spaces."""
)
print('-'*60)

# Prompt the user for their input
# get the user's input and store it in a variable
user_input = input("Enter the temperature to convert: (##.#C or ##.#F): ")

# separate the two parts of the input and store each one separately
temperature_value = user_input[:-1]
temperature_unit = user_input[-1]

# temp code for testing purposes
print(temperature_value)
print(temperature_unit)

# check if first letter of value is '-'
test_value = temperature_value
if temperature_value[0] == '-':
    test_value = temperature_value[1:]

# check if the first part of the input is a number
if test_value.replace('.', '', 1).isdecimal():

    # check if the second part of the input is a valid unit of measure
    if temperature_unit.upper() == 'C':
        # convert the temperature value to F unit of measure
        converted_temperature = round((float(temperature_value) * 9/5) + 32,2)
        converted_unit = 'F'

    elif temperature_unit.upper() == 'F':
        # 7. convert the temperature value to C unit of measure
        converted_temperature = round((float(temperature_value) - 32) * 5/9,2)
        converted_unit = 'C'

    else:
        # if the unit of measure is not valid, give message to user and end program
        print("Invalid unit of measure. Please enter a 'C' or an 'F'.")
        exit()

else:
    # if the value is not a number, give message to user and end program
    print("Invalid temperature value. Please enter a number.")
    exit()

# display the result to the user
print("The converted temperature is: ", converted_temperature, "°", converted_unit)

# end the program
exit()