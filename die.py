import random


class Die:
    def __init__(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return "Dice shows " + str(self.value)

    @staticmethod
    def DieRoll():
        value = random.randint(1, 6)
        return value

    @staticmethod
    def die_reroll():
        return Die.DieRoll()
