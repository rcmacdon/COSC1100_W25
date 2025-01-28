# --------------------------------------
# Title: Loop Basics: Iteration
# Author: Clint MacDonald
# Date: Jan 28, 2025
# Purpose: To demonstrate the basics of iteration using loops in Programming
# --------------------------------------

# Four Different Kinds of Loops

# For Loop
# used when you know exactly how many iterations to complete
print("-"*60)
print("For Loop")

for i in range(5):
    print(i, 'multiple of 2:', i*2)
print("End of loop: i = ", i)

# for loop in C languages (c, c++, c#, Java, JavaScript, PHP)
# for (int i = 0; i < 5; i++) {
#       console.log("%d multiple of 2: %d\n", i, i*2);
# }
# console.log("End of loop: i = %d\n", i);   

# While Loop
# unknown number of iterations but with an exit strategy
#      doing the first iteration is NOT guaranteed
print("-"*60)
print("While Loop")
i = 0
while i < 5:
    print(i, 'multiple of 2:', i*2)
    i += 1    # i = i + 1
print("End of loop: i = ", i)

# Do While (Loop Until)
# unknown number of iterations but with an exit strategy
#      doing the first iteration is guaranteed


# Does not exist in Python
# simulate it
print("-"*60)
print("Do While Loop")
i = 0
while True: # UNACCEPTABLE
    print(i, 'multiple of 2:', i*2)
    i += 1
    if i >= 5:
        break # UNACCEPTABLE
print("End of loop: i = ", i)
#
# do {
#    console.log("%d multiple of 2: %d\n", i, i*2);
#    i++;
# } while (i < 5);

# For Each Loop
# unknown number of iterations but you want ALL of them

print("-"*60)
print("For Each Loop")
for i in [0, 1, 2, 4, 7]:
    print(i, 'multiple of 2:', i*2)


# --------------------------------------
# Different Versions of For Loop
# --------------------------------------
# Basic
print("-"*60)
print("Basic For Loop")
for i in range(5):
    print(i, 'multiple of 2:', i*2)

# With Start and End
print("-"*60)   
print("For Loop with Start and End")
for i in range(5, 10):
    print(i, 'multiple of 2:', i*2)

# With Start, End and Step  
print("-"*60)
print("For Loop with Start, End, and Step")
for i in range(5, 10, 2):
    print(i, 'multiple of 2:', i*2)

# With Start, End, and Negative Step
print("-"*60)
print("For Loop with Start, End, and Negative Step")
for i in range(10, 5, -1):
    print(i, 'multiple of 2:', i*2)

# with a String
print("-"*60)
print("For Loop with a String")
for c in "Hello World":
    print(c)
    if c.lower() == 'o':
        print("Found an 'o'")

# Practice 1
# Print all the numbers from 1 to 100
print("-"*60)
print("Practice 1")
for i in range(1, 101):
    print(i)

print("-"*60)
print("Practice 1 with while loop")
i = 1
while i <= 100:
    print(i)
    i += 1
    
# Practice 2
# print the multiples of 4 up to 200 using a while loop
print("-"*60)
print("Practice 2")
i = 4
while i <= 200:
    print(i)
    i += 4

# Practice 3
# print the exponentiation of 2 up to 2^31
# trivia: what does this number represent?
# 2^31 = 2,147,483,648
print("-"*60)
print("Practice 3")
i = 0
while i <= 31:
    print(2**i)
    i += 1 

# or
print("-"*60)
print("Practice 3 with for loop")
for i in range(32):
    print(2**i)