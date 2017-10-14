from random import randint

class Die():
    """ simple simulation of a random dice roll """
    def __init__(self, sides=6):
        """ init the die """
        self.sides = sides

    def roll_die(self, times):
        for time in range(1,times + 1):
            x = randint(1, self.sides)
            s = "\nRoll #{}:".format(time)
            s += "The {} sided die has landed on {}".format(self.sides, x)
            print(s)


if __name__ == "__main__":

    # a 6 sieded die rolled 10 times
    my_roll = Die()
    my_roll.roll_die(10)

    # a 10 sieded die rolled 10 times
    my_roll = Die(10)
    my_roll.roll_die(10)

    # a 20 sieded die rolled 10 times
    my_roll = Die(20)
    my_roll.roll_die(10)

