# SNAKES AND LADDERS GAME

# Importing useful modules created in project directory
from player_position import *
from configuration import *


class StartGame:
    # Method involving all important steps.
    def start_rolling(self):

        print("WELCOME TO SNAKES AND LADDERS")

        # Enter names of players.
        player1 = PlayerPosition(input("ENTER FIRST PLAYER'S NAME : "))
        player2 = PlayerPosition(input("ENTER SECOND PLAYER'S NAME : "))

        # Configure snakes and ladders by specifying their start and end points.
        conf = ConfigureSnakesAndLadders()
        conf.enter_snakes()
        conf.enter_ladders()
        conf.show_snakes_and_ladders()

        # Show initial positions of both players i.e 0 .
        player1.display_position()
        player2.display_position()

        # An infinite loop runs until a player wins.
        while True:

            # Steps and functions for player1.
            print("{}'s turn".format(player1.name))
            roll = input("PRESS ENTER TO ROLL THE DICE")
            player1.new_position()
            player1.check_snake()
            player1.check_ladder()

            # Break the loop when a player wins.
            if player1.check_win():
                break
            player1.display_position()

            # Give one more turn if a dice shows "6"
            if player1.dice_count == 6:
                print("!!!You got 6 ,Press ENTER for another turn!!!")
                player1.new_position()
                player1.check_snake()
                player1.check_ladder()
                if player1.check_win():
                    break
                player1.display_position()

            print("\n")
            print("--------------------------------------")
            print("\n")

            # Steps and functions for player2
            print("{}'s turn".format(player2.name))
            roll = input("PRESS ENTER TO ROLL THE DICE")
            player2.new_position()
            player2.check_snake()
            player2.check_ladder()
            if player2.check_win():
                break
            player2.display_position()

            if player2.dice_count == 6:
                print("!!!You got 6 .Press ENTER for another turn!!!")
                player2.new_position()
                player2.check_snake()
                player2.check_ladder()
                if player2.check_win():
                    break
                player2.display_position()

            print("\n")
            print("--------------------------------------")
            print("\n")


if __name__ == '__main__':
    # main driver program
    match = StartGame()
    match.start_rolling()
