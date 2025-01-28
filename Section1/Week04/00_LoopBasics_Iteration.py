# ------------------------------------
# Title: Iteration Basics
# Author: Clint MacDonald
# Date: Jan 28, 2025
# Purpose: To demonstrate the basics of iteration in Programming
# ------------------------------------

# In mainstream programming there are 4 types of loops
# 1. For Loop
# 2. While Loop
# 3. Do While Loop (Loop Until)
# 4. For Each Loop

# In Python, there are only 2/3 types of loops

# 1. For Loop
# Used in iteration when we know exactly how many there are
print("-"*60)
print("Basic For Loop")
for i in range(5):
    print(i, 'multiple of 2:', i*2)

# in other languages
# for (int i = 0; i < 5; i++) {        
#     console.log(i)
# }

# i++ is same as i = i + 1

# 2. While Loop
# Used in iteration when we don't know how many there are
# and there is a specific exit strategy
#    - the first iteration is NOT guaranteed
print("-"*60)
print("Basic While Loop")
i = 0
while i < 5:
    print(i, 'multiple of 2:', i*2)
    i += 1  # same as i = i + 1

# 3. Do While Loop (Loop Until) - DOES NOT EXIST IN PYTHON
# Used in iteration when we don't know how many there are
# and there is a specific exit strategy
#    - the first iteration is guaranteed
print("-"*60)
print("Basic Do While Loop")
i = 0
while True:  # UNACCEPTABLE
    print(i, 'multiple of 2:', i*2)
    i += 1  
    if i >= 5:
        break    # UNACCEPTABLE
# in other languages
# i = 0
# do {
#     console.log(i)
#     i++
# } while (i < 5)



# 4. For Each Loop
print("-"*60)
print("Basic For Each Loop")
for i in [0, 1, 2, 3, 4, 7]:   # with a list
    print(i, 'multiple of 2:', i*2)

# many different versions of for loop
# For loop with a string
print("-"*60)
print("For Loop with a String")
for i in "Hello World":  
    print(i)
    if i == 'o':
        print("Found 'o'")

# for loop with a range with a start and an end
print("-"*60)
print("For Loop with a Range, Start, and End")
for i in range(5, 10):  # 5 is inclusive, 10 is exclusive
    print(i)

# for loop with a range with a start, end, and step
print("-"*60)
print("For Loop with a Range, Start, End, and Step")
for i in range(5, 10, 2):  # (start, end, step)
    print(i)

# for loop with a range with a start, end, and step (negative)
print("-"*60)
print("For Loop with a Range, Start, End, and Step (Negative)")
for i in range(10, 5, -1):  # (start, end, step)
    print(i)

# simulated Loop Until
print("-"*60)
print("Simulated Do While Loop")
doLoop = True
i = 0
while doLoop:
    print(i)
    i += 1
    if i >= 5:
        doLoop = False

# next line of code 
print("-"*60)
     

# Practice
# Practice: print multiples of 4 up to 200
print("-"*60)