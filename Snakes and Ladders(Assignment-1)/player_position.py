# Importing modules present in project directory
from dice import *
from configuration import *


# Class used to specify position of player in the game
class PlayerPosition:

    # Function for initialising name and position of each player.
    def __init__(self, name):
        self.name = name
        self.current_position = 0

    # Function for displaying present position of a player in game.
    def display_position(self):
        print("The current position of {} is {}".format(self.name, self.current_position))

    # Function for updating the position of a player according to dice throw value.
    def new_position(self):
        # Use dice_roll() function from dice module to get face value of dice and update current position.
        self.dice_count = DiceClass.dice_roll(self)
        self.current_position += self.dice_count

    # Function for checking whether there is snake bite at present position.
    def check_snake(self):
        for key in ConfigureSnakesAndLadders.snakes:
            if self.current_position == key:
                self.current_position = ConfigureSnakesAndLadders.snakes[key]
                print("!!! SNAKE BITE !!!")
                print("You have gone down from {} to {}".format(key, self.current_position))

    # Function for checking whether there is a ladder climb at present position.
    def check_ladder(self):
        for key in ConfigureSnakesAndLadders.ladders:
            if self.current_position == key:
                self.current_position = ConfigureSnakesAndLadders.ladders[key]
                print("!!! LADDER CLIMBED !!!")
                print("You have gone up from {} to {}".format(key, self.current_position))

    # Function for checking whether a player has won a match or not and display message on winning.
    # If a dice value is such that player crosses 100,it is not considered,
    # Exact 100th position must be reached for winning
    def check_win(self):
        if self.current_position == 100:
            print("{} has won the game".format(self.name))
            return True
        if (self.current_position > 100):
            self.current_position -= self.dice_count
            print("Try again in next turn,you need to reach 100")
            return False
