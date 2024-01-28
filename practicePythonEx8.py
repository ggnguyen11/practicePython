# practicepython.org | exercise 8 | 01/27/2024
# prompt: make a 2-player rock-paper-scissors game
# given hints: ask for player plays (using input), compare them, print out
# congratulations to winner, and ask if players want to start a new game

# imported sys module for sys.exit() to end script
import sys

# asking for player names
player1 = input("Rock Paper Scissors! Who's player one?\n")
player2 = input("\nWelcome " + player1 + "! " + "Who's player two?\n")

# rps() function for rock, paper, scissors
def rps():
# while loop for game logic, print statement + break instead of return,
# which shouldn't be used within loop
    while True:
# evaluating players' choices, using "\" for line continuation
        p1move = input("\nLet's get this started!" + " " + player1 + \
               ", what's your move?\n")
        p2move = input("\n" + player2 + ", what's your move?\n")
# conditionals
        if p1move.lower() == "rock" and p2move.lower() == "scissors":
            print("\nCongratulations " + player1 + ", you win!\n")
            break
        elif p1move.lower() == "rock" and p2move.lower() == "paper":
            print("\nCongratulations " + player2 + ", you win!\n")
            break
        elif p1move.lower() == "paper" and p2move.lower() == "rock":
            print("\nCongratulations " + player1 + ", you win!\n")
            break
        elif p1move.lower() == "paper" and p2move.lower() == "scissors":
            print("\nCongratulations " + player2 + ", you win!\n")
            break
        elif p1move.lower() == "scissors" and p2move.lower() == "paper":
            print("\nCongratulations " + player1 + ", you win!\n")
            break
        elif p1move.lower() == "scissors" and p2move.lower() == "rock":
            print("\nCongratulations " + player2 + ", you win!\n")
            break
        elif p1move.lower() == p2move.lower():
            print("\nIt's a tie!\n")
            break

# conditional function returning booleans for playing again
def playagain():
    replay = input("Would you like to play again? Y/N\n")
    if replay == "y":
        return True
    elif replay == "n":
        return False
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        return playagain()

# parameterless function call: if playagain() = True then repeat while loop
while True:
    rps()
    if playagain():
        continue
    else:
        sys.exit()