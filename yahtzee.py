from die import Die


class YahtzeeMainClass:
    intTurn = 1
    keepItGoing = True

    def __init__(self):
        self.intTurn = 1

    def is_yahtzee(self, diceRolls):
        return all(dice == diceRolls[0] for dice in diceRolls)

    def playerTurn(self):
        print(f"Starting turn: {self.intTurn} of 3, rolling dice")
        diceRolls = []
        for i in range(5):
            die = Die()
            #die.value = 5
            diceRolls.append(die.value)
            print(die)

        if self.is_yahtzee(diceRolls):
            print("You win!")
            self.playAgain()

        if self.intTurn != 3:
            if input("Want to throw again? (y for yes, anything else for no) ") == "y":
                self.intTurn += 1
            else:
                self.keepItGoing = False

        if self.intTurn == 3:
            self.playAgain()

    def run(self):
        while self.keepItGoing:
            self.playerTurn()

    def playAgain(self):
        if input("Game over! Want to play again? ") == "y":
            self.intTurn = 1
            self.keepItGoing = True
            return self.keepItGoing
        else:
            self.keepItGoing = False


def main():
    YahtzeeMainClass()


if __name__ == "__main__":
    game = YahtzeeMainClass()
    game.run()
