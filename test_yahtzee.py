from yahtzee import YahtzeeMainClass
from die import Die

import pytest


def test_is_yahtzee_when_all_dice_matches():
    dice = [Die(), Die(), Die(), Die(), Die()]

    for die in dice:
        die.value = 6

    assert YahtzeeMainClass().is_yahtzee(dice) is True


def test_is_not_yahtzee_when_one_dice_differs():
    dice = [Die(), Die(), Die(), Die(), Die()]

    for die in dice:
        die.value = 6

    dice[2].value = 5

    assert YahtzeeMainClass().is_yahtzee(dice) is False


if __name__ == '__main__':
    pytest.main()
