# # for loops
# # when you want to do the same action with every element in a list

# magicians = ['alice', 'david', 'carolina']
# for magicians in magicians:
#     print(magicians)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians: # every indented line following the line is condsidered inside the loop
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}\n")
# print("Thank you, everyone. That was a great show!")

# 4.1 Pizzas:
# pizzas = ['cheese', 'pepporoni', 'supreme']

# for pizzas in pizzas: # by using the (s) or plural at the end, you get an output that prints a list. otherwise you get "the list" printed 3 times
#     # print(pizzas)
#     print(f"My favorite pizza is {pizzas.title()}.") #the loop allows you to write one line of code that's executed till it's no longer True (in this case 3 times for each pizza)
# print("I love pizza so much. I eat it everyday.") #this line sits outside of the loop

# # 4.2 Animals:
# animals = ['lion', 'tiger', 'kitty cat'] #animals with similar characteristics

# for animals in animals:
#     # print(f"I love furry, fluffy animals like the {animals.title()}!") #this statement requires you remove the (s) in animals in the for statement
#     print(f"A {animals.title()} would make a great pet!") #this statement requires you keep the (s) in animals in the for statement
# print("All of these animals have beautiful eyes. They're considered to be perfect hunters too!")

# # example of range function
# numbers = list(range(1,10))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# # Using range() to make a list of numbers
# squares = [] # there's currently nothing in the list
# for value in range(1, 11): # this loop is finding the square of each number 1-11
# 	square = value ** 2 # assigning square to the power of
# 	squares.append(square) # so now we've added square to the list
# print(squares) # we're out of the loop

# # the above code written more concisesly

# squares = []
# for value in range(1,11):
#     squares.append(value**2) # each value is raised to the second power, then appended to the list immediately
# print(squares)

# numbers = [1, 2, 3, 4, 5]
# min_numbers = min(numbers) #this is the code given to us in the book min()
# max_numbers = max(numbers)
# sum = sum(numbers)

# print(min_numbers)
# print(max_numbers)
# print(sum)

# # list comprehension

# squares = [value**2 for value in range(1, 11)]
# print(squares) 
# # the value of square is... the square for the numbers in the range of 1-10

# # 4-3 counting to twenty # print the numbers 1-20 using a for loop
# numbers = list(range(1,20))
# print(numbers)

# # 4-4 one million make a list 1-1mil use a for loop to print

# for value in range(1,1000000000): # control C to stop a block of executing code
#     print(value)

# # 4-5 summing a million # this program is bugging out when i go up to 1 million...

# hundreds = list(range(1, 187878787))
# print(min(hundreds))
# print(max(hundreds))
# print(sum(hundreds))

# # here's the even number example

# even_numbers = list(range(1,20,2)) # this is saying from numbers 1-20 it will print every 2 integers
# print(even_numbers)

# # odd numbers # us the third argument of the range() function to make a list of odd numbers from 1-20, use a for loop

# odd_numbers = list(range(1, 20, 2)) # is we start on an odd number, it counts from there
# print(odd_numbers)

# more_counters = list(range(80, 190, 3)) # from 8- to 190 we're counting every three int
# print(more_counters)

# odd_numbers = [value+2 for value in range(1,20)]
# print(odd_numbers) # here's the for loop we'd use

# # 4-7 Threes... make a list of multiples of 3 from 3-30, use a for loop

# cubes = []
# for value in range(1,10):
#     cubes.append(value**3)
# print(cubes)

# # 4-8 cube comprehension: use the list comprehension to generate a list of 10 cubes

# cubes = [value**3 for value in range(1, 10)]
# print(cubes)

# # slicing examples
# players = ['charles', 'martin', 'michael', 'florence', 'eli']
# print(players[0:3]) # the last two players are left out

# players = ['charles', 'martin', 'michael', 'florence', 'eli']
# print(players[:4])

# players = ['charles', 'martin', 'michael', 'florence', 'eli']
# print(players[2:])
# print(players[-3:])

# players = ['charles', 'martin', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for players in players[:3]:
#     print(players.title())

#  # copying a list using [:]
# my_foods = ['pizza', ' falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli') # to prove that we have two list, we'll append new items to each list
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# # 4-10 slices

# my_foods = ['pizza', ' falafel', 'carrot cake', 'mangos', 'avodcado', 'rice', 'chicken', 'mashed potatoes', 'corn']
# friend_foods = my_foods[:]

# my_foods.append('cannoli') 
# friend_foods.append('ice cream')

# # print("My favorite foods are:")
# # print(my_foods)

# # print("\nMy friend's favorite foods are:")
# # print(friend_foods)

# print(f"The first three items in the list are: \n{my_foods[0:3]}.")
# print(f"Three items from the middle of my list are: \n{my_foods[4:7]}.")
# print(f"The last three items in my list are:\n{my_foods[-3:]}")

# # 4-11 my pizzas, your pizzas #so I need to come back to this and use a for loop somehow...

# my_pizzas = ['pepporoni', 'three cheese', 'hawaiian', 'supreme', 'pesto chicken']
# friend_pizzas = my_pizzas[:]

# # print(friend_pizzas) # test

# my_pizzas.append('olive mushroom')
# friend_pizzas.append('white pizza')

# print(f"My favorite pizzas are:\n{my_pizzas[:]}")
# print(f"My friends favorites pizzas are:\n{friend_pizzas[:]}") # not sure how to get rid of the [''] ???

# # 4-12 - come back to in the morning! pg 146
# write two for loops to print each foods list

# fruits = ['apple', 'orange', 'grapes', 'pear', 'peach']
# friendsfruits = fruits[:]

# fruits.append('cantalop')
# fruits.append('watermelon')
# del fruits[0:1]
# friendsfruits.append('star fruit')
# friendsfruits.append('guava')
# del friendsfruits[0:4]

# print("My favorite fruits are:") # this is not a for loop
# print(*fruits, sep = ", ") # print a list separated by commas

# for fruits in fruits: # i was getting an error when the name has an underscore
#     print(f"My favorite fruits are {fruits.title()}!") # this will loop through the list, which is annoying

# print("My favorite fruit is:") # here i can use a for loop and index to designate my favorite fruit
# for fruit in fruits[1]:
# 	print(fruits.title())

# print("My friends favorite fruits are:")
# for friendsfruits in friendsfruits[:3]:
# 	print(friendsfruits.title())

# # Tuples!

# # example of a tuple
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# # example of looping through all values in a Tuple, it returns like a list
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# example of what not to do..
# dimensions[0] = 250 # this is not support, because a Typle is immutable

# dimensions = (200, 50) # the original dimensions
# print("Original dimensions:")
# for dimension in dimensions:
# 	print(dimension) # watch the syntax on these for loops, (s) for plural will trip you up

# dimensions = (400, 100)
# print("\nModified dimensions:") # we associate a NEW tuple with the variable dimensions
# for dimension in dimensions:
# 	print(dimension)

# 4-13
# a buffet offers only five basic foods, think of five foods and store them in a tuple

# foods = ('salad', 'pasta', 'pizza', 'omletes') # comment this out to move onto the next task
# for food in foods:
#     print(food) 

# foods[0] = ('fruits') # TypeError: 'tuple' object does not support item assignment

# ogfoods = ('salad', 'pasta', 'pizza', 'omletes')
# print("original buffet foods:")
# for ogfood in ogfoods:
#     print(ogfood)

# ogfoods = ('ice cream', 'japanese', 'chinese', 'stirfry')
# print("\nmodified buffet foods:")
# for ogfood in ogfoods:
#     print(ogfood)