# add your comment header

#region IMPORTS
#endregion

#region GLOBAL VARIABLES (CONSTANTS)
# YOU MAY NOT CHANGE ANYTHING IN THIS SECTION
# except for the values of the variables for testing purposes
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12
ALLOW_SPECIAL_CHARACTERS = True
ALLOWED_SPECIAL_CHARACTERS = "!@#$%^&*"
MUST_HAVE_DIGIT = True
MUST_HAVE_UPPERCASE = True
MUST_HAVE_LOWERCASE = True
ALLOW_SPACES = False
ALPHANUMERIC_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#endregion

#region FUNCTION DEFINITIONS
# Enter your code here.... erase this comment before submitting

#endregion

#region MAIN APPLICATION

# YOU MAY NOT CHANGE ANYTHING IN THIS REGION
print('-'*40)
print("Welcome to the Password Generator")

doContinue = True
while doContinue:
    print('-'*40)

    # input
    password = getString("Enter your password (Q to Quit): ")
    if password.upper() == "Q":
        doContinue = False
        continue

    # have the user re-type the password to confirm
    password2 = getString("Re-enter your password: ")

    # check if the passwords match
    if passwordsMatch(password, password2):

        # check if the password is valid
        if validatePassword(password):    
            print("Password is valid")
        else: 
            print("Passwords are invalid")
    else:
        print("Passwords do not match")

    input("Press Enter to continue...")

print("Goodbye!")
print('-'*40)
exit(0)
#endregion