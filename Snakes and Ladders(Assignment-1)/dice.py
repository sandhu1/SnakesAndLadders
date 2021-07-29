import random


# Class for defining dice_roll() function
# dice_roll() helps to return a face value for one dice throw.
class DiceClass:

    def dice_roll(self):
        rand_num = random.randint(1, 6)
        print("You got {} on face of dice".format(rand_num))
        return rand_num
