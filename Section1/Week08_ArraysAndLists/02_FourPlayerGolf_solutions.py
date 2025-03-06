# -------------------------------------------------
# Title:    Week 8 - Thursday Practice Exercise
# Date:     March 6, 2025
# Author:
# Purpose:  To practice using arrays
# -------------------------------------------------

# ----------------
# Instructions
'''
Recreate Tuesdays Golf score application with the following changes (remember the source code is available on GitHub):
1) There are 2 players
2) Scores will be entered by the user for each hole.
3) The game is a skins game, meaning that:
- the player that gets the best score on a hole wins the hole and gets 1 point.  
- If 2 players tie, the hole is carried over and the player who individually wins the next hole gets 2 points, (or 3 points if the previous 2 holes were held over) 
- The overall winner will be the player whom gets the most points.
4) At the end, output a list of holes, the score each player got, par, and the type of score the player got according to the following data:
    -3 - albatross
    -2 - eagle
    -1 - birdie
     0 - par
    +1 - bogie
    +2 - double bogie
''' # ----------------

# Clint's Solution!
import random

#region Function Definitions
#define a function to return a string based on an integer input
def scoreType(score):
    if score == -3: return "albatross"
    elif score == -2: return "eagle"
    elif score == -1: return "birdie"
    elif score == 0: return "par"
    elif score == 1: return "bogie"
    elif score == 2: return "double bogie"
    else: return "unknown"
#endregion

#region Declarations
NUM_HOLES = 5
NUM_PLAYERS = 2
playerNames = []
player1Score = []
player2Score = []
player1Skins = 0
player2Skins = 0
par = [ 3, 4, 3, 5, 4, 5, 4, 4, 4, 3, 4, 4, 5, 4, 5, 3, 4, 4]
#endregion

# golf course with 18 holes has predetermined par scores
totalPar = sum(par)

print('''Welcome to Clint's Golf Simulator
We are playing at Clint's Golf Course Today!  The 18 hole par scores are:''')
print(par)
print("Total Par: %i" % totalPar)

#region obtain playerNames
for i in range(NUM_PLAYERS):
    playerNames.append(input("Please enter player %i's name: " % (i+1)))
#endregion

#region randomize who goes first
currentPlayer = random.randint(0,NUM_PLAYERS - 1)
print("Thankyou - %s will go first!" % (playerNames[currentPlayer]))
#endregion

#region Iterate through holes
# play each hole
holeWorth = 1
for hole in range(NUM_HOLES):
    print("--- Hole %i ---" % (hole+1))
    #loop for each player
    for player in range(2):

        goodInput = False
        while not goodInput:
            score = int(input("Please enter %s's score for " % playerNames[currentPlayer]))
            if 9 < score < 0: raise ValueError()
            try:
                if currentPlayer==0: player1Score.append(score)
                else: player2Score.append(score)
                goodInput = True
            except ValueError as v:
                print("invalid score, please try again")

        currentPlayer += 1
        if currentPlayer >= NUM_PLAYERS: currentPlayer = 0

    # all players entered
    # determine who won the hole
    if player1Score[hole] < player2Score[hole]: 
        player1Skins += holeWorth
        holeWorth = 1
    elif player1Score[hole] > player2Score[hole]: 
        player2Skins += holeWorth
        holeWorth = 1
    else: 
        if hole == NUM_HOLES - 1: 
            player1Skins += holeWorth
            player2Skins += holeWorth
        else: holeWorth += 1

    print("After Hole %i - %s has %i skins and %s has %i skins" % (hole + 1, playerNames[0], player1Skins, playerNames[1], player2Skins))
    print('-'*60)
# --- end of hole entry

#endregion

#region Output Summary
for i in range(NUM_HOLES):

    print("Hole: %2i - Par: %2i %7s's Score: %2i Diff: %2i %12s  %7s's Score: %2i Diff: %2i %12s" % (i + 1, par[i], playerNames[0], player1Score[i], player1Score[i] - par[i], scoreType(player1Score[i] - par[i]), playerNames[1], player2Score[i], player2Score[i] - par[i], scoreType(player2Score[i] - par[i])))

print('-'*60)
print("Total Skins: %s has %i and %s has %i" % (playerNames[0], player1Skins, playerNames[1], player2Skins))
if player1Skins > player2Skins: print("The winner is %s" % playerNames[0])
elif player1Skins < player2Skins: print("The winner is %s" % playerNames[1])
else: print("The game is a tie")
#endregion

