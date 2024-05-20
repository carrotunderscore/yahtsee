import random


class Die:
    def __init__(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return "Dice shows " + str(self.value)

