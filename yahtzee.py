from die import Die


class YahtzeeMainClass:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.turn = 1
        self.keep_going = True
        self.limitReached = False

    def is_yahtzee(self, dice_rolls):
        return all(dice == dice_rolls[0] for dice in dice_rolls)

    def play_turn(self):
        if self.turn == 3:
            self.limitReached = True
        if self.turn == 1:
            self.limitReached = False
        print(f"Starting turn: {self.turn} of 3, rolling dice")
        # self.dice = [6, 6, 6, 6, 6]
        for die in self.dice:
            print(die)

        if self.is_yahtzee(self.dice):
            print("You win!")
            self.play_again()

        if self.turn != 3 and self.keep_going:
            if input("Want to throw again? (y for yes, anything else for no) ") == "y":
                self.turn += 1
            else:
                self.keep_going = False

        if self.limitReached:
            self.play_again()

    def play_again(self):
        if input("Game over! Want to play again? ") == "y":
            self.turn = 1
            self.keep_going = True
        else:
            self.keep_going = False

    def run(self):
        while self.keep_going:
            self.play_turn()


game = YahtzeeMainClass()
game.run()
