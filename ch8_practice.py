# # ----FUNCTIONS-------------------------

# # example of a function
# def greet_user(name):
#     """display user name"""
#     print(f"\nHello, {name.title()}!")
# greet_user('jesse')

# # -----TRY IT YOURSELF-------------------
# # 8-2 message

# def display_message(sentence):
#     """display sentence"""
#     print(sentence)

# display_message('\nIn this chapter we are learning about functions.')

# def favorite_book(title):
#     """display favorite book title"""
#     print(f"\nOne of my favorite books is {title.title()}!")

# favorite_book('Ada\'s Algorithm')

# # ------------------------------------

# # positional arguments

# def pet_info(name, animal='cat'):
#     """describes pet"""
#     print(f"\nI have a {animal.title()}, and their name is {name.title()}.")

# pet_info(animal='hamster', name='harry')
# pet_info('dog', 'toby')
# pet_info('cat', 'kit cat hufflepuff')
# pet_info('fox', 'foxy')
# pet_info('mouse', 'mountain')
# pet_info(name='silly goose')
# pet_info('wili')
# pet_info(name='willi', animal='dog')

# # ---TRY IT YOURSELF------------------
# # 8-3 make a t-shirt function
# # 8-4 modify, make size and graphic default

# def make_shirt(color, size='large', graphic='I love Python'):
#     """print size and graphic on tshirt"""
#     print(f"\tYou're ordering a {size}, {color} t-shirt with the message '{graphic.capitalize()}' printed on it.")

# # 8-3 call functions
# make_shirt('medium', 'best day in the world', 'mustard')
# make_shirt(size='large', graphic='best husband in the universe', color='blue tie dye')
# make_shirt('XXL', graphic="sister, sister", color='purple')

# # 8-4 call functions
# make_shirt('black')
# make_shirt(color='brown', size='medium', graphic='I love using Python for automation!')

# # ----CITIES--------------------------
# # 8-5 fucntion that take input: city name, country

# prompt = input("What's your favorite city?  ")

# def fav_city(city, country='america'):
#     print(f"My favorite city is {city.title()} in {country.title()}. It's so charming!")

# fav_city('honolulu')
# fav_city('new york')
# fav_city('madrid', country='spain')

# # ----RETURN VALUES-------------------

# # example
# def get_formatted_name(first, last, middle=''):
#     """Return a full name, neatly formatted"""
#     if middle:
#         full_name = first + ' ' + middle + ' ' + last
#     else:
#         full_name = first + " " + last
#     return full_name.title()

# musicians = []

# musician1 = get_formatted_name('jimi', 'hendrix')
# musician2 = get_formatted_name('Booker', 'Washington', 'tee')
# musicians.append(musician1)
# musicians.append(musician2)

# for musician in musicians:
#     print(musician)


# # RETURN LIST AND DICTS---------------

# def build_person(first, last, location='', age='', pronoun='', email=''):
#     """return a dict of info about a person"""
#     person = {'first': first, 'last': last}
#     if age:
#         person['age'] = age # we're adding this to out list
#     if pronoun:
#         person['pronoun'] = pronoun
#     if email:
#         person['email'] = email
#     return person

# musician1 = build_person('jimi', 'hendrix', 'heaven')
# print(musician1)
# musician2 = build_person('richard', 'smith', 'honolulu', '32', 'she/her', 'rsmith@gmail.com')
# print(musician2)
# musician3 = build_person('roger', 'bong', location='honolulu')
# print(musician3)
# musician4 = build_person('chaz', 'umamoto', 'honoluu', age=22)
# print(musician4)

# #-------------------------------------

# # using a function and while loop

# def get_full_name(first, last):
#     """return full name neatly"""
#     full_name = first + ' ' + last
#     return full_name.title()

# while True:
#     print(f"Please tell me your name: ")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_full_name(f_name, l_name)
#     print(f"Hello {formatted_name.title()}!")
#     break

# # don't use the line below when getting user input
# # print(get_full_name('leimomi', 'bong', 'renee'))

# #----TRY IT YOURSELF------------------

# # 8-6 NAMES

# def city_county(city, country):
#     """ """
#     fcitycountry = city + ', ' + country
#     return fcitycountry

# while True:
#     print(f"Where do you consider your hometown and country?")
#     hometown = input("My hometown is: ")
#     homecountry = input("My home country is: ")

#     fhome = city_county(hometown, homecountry)
#     print(f"\nYou're from {hometown.title()}, {homecountry.title()}? That's rad!")
#     break

# # 8-7 ALBUMS---------------------------

# def make_album(artist, album, tracklist=''):
#     """Return album dictionary"""
#     album = {'artist': artist, 'album': album, 'tracklist': tracklist}
#     return album

# # print(make_album('megan thee stallion', 'fever', tracklist=18))
# # print(make_album('megan thee stallion', 'good news'))
# # print(make_album('megan thee stallion', 'girls in the hood,', 14))

# # while loop that allows us to take in user input

# active = True

# while True:

#     print("===Your Music Library======")
#     print("Enter the album information.")
#     print("(Enter 'q' to quit any time.)")

#     artist = input("Artist Name: ") #these variables use names that are different than the function
#     if artist == 'q':
#         break

#     album = input("Album Title: ")
#     if album == 'q':
#         break

#     tracklist = input("Number of songs: ")
#     if tracklist == 'q':
#         break

#     repeat = input("Did you want to add another album? (yes/no) ")
#     if repeat == 'no':
#         active = False
#         break
    
#     album = make_album(artist, album, tracklist)
#     print(album)

# # ---PASSNG A LIST THROUGH A FUNCTION---

# # creating a unique greeting for everyone on a list
# def greet_user(names):
#     """print a simple greeting to each user in the list."""
#     for name in names:
#         message = "Hello, " + name.title() + "!"
#         print(message)

# usernames = ['hannah', 'tyler', 'margrette']
# greet_user(usernames)

# # ---modifying a list in a function---

# # example problem

# # first function
# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     # first while loop

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()

#         # simulate creating a 3d print from the design
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)

# # second function
# def show_completed_models(completed_models):
#     """ 
#     Show all the models that were printed.
#     """
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# # place out list being modifified by the function outside of our fucntion blocks
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = [] # the list we're modifying

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# # ---TRY IT YOURSELF-------------------
# # 8-9 MAGICIANS

# magicians = ['apollo robbins', 'dynamo', 'shin lim']

# def show_magicians(magicians):
#     for magician in magicians:
#         print(f"Tonight's magician is {magician.title()}!")
#         print("(ﾉ>ω<)ﾉ :｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆")

# show_magicians(magicians)


# # 8-10 GREAT MAGICIANS-----------------

# def make_great(good_magicians, greantness):
#     """
#     display good magicians list
#     move them to great musicians list
#     """

#     while good_magicians:
#         list_of_magicians = good_magicians.pop()

#         # simulate creating a 3d print from the design
#         print(f"{list_of_magicians.title()} if good now, but let's make them great!")
#         greantness.append(list_of_magicians)

# def show_make_great(greantness):
#     """ 
#     Show all the models that were printed.
#     """
#     print("\nWhat makes them great you ask? It's the word, great.")
#     for magician in greantness:
#         print(f"The GREAT {magician.title()} is here to do magic!")

# good_magicians = ['hoodini', 'ranbini', 'stu']
# greantness = [] 

# make_great(good_magicians, greantness)
# show_make_great(greantness)

# # 8-11 -----------MESSAGES------------

# # for the first function, list are above the code blocks to be referenced

# print("===TEXT MESSAGES===")

# def show_messages(messages):
#     """print text messages"""
#     for message in messages:
#         print(message)

# def send_messages(messages, sent_messages):
#     while messages:
#         message = messages.pop()
#         print(message)
#         sent_messages.append(message)
#     print("===LISTS===")

# messages = ['hi', 'how are you?', 'hey there']
# sent_messages = []

# messages.append('hows it going')
# messages.append('whats up')

# # send_messages(messages, sent_messages) # will append original list
# send_messages(messages[:], sent_messages) # uncomment to make a copy of the list
# print(messages)
# print(sent_messages)
# # print(show_messages(messages))

# # ------------------------------------

# christmas wish list (made this one up)

# # def show_wish_list(wish_list):
# #     """..."""
# #     print("\nWish list items:")
# #     for item in wish_list:
# #         print(item.title())
# # print(show_wish_list(wish_list))

# def christmas_list(wish_list, purchased):
#     """  move wish list to purchased list """
#     print("======>My Xmas wish list:")
#     while wish_list:
#         want = wish_list.pop()
#         print(want.title())
#         purchased.append(want)

# def recently_purchased(purchased):
#     """ show what you bought """
#     print(f"======> I recently bought:")
#     for purchase in purchased:
#         print(purchase.title())

# wish_list = ['laptop', 'apple watch', 'book', 'sweater']
# purchased = []
# gifts = []

# christmas_list(wish_list, purchased)
# recently_purchased(purchased)

# print(wish_list)
# print(purchased)

# # ------------------------------------

# # pizza toppings
# def make_pizza(*toppings):
#     "print the list of toppings that have been requested."
#     print(toppings)

# make_pizza('pep', 'cheese', 'mushrooms', 'onion', 'garlic')

# # replace the print statement with a loop!
# def make_pizza(size, *toppings):
#     """summarize the pizza we are about to make"""
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"  - {topping}")

# make_pizza(16, 'pep', 'cheese', 'mushroms')
# make_pizza('pep')

# # ---using arbitrary keyword arguments---
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing what we know about a user"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

# # ----TRY IT YOURSELF-----------------

# # 8-12 SANDWICHES

# def make_sandwich(bread, *toppings):
#     print("Make a sandwich with the following ingredients:")
#     for topping in toppings:
#         print(f" -- {topping.title()}")
#     print(f"... on deliciously toasted {bread.title()} bread!")

# make_sandwich('whole wheat', 'egg', 'mayo', 'bacon', 'onion', 'garlic')
# make_sandwich('white', 'mustard', 'turkey')
# make_sandwich('crusty country', 'jam', 'peanut butter')

# # refactored with *args

# def sandwich_ingredients(*args):
#     """print summary of sandwich ingredients"""
#     print(f"These are the sandwich ingredients:")
#     for arg in args:
        
#         print(f"- {arg}")

# sandwich_ingredients("\n")
# sandwich_ingredients('chesse', 'bacon', 'salad')

# # ---------------------------------------

# # 8-13 User Profile
# # build a profile for yourself
# def build_profile(first, last, location, hobby, **user_info):
#     """Build a dictionary containing what we know about a yourself"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     profile['location'] = location
#     profile['hobby'] = hobby
#     for key, value in user_info.items():
#         profile[key] = value
#         print(f"Here's your profile {first.capitalize()} {last.capitalize()}! Thanks for submitting.")
    
#     return profile

# user_profile = build_profile('leimomi', 'bong', 'honolulu', 'cooking', fav_food='cheese')
# print(user_profile)


# # 8-14 cars----------------------------


# def make_car(make, model, **other):
#     """build dictionary containing car info"""

#     car_details = {}
#     car_details['make'] = make
#     car_details['model'] = model
    
#     for key, value in other.items():
#         car_details['key'] = value
#     return car_details

# # we use a new variable to call the function 'new_car"
# new_car1 = make_car('tokyota', 'rav4', year='1998', tow_package=False)
# new_car2 = make_car('honda', 'element', year='2011', color='silver')

# print(f"You own two cars. They're both old. Here are you cars below:")
# print(f"{new_car1} {new_car2}")


# # ------------------------------------

# # another way of writing the program above
# # you don't need to define the dictionary inside of the fucntion ** indicate it will create one

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('lei', 'bong', age='33', hobby='swimming')
# print(user_profile)

