## --------------------------------------
## Title:   4 Player Golf Game
## Author:  Jonah The Assistant
## Date:    May 6th 2025
## Purpose: Simulate 4 players playing a game of golf
## --------------------------------------

#region 1: initialize variables
player_one = []
player_two = []

hole = 1

player_one_score = 0
player_two_score = 0

stalled = 0

course_record = 59

par = [4, 3, 5, 4, 4, 3, 4, 5, 4, 4, 3, 4, 5, 4, 4, 3, 5, 4]
scores = ["Condor", "Albatross", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Triple Bogey", "Quadruple Bogey", "Disaster"]
#endregion

#region 2: Game logic
while len(player_one) < 18 and len(player_two) < 18:
    player_one_input = input(f"Player 1, enter your score for hole {hole}: ")
    player_two_input = input(f"Player 2, enter your score for hole {hole}: ")
    #region 2.1: Error handling
    try:
        player_one.append(int(player_one_input))
        player_two.append(int(player_two_input))
    except ValueError:
        print("Please enter a valid number for player 1 and 2")
    #endregion
    
    #region 2.2: Score Calculation
    if len(player_one) == hole and len(player_two) == hole:
        player_one_hole_score = int(player_one_input) - par[hole - 1]
        print(f"Player 1 scored a {scores[player_one_hole_score + 4]} on hole {hole}")
        player_two_hole_score = int(player_two_input) - par[hole - 1]
        print(f"Player 2 scored a {scores[player_two_hole_score + 4]} on hole {hole}")
    #endregion
        #region 2.3: Hole results
        if int(player_one_input) < int(player_two_input):
            player_one_score += 1 + stalled
            print(f"Player 1 wins hole {hole}!")
            stalled = 0
        elif int(player_one_input) > int(player_two_input):
            player_two_score += 1 + stalled
            print(f"Player 2 wins hole {hole}!")
            stalled = 0
        elif hole != 18 and player_one_input == player_two_input:
            stalled += 1
            print(f"Hole {hole} is a tie! next hole is worth {stalled + 1} points")
        
        elif hole == 18 and player_one_input == player_two_input:
            print(f"Hole {hole} is a tie! splitting the points between the two players")
            half_stalled = stalled // 2
            player_one_score += 1 + half_stalled
            player_two_score += 1 + half_stalled

        hole += 1
        #endregion
#endregion

#region 3: Game results



if player_one_score > player_two_score:
    print("Player 1 wins!")
    if sum(player_one) < course_record:
        print("Player 1 has set a new course record!")
elif player_two_score > player_one_score:
    print("Player 2 wins!")
    if sum(player_two) < course_record:
        print("Player 2 has set a new course record!")
else:
    print("It's a tie!")
#endregion


