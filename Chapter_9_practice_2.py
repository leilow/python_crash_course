# # ===== TRY IT YOURSELF===============

# 9-13 OVERED DICTIONARY

from collections import OrderedDict

glossary = OrderedDict()

glossary = {
    'variable': 'use to store value',
    'function': 'named block of code that performs a task',
    'tupled': 'immutable lists',
    'dictionaries': 'connections between pieces of information',
    'python': 'a programming language',
}

print("\n")
for key, value in glossary.items():
    print(f"{key.capitalize()}: {value.capitalize()}")
print("\n")

# 9-14 DICE / RANDOM ===================

from random import randint

class Die:
    """create a simple die class"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die = Die(20)
for _ in range(0, 10):
    die.roll_die()

# 9-14 LOTTERY==========================

from random import choice

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# # for loop to show how many times it took to get a winning ticket
my_ticket = choice(values)

for i in range(0, len(values)):
    print(choice(values))
    if values[i] == my_ticket:
        print(f"It took {i+1} iterations to get the ticket {values[i]}")
        break

# # randomly generate a ticket value
print(f"The following tickets have won a price:")
for _ in range(0, 4):
    print(choice(values))

