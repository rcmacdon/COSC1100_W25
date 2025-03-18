# ------------------------------------------------------------------
# Title:    A quick Simulation of a DnD battle
# Date:     March 20, 2025
# Author:   Clint MacDonald
# Purpose:  To demonstrate an example of a tools file used in an application
# ------------------------------------------------------------------

import tools as tools

'''
This is an example of an application that will simulate a battle between two DnD characters.
One character is a fighter and the other is a paladin and they are alternating slashing at each
other with a long sword.  The program will keep track of the hit points and armor class of each
character and determine the winner based on who runs out of hit points first.
'''
#region GLOBAL CONSTANTS
WELCOME_MESSAGE = ('-'*40) + "\nWelcome to the DnD Battle Simulator\n" + ('-'*40)
MIN_AC = 10
MAX_AC = 20
MIN_HP = 10
MAX_HP = 50
MIN_HIT_BONUS = 1
MAX_HIT_BONUS = 6
MIN_DAMAGE_BONUS = 1
MAX_DAMAGE_BONUS = 6
HIT_DAMAGE_DIE = 8
#endregion

#region GLOBAL VARIABLES
number_of_players = 2
players = []
ac = []
hp = []
hit_bonus = []
damage_bonus = []
initiative = []
#endregion

#region FUNCTION DEFINITIONS
def pause():
    '''Pauses the program until the user presses enter'''
    input("Press Enter to continue...")

def initialize_players():
    '''Initializes the players via user input'''
    for i in range(number_of_players):
        print('-'*40)
        print(("Player %i" % (i+1)).upper())
        print('-'*40)

        # obtain information for each character
        player = tools.get_string("Enter the name of player %i: " % (i+1))
        players.append(player)
        ac.append(tools.getIntegerRange(("Enter the armor class for %s: " % player), MIN_AC, MAX_AC))
        hp.append(tools.getIntegerRange(("Enter the hit points for %s: " % player), MIN_HP, MAX_HP))
        hit_bonus.append(tools.getIntegerRange(("Enter the hit bonus for %s: " % player), MIN_HIT_BONUS, MAX_HIT_BONUS))
        damage_bonus.append(tools.getIntegerRange(("Enter the damage bonus for %s: " % player), MIN_DAMAGE_BONUS, MAX_DAMAGE_BONUS))
        initiative.append(tools.getIntegerRange(("Enter the initiative for %s: " % player), 1, 20))

    print(('-'*40) + "\nAll players have been initialized\n" + ('-'*40))
    pause()

def display_players():
    '''Displays the player information'''
    for i in range(number_of_players):
        print('-'*40)
        print(("Player %i" % (i+1)).upper())
        print('-'*40)
        print("Name: %-25s" % players[i])
        print("Armor Class:  %2i" % ac[i])
        print("Hit Points:   %2i" % hp[i])
        print("Hit Bonus:    %2i" % hit_bonus[i])
        print("Damage Bonus: %2i" % damage_bonus[i])
        print("Initiative:   %2i" % initiative[i])
        pause() 

def attack(attacker: int, defender: int):
    '''Simulates an attack by randomizing the dice rolls'''
    print("%s is attacking %s" % (players[attacker], players[defender]))
    pause()

    # roll the dice to see if the attack hits
    roll = tools.get_random_integer(20+hit_bonus[attacker])
    print("%s rolled a %i + %i to hit" % (players[attacker], roll, hit_bonus[attacker]))
    print("%s's armor class is %i" % (players[defender], ac[defender]))
    pause()

    if roll + hit_bonus[attacker] >= ac[defender]:
        print("The attack hits!")
        pause()

        # roll the dice to determine the damage
        damage = tools.get_random_integer(HIT_DAMAGE_DIE) + damage_bonus[attacker]
        print("%s deals %i damage to %s" % (players[attacker], damage, players[defender]))
        hp[defender] -= damage
        pause()
    else:
        print("The attack misses!")
        pause()

def check_death(player: int):
    '''checks if a player has died'''
    if hp[player] <= 0:
        print("%s has died!" % players[player])
        return True
    return False

def battle(player1: int, player2: int):
    '''Simulates the battle between the two characters'''
    print('-'*40)
    print("The battle begins!")
    print('-'*40)
    # determine who goes first
    attacker = player1
    defender = player2
    
    if (tools.get_random_integer(20) + initiative[player1]) <= (tools.get_random_integer(20) + initiative[player2]):
        attacker = player2
        defender = player1
    
    doContinueBattle = True
    while doContinueBattle:
        attack(attacker, defender)

        #end of round stats
        print('-'*40)
        print("End of round stats".upper())

        print("%s's hit points: %i" % (players[player1], hp[player1]))
        print("%s's hit points: %i" % (players[player2], hp[player2]))
        print('-'*40)
        pause()

        # check if one player has died
        if check_death(defender):
            print((("*"*40) + "\n%s wins!\n" + ("*"*40)) % players[attacker])
            doContinueBattle = False
        else:
            attack(defender, attacker)
            if check_death(attacker):
                print((("*"*40) + "\n%s wins!\n" + ("*"*40)) % players[defender])
                doContinueBattle = False

        

    print("The battle has ended!")
    pause()

#endregion

#region MAIN FUNCTION
def main():
    '''Main function to run the DnD Battle Simulator'''
    print(WELCOME_MESSAGE)
    initialize_players()
    display_players()
    doBattle = True
    while doBattle:
        battle(0,1)
        doBattle = tools.get_string("Would you like to battle again? (Y/N): ").upper() == "Y"

    print("Goodbye!")
    exit()
#endregion

# execute the main function first
main()