import random


class Dice:
    dices = (1, 2, 3, 4, 5, 6)

    def roll(self):
        dice1 = random.choice(self.dices)
        dice2 = random.choice(self.dices)
        print(f'({dice1}, {dice2})')

    def roll2(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

d1 = Dice()
d1.roll()

d2 = Dice()
print(d2.roll2())
