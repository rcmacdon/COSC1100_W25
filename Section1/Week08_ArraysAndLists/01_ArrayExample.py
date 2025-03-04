# ---------------------------------------------
# Title: Array Example 1
# Author: Clint MacDonald
# Date: March 4, 2025
# Purpose: To learn how array elements are used in coding
# ---------------------------------------------
import random

# golf example of 18 holes
par = [ 3, 4, 3, 5, 4, 5, 4, 4, 4, 3, 4, 4, 5, 4, 5, 3, 4, 4]

totalPar = 0
for p in par:
    totalPar += p

print(par)
print("The total pare is: " + str(totalPar))

myScore = []
totalScore = 0
for i in range(18):
    myScore.append(random.randint(1,6))
    totalScore += myScore[i]

print(myScore)

for i in range(18):
    #print("Hole: " + str(i+1) + " Par: " + str(par[i]) + " Score: " + str(myScore[i]) + "  Diff: " + str(myScore[i] - par[i]))
    print("Hole: %i Par: %i Score: %i Diff: %i" % (i+1, par[i], myScore[i], myScore[i]-par[i]))

print('-'*40)
print("Course Par: %i   Your Score: %i   Overall Score: %i" % (totalPar, totalScore, totalScore - totalPar))


