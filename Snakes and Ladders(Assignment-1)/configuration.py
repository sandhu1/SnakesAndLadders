# Class for configuring snakes and ladders on the game board and can be configured at the start of game.
class ConfigureSnakesAndLadders:

    # Dictionaries are used to store values in the way that
    # key is starting point and value is ending point .
    snakes = {}
    ladders = {}

    # Enter snakes values so that it decreases the final position of player.
    def enter_snakes(self):
        self.snakes_number = int(input("ENTER THE NUMBER OF SNAKES : "))
        for i in range(1, self.snakes_number + 1):
            print("SNAKE #{}".format(i))
            temp = int(input("Enter starting point : "))
            self.snakes[temp] = int(input("Enter ending point : "))

    # Enter ladders values so that it increases the final position of player.
    def enter_ladders(self):
        ladders_number = int(input("ENTER THE NUMBER OF LADDERS : "))
        for i in range(1, ladders_number + 1):
            print("LADDER #{}".format(i))
            temp = int(input("Enter starting point : "))
            self.ladders[temp] = int(input("Enter ending point : "))

    # Function used to print snakes and ladders after configuration is done.
    def show_snakes_and_ladders(self):
        print("Snakes in the game are  {}".format(self.snakes))
        print("Ladders in the game are {}".format(self.ladders))