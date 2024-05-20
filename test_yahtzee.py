import pytest


def test_is_yahtzee_when_all_dice_matches():
    diceRolls = [1, 1, 1]
    assert all(die == diceRolls[0] for die in diceRolls)


def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    data = [1, 2, 3, 4, 5]
    assert len(set(data)) == len(data)


if __name__ == '__main__':
    pytest.main()
