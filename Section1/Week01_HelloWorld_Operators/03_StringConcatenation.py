# ----------------------------------
# Title:    String Concatenation
# Author:   Clint MacDonald, StudentID
# Date:     January 9, 2025
# Purpose:  Learn 5 ways to do String Concatenation.
# ----------------------------------

# define variables
first_name = "Clint"
last_name = "MacDonald"
student_id = "123456789"

# concatenate using the + operator
full_name = first_name + " " + last_name + " (" + student_id + ")"

print("-------------------------")

print("Hello, My name is " + full_name + ".")
print("Hello, My name is", full_name, ".")
print("Hello, My name is %s." % full_name)
print(f"Hello, My name is {full_name}.")
print("Hello, My name is {}.".format(full_name))



print("\n")
