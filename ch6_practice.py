# # ---------CHAPTER 6------------------


# to access the value associated with a key
alien = {'color': 'green'}
print(alien['color'])

alien = {'color': 'green', 'points': '5'}
new_points = alien['points']
print(f"You just earned " + str(new_points) + " points!")

# adding new key-value pairs to dictionary
alien = {'color': 'green', 'points': '5'}
alien['height'] = 25
alien['weight'] = 100
print(alien)

# starting with an empty dictionary
alien = {}
print(alien)
alien['color'] = 'green'
alien['heigh'] = 25
print(alien)

# modify the value, keep the key the same
alien = {'color': 'green'}
print(f"The alien is {alien['color']}.")
alien['color'] = 'yellow'
print(f"The alien is now {alien['color']}.")

# modifying the value to return a different answer
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# # ------------------------------------
# removing a key-value pair

alien = {'color': 'green', 'points': 5}
del alien['points']
print(alien)

alien['planet'] = 'mars'
print(alien)

# # ------------------------------------

# a dictionary of similar objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
}

print(favorite_languages)
print(favorite_languages['jen'])
print(f"Jen's favorite lanague is: {favorite_languages['jen'].title()}.")

# # ------------------------------------

# 6.1 friend's profile

friends_info = {
    'first name': 'nancy',
    'last name': 'shon',
    'age': '34',
    'job': 'car tech',
    'city': 'honolulu',
}

print(friends_info)
print(f"Nancy's last name is Korean. It's {friends_info['last name'].title()}.")

# # ------------------------------------

# # 6.2 favorite number

fav_nums = {
    'chaz': '5',
    'sarah': '66',
    'bekha': '28',
    'sean': '32',
    'nancy': '100',
}

# for key in fav_nums.keys():
#     print(key)
# for value in fav_nums.values():
#     print(value)

# print(f"Chaz's favorite number is {fav_nums['chaz']}.")
# print(f"Sarah's favorite number is {fav_nums['sarah']}.")
# print(f"Bekha's favorite number is {fav_nums['bekha']}.")
# print(f"Sean's favorite number is {fav_nums['sean']}.")
# print(f"Nancy's favorite number is {fav_nums['nancy']}.")

for key, value in fav_nums.items():
    # print(key, ' : ', value)
    print(key.title() + "\'s favorite number is " + value.title() + ".")

# # ------------------------------------
# 6-3 Glossary

glossary = {
    'variable': 'use to store value',
    'function': 'named block of code that performs a task',
    'tupled': 'immutable lists',
    'dictionaries': 'connections between pieces of information',
    'python': 'a programming language',
}

for key, value in glossary.items():
    print("\n" + key.capitalize(), ':', value.capitalize() + ".\n")

# # ------------------------------------
# # looping through all key-value pairs in a dictionary
# # items method

user_1 = {
    'username': 'leilow808',
    'first': 'leimomi',
    'last': 'bong',
}

for key, value in user_1.items():
    print("\nKey: " + key.title())
    print("Value: " + value.title())

neighbors = {
    'sean': 808,
    'nancy': 810,
    'bekha': 811,
    'chaz': 807,
    'yayoi': 809,
}

for neighbor, num in neighbors.items():
    print(neighbor.title() + " lives in apartment " + str(num) + ".")
print("These are my neighbors. We're all friends!")

# # ------------------------------------
# # keys methods

neighbors = {
    'sean': 808,
    'nancy': 810,
    'bekha': 811,
    'chaz': 807,
    'yayoi': 809,
}

for neighbor in neighbors.keys():
    print(neighbor.title())

for neighbor in neighbors:
    print(neighbor.title())

for number in neighbors.values():
    print(number)

friends = ['nancy', 'sean', 'yayoi']

for name in neighbors.keys():
    print(name.title())

    if name in friends:
        print("Hey there " + name.title())

for name in sorted(neighbors.keys()):
    print(name.title() + ", thanks for being my neighbor.")

for number in neighbors.values():
    print(number)
# print("We all live on the 8th floor!")

# # ------------------------------------

# using set to make a list without repeats

favorite_foods = {
    'nancy': 'fries',
    'sean': 'fries',
    'roger': 'yogurt',
    'kit': 'tuna',
    'sarah': 'nabe',
}

for food in set(favorite_foods.values()):
    print(food)

# # ------------------------------------

# 6-5 Rivers

rivers = {
    'china': 'yangtze',
    'india': 'ganges',
    'afrida': 'congo',
    'brazil': 'sao francisco',
    'america': 'yukon',
    'america': 'mississippi'
}

# use a loop to print a sentence about each river

for key, value in rivers.items():
    print("The " + value.title() + " runs through " + key.capitalize() + ".")

# use a loop to print the name of each river

for river in rivers.values():
    print(river)

# use a loop to print the name of each country

for country in rivers.keys():
    print(country)

# a set that takes out repeats
for river in set(rivers.keys()):
    print(river)

# # my favorite river

fav_rivers = ['america', 'china']

for river in rivers.keys():
    print(river)

    if river in fav_rivers:
        print(river + " is a favorite!")

# --------------------------------------

# # storing dictionaries in a list

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# --------------------------------------

# make a fleet of aliens!

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# if you'd like to change a value in your dictionary
# you can use range
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
print(aliens[0:3])

# you should be able to use an elif statment here with the above block code
# it wasn't working for me??
for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 10
    print(aliens[0:3])

# check to see the first 5 aliens added to the list
for alien in aliens[:5]:
    print(alien)
print("...")

# check to see how many aliens have been created in total
print("Total number of aliences: " + str(len(aliens)))

# --------------------------------------

# list in a dictionary
# storing info about a pizza

pizza = {
    'crust': 'brooklyn',
    'toppings': ['mushrooms', 'extra cheese', 'sausage'],
}

# summarize your order
print("You ordered a " + pizza['crust'] + " style pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_toppings = {
    'nancy': ['extra cheese', 'extra pepporoni'],
    'sean': ['olives', 'feta', 'sardines'],
    'roger': ['peppers', 'red onions', 'pesto'],
    'sarah': ['extra cheese', 'tomatoes'],
    'lei': ['arugala'],
}

for name, toppings in favorite_toppings.items():
    print("\n" + name.title() + "'s favorite pizza toppings are:")
    for topping in toppings:
        print("\t" + topping.title())

# --------------------------------------

#  dictionary in dictioanry

users = {
    'ChooChoo808': {
        'first': 'sean',
        'last': 'cho',
        'location': 'honolulu',
        'school': 'uh manoa'
    },
    'LinCiCandy': {
        'first': 'cynthia',
        'last': 'lin',
        'location': 'honolulu',
        'school': 'princeton',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    school = user_info['school']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    print("\tSchool: " + school.title())

# # ------------------------------------

# # 6-7: name dictionaries for 3 people, store in a list
# # loop your list, print everything you know about each person

nancy_shon = {'first name': 'nancy', 'last name': 'shon', 'location': 'honolulu', 'hobby': 'pottery', 'job': 'car tech'}
roger_bong = {'first name': 'roger', 'last name': 'bong', 'location': 'seattle', 'hobby': 'music', 'job': 'business owner'}
sarah_umamoto = {'first name': 'sarah', 'last name': 'umamoto', 'location': 'san diego', 'hobby': 'surfing', 'job': 'coordinator'}

people = [nancy_shon, roger_bong, sarah_umamoto]

for x in people:
    for key, value in x.items():
        print(f"...{key.title()}: {value.title()}")

# this block can do a simple loop that prints each dictionary on a separate line
for person in people:
    print(people)

# print(people[:2]) #prints roger and nancys info as dictionaries
print(people[0]) #prints the entire dictionary
print(people[0]['location']) #value
print(people[0]['first name'].title()) #key and titlecase
print(people[0]['job'].title())

# update her information
people[0]['location'] = 'new york'
people[0]['job'] = 'designer'
print(people[0]['location'].title())

# print statements the information about each person

# nancy

print(f"------\nMy neighbor\'s name is " + people[0]['first name'].title() + " " + people[0]['last name'].title() + ".")
print(f"She used to live next door, but recently she moved to " + people[0]['location'].title() + ".")
print(f"She works at her family's business, but she's trained as a " + people[0]['job'] + ".")

# roger
print(f"------\nThe next person on my list if my husband, " + people[1]['first name'].title() + ".")
print(f"He's a " + people[1]['job'].title() + " of an independent record label. They do good work!")
print(f"Originally he was born and raised in " + people[1]['location'] + ". We visit often!")

# sarah
print(f"------\nLast but not least is my friend " + people[2]['first name'].title() + " " + people[2]['last name'] + "!")
print(f"She's a " + people[2]['job'] + " at a local church, and an amazing mother!")
print(f"Her and her family live in " + people[2]['location'].title() + " and visit Hawaii regularly.")

# # --------------------------------------

# 6-8 make several dictionaries
# name of dictionary is name of a pat

pet1 = {'animal': 'cat', 'owner': 'erin'}
pet2 = {'animal': 'dog', 'owner': 'sam'}
pet3 = {'animal': 'hamster', 'owner': 'terry'}
pet4 = {'animal': 'snake', 'owner': 'megan'}
pet5 = {'animal': 'goldfish', 'owner': 'timo'}

pets = [pet1, pet2, pet3, pet4, pet5]

# loop through list and print everything about the pets

for pet in pets:
    print(pet)
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")

# # --------------------------------------

# # 6.9 Favorite places

favorite_places = {
    'mary': {
        'hawaii': 'nuuanu',
        'california': 'santa cruz',
        'europe': 'paris',
        'asia': 'japan',
    },
    'luke': {
        'hawaii': 'hilo',
        'california': 'los angeles',
        'europe': 'madrid',
        'asia': 'indonesia',
    },
    'alice': {
        'hawaii': 'kailua',
        'california': 'san francisco',
        'europe': 'berlin',
        'asia': 'thailand',
    },
    'will': {
        'hawaii': 'aiea',
        'california': 'big bear',
        'europe': 'netherlands',
        'asia': 'china',
    },
}

for person in favorite_places:
    print(person.title())
    for key, value in favorite_places[person].items():
        print(f"\t{key.title()}: {value.title()}")

# # --------------------------------------

# 6-10 Favorite numbers
# modify 6-2 so every person has more than one favorite number

# # favorite number

fav_nums = {
    'chaz': [5, 1, 2],
    'sarah': [8, 80, 888],
    'bekha': [20, 100],
    'sean': [5, 55],
    'nancy': [1010, 28, 2, 8],
}

for key in fav_nums.keys():
    print(key)
for value in fav_nums.values():
    print(value)

print(f"Chaz's favorite number is {fav_nums['chaz']}.")
print(f"Sarah's favorite number is {fav_nums['sarah']}.")
print(f"Bekha's favorite number is {fav_nums['bekha']}.")
print(f"Sean's favorite number is {fav_nums['sean']}.")
print(f"Nancy's favorite number is {fav_nums['nancy']}.")

for key, value in fav_nums.items():
    print(f"{key.title()}: {value}")

# # final solution
for person, number in fav_nums.items():
    print(f"{person.title()}'s favorite number is:")
    for number in number:
        print("\t" + str(number))

# # --------------------------------------
# # 6-11 Cities
# # create dictionary of cities with info about each

fav_cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'The Louvre is the world\'s biggest art museum.',
    },
    'honolulu': {
        'country': 'america',
        'population': '348 thousand',
        'fact': 'The only royal palace in America.',
    },
    'kyoto': {
        'country': 'japan',
        'population': '1.5 million',
        'fact': 'The original name of Kyoto was Heiankyo.',
    },
}

for city, info in fav_cities.items():
    print(f"{city.title()} is only one of my favorite cities in the world!")
    print("Here's some info about the city! Hope you enjoy.")
    for key, value in info.items():
        print(f"\t{key.title()}: {value.capitalize()}")
    print("\n")

# # --------------------------------------
# # 6-12 Extensions

fav_cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'The Louvre is the world\'s biggest art museum.',
    },
    'honolulu': {
        'country': 'america',
        'population': '348 thousand',
        'fact': 'The only royal palace in America.',
    },
    'kyoto': {
        'country': 'japan',
        'population': '1.5 million',
        'fact': 'The original name of Kyoto was Heiankyo.',
    },
}

# new value added to a nested dictionary
fav_cities['paris']['population'] = '2.2 million'
print(fav_cities['paris']['population'])

fav_cities['kyoto']['fact'] = 'For over 1,000 years Kyoto was the capital city of Japan.'
print(fav_cities['kyoto']['fact'])

# add a new dictionary
fav_cities['dubai'] = {
    'country': 'United Arab Emirates',
    'population': '3.3 million',
    'fact': 'Dubai is home to the tallest skyscraper in the world.',
    }
print(fav_cities)

for city, info in fav_cities.items():
    print(f"{city.title()} is only one of my favorite cities in the world!")
    print("Here's some info about the city! Hope you enjoy.")
    print("------->")
    for key, value in info.items():
        print(f"\t{key.title()}: {value.capitalize()}")
    print("\n")