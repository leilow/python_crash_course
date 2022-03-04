#---------CHAPTER 5 CONDITIONALS--------

# using the equality operator to check if two statement are equal

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for inequality

topping = ['pepporoni', 'cheese', 'basil', 'anchovies']

if topping != 'anchovies':
    print("hold the anchovies")

# checking whether a value is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post response if you wish.")

# 5-1 conditional test

# write a series of conditional test

car = 'subaru'
print("is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs the car an Audi? I predict False.")
print(car == 'audi')

print("\nIs car equal to 'bmw'?")
print(car == 'bmw')


order = 'desk'
print(order == 'lamp')
print(order == 'table')
print(order == 'nightstance')
print(order == 'stool')
print(order == 'chair')
print(order == 'cups')
print(order == 'basket')
print(order == 'blanket')
print(order == 'pillow')
print(order == 'desk')

if order == 'desk':
    print(f"The customer ordered a new desk!")

# test for equality and inequality with strings

mycat = 'orange'

if mycat == 'orange':
    print("Hey, that's my cat.")

theircat = 'white'

if theircat == 'brown':
    print("Hey, that's their cat.")
else:
    print("Woah, that's not their car. Their cat's brown!")


# using upper or lower case to run a test

cats = ['MARY', 'KITTY', 'COCO']

for cat in cats:
    if cat == 'KITTY':
        print(cat.lower())
    else:
        print('He spell his cats name in upper case.')

# running numerical tests
# a test checking a users age

age = 35

if age == 42:
    print("42? You don't look a day over 30.")
if age >= 43:
    print("You don't look a day over 40!")
if age <= 25:
    print("You have a whole life ahead of you. Wear sunscreen!")
if age != 18:
    print("You're not old enough to be here!")

# a test using keyword and keyword or
if age >= 10 or age <= 10:
    print("You're not 10 years old.")
elif age == 10:
    print("You're 10 years old. Congrats.")

if age == 18 or age >= 18:
    print("You can legally have a drink. Cheers!")
if age >= 30 and age <= 40:
    print("You probably drink wine at your age.")
else:
    print("Who knows what you drink.")

# test whether an item is not in a list

history_students = ['kari', 'sean', 'nancy']
student = 'marie'

if student not in history_students:
    print(f"{student.title()} is not in history class.")

# # test whether an item is in a list

history_students = ['kari', 'sean', 'nancy']
if 'sean' in history_students:
    print(f"{history_students[1].title()} in class today.")

age = 16
if age >= 18:
	print("You are old enoug to vote.")
	print("Have you registered to vote yet?")
else:
    print("Sorry, you're too young to vote.")
    print("Please register as soon as you turn 19!")

# use an if-elif-else chain to determine a person's admission rate

age = 3

if age < 4:
    print("You admission is free.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# another expample that doesn't end in else
age = 100

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 30
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}. Thank you.")

# a example of when you want to act on every Truth statement

requested_toppings = ['onions', 'spinach']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
if 'onions' in requested_toppings:
    print("Adding onions.")
if 'onions' in requested_toppings:
    print("Adding spinach.")

print("\nFinished making your pizza!")                     

# 5-3 Alien Colors program 1

alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("He's green. 5 points.")
if 'yellow' in alien_color:
    print("He's yellow too. 5 points.")
if 'red' in alien_color:
    print("And red, wowzer! 5 points.")
if 'blue' in alien_color: # false, there's no blue in the list
    print("bye now.")

# 5-4 alien colors program 2

alien_color = 'green'

if alien_color == 'green':
    print("green, 5 points")
if alien_color != 'green':
    print("nope, 10 points")
else:
    print("thanks for playing")

# 5-5 alience colors program 3

alien_color = 'blue'

if alien_color == 'green':
    print("\nyou earned 5 points")
elif alien_color == 'yellow':
    print("\nyou earned 10 points")
elif alien_color == 'red':
    print("\nyou earned 15 points")
else:
    print("\nno points for you")

alien_color = ['orange', 'brown', 'white'] # # when you run colors not in the program,
#  it comes back 'no colors, no points' so the test is working

if 'green' in alien_color:
    print("you earned 5 points")
if 'yellow' in alien_color:
    print("you earned 10 points")
if 'red' in alien_color:
    print("you earned 15 points")
else:
    print("no color, no points")


# if elif else block
age = 101

if age <= 4:
    print(f"baby")
elif age <= 8:
    print(f"child")
elif age <= 13:
    print(f"teenager")
elif age <= 20:
    print(f"adult")
elif age <= 50:
    print(f"senior")
else:
    print("elder")

# favorite fruit: make a list and write statements that check for certain
# fruits in yoru

favorite_fruits = ['melon', 'grape', 'papaya']

if 'melon' in favorite_fruits:
    print("you really like melons")
if 'grape' in favorite_fruits:
    print("youre really like grapes")
if 'papaya' in favorite_fruits:
    print("you like papaya")

# practice code

requested_toppings = ['pep', 'cheese', 'onion']

for requested_toppings in requested_toppings:
    if requested_toppings == 'cheese':
        print(f"sorry we're out of cheese")
    else:
        print(f"adding {requested_toppings}")
print("pie is ready")

# multiple list

avail_toppings = ['olives', 'cheese', 'mushrooms']
request_toppings = ['fries', 'beats', 'pep']

for request_toppings in request_toppings:
    if request_toppings in avail_toppings:
        print(f"Adding {request_toppings}.")
    else:
        print(f"sorry, don't have {request_toppings}.")
print("your finished now")


for request_toppings in request_toppings:
    if request_toppings in avail_toppings:
        print(f"Adding {request_toppings}.")
    else:
        print(f"sorry, don't have {request_toppings}.")
print("your finished now")

# another exercise
my_name = 'leimomi bong'
my_birthday = 'july 21, 1988'
occupation = 'actress'
age = 25

print(f"Name: {my_name.title()}.")
print(f"Birthday: {my_birthday.title()}.")
print(f"Occupation: {occupation.title()}.")

print(f"{my_name.title()} is an {occupation.title()} who is {age} year old.")
print(f"Her brithday is on {my_birthday[:].title()}.")
print(f"She is an {occupation}!")

# 5.8  hello admin

users = ['ron', 'don', 'tod', 'mary', 'ann']
# new_users = ['jerry', 'kit', 'bob', 'sandy', 'roger', 'tod', 'mary']
# users = []

for user in users:
    if user != 'admin':
        print(f"Hello {user}!")
    elif user == 'admin':
        print("Welcome admin! Would you like to see the reports?")

# 5.9 No users and clearing the list

new_list_users = users.copy()
print(new_list_users)

new_list_users.clear()
print(new_list_users)

if new_list_users == []:
    print("We need to find some users.")

# 5.10
"""
program simulates how wesbites ensure each user has unique name
loop through users to see if user name already in use
comparison is not case sensitive 'JOHN' == john
"""

current_users = ['sQUare101', 'Triangle202', 'cIRcle303', 'star404', 'recTangle505']
new_users = []

for i in range(len(current_users)):
    current_users[i] = current_users[i].lower()
for i in range(len(new_users)):
    new_users[i] = new_users[i].lower()

# # an if statement that checks if both list are the same
# # my first solution...
# if current_users == new_users:
#     print("the lists are the same")
# if current_users != new_users:
#     print("the lists are different")

message = input("Enter a new user name: ")

def check_availability(name):
    for user in current_users:
        if user == name:
            print("user name is taken")
            return user == name
        elif user != name:
            print("user name is available")
            return user != name

print(check_availability(message))

# 5-11 Ordinal Numbers

"""
store 1-9 in a list
loop through the lsit
use if-elif-else inside loop to print proper ordinal endings

output: "1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th" on separate lines
"""

ord_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in ord_nums:
    if n == 1:
        print(f"{n}st")
    
    if n == 2:
        print(f"{n}nd")

    if n == 3:
        print(f"{n}rd")
    
    if n >= 4:
        print(f"{n}th")