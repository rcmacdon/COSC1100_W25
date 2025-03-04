# ----------------------------------------------------
# Title:    A small program for comparing golf scores
# Author:   Clint MacDonald
# Date:     March 4, 2025
# Purpose:  A see an example of arrays in action
# ----------------------------------------------------
import random

NUM_HOLES = 18

# golf course with 18 holes has predetermined par scores
par = [ 3, 4, 3, 5, 4, 5, 4, 4, 4, 3, 4, 4, 5, 4, 5, 3, 4, 4]
totalPar = sum(par)

print(par)
print("Total Par: %i" % totalPar)

# record person's actual scores
myScore = []
totalScore = 0
for hole in range(NUM_HOLES):
    myScore.append(random.randint(1,6))
    totalScore += myScore[hole]

print(myScore)
print("Player Score: %i" % totalScore)

for i in range(NUM_HOLES):
    print("Hole: %i Par: %i Score: %i Diff: %i" % (i + 1, par[i], myScore[i], myScore[i] - par[i]))






