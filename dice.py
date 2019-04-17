from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides
    def roll_die(self):
        # random dice roll
        x = randint(1, self.sides)
        return x

#regular 6 sides die.
roll1 = Die(6)

result_1 = []

# roll the dice 10 times
for roll_num in range(10):
    result = roll1.roll_die()
    result_1.append(result)

print(result_1)

result_2 = []

#playing around with dice with a different num of sides
roll2 = Die(10)

for roll_num in range(10):
    result = roll2.roll_die()
    result_2.append(result)

print(result_2)
