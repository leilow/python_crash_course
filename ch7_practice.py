# # -------USER INPUT AND WHILE LOOPS---

message = input("\nTell me something, and i'll repeat it back to you: ")
print(message)
print("   ")

# # store your prompt in a vairable, and pass through input()

prompt = "We can personalize a message for you.\n"
prompt += "What is your name?\n\t---->"

name = input(prompt)
print(f"Hello, {name}!")
print("   ")

# # using and int() to accept numerical input

height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")
    print("   ")

# # modulo operator

number = input("\nEnter a number. I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {str(number)} is even.")
else:
    print(f"The number is {str(number)} is odd.")
print("   ")

# # Accepting Input---------------------

# # 7-1 Rental car

message = input("What kind of rental care are you interested in? ")
print(f"Let me see what kind of {message.capitalize()}s we have available!")
print("   ")

# # 7-2 Restaurant Seating
message = input("How many people will be dining with you this evening? ")
message = int(message)

if message >= 8:
    print(f"Thanks. The wait for your party will be 30 minutes.")
else:
    print(f"Great. We've got a table ready for you. Right this way!")

# # 7-3 Multiples of Ten

message = input("\nTell me a number. Any number! ")
message = int(message)
if message % 10 == 0:
    print("This number is a multiple of 10!")
else:
    print("This number is NOT a multiple of 10.")
print("   ")

# # ----------WHILE LOOP----------------
# parrot.py program

prompt = "\nTell me something, and I'll repeat it back to you!"
prompt += "\nEnter 'quit' to end the program. "

active = True

message = ""

while message != 'quit':
    message = str(input(prompt).lower())
    print(f'\"{message.capitalize()}", said the parrot! "{message.capitalize()}!"')
    if message == 'quit':
        print("Thanks for playing!")
        active = False
        break


# # ------BREAK AND CONTINUE------------

# # using a break to exit a loop

prompt = "\nEnter the name of a city you've visited:  "
prompt += "\n(Enter 'quit' when you are finished.)  "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print("Thanks for playing.")
        print("\n")
        break
    else:
        print(f"I've never been to that {message.title()}! I'd like to go someday.")
        

# # continue in a loop
# # print odd numbers

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# # print even numbers
# old_number = 0
# while old_number < 20:
#     old_number += 2
#     if old_number % 3 == 0:
#         continue
#     print(old_number)

# # count by 5 through 55
# fives = 0
# while fives < 55:
#     fives += 5
#     if fives % 5 == 1:
#         continue
#     print(fives)

# # ----7-4 PIZZA TOPPINGS-----------------

# # write a loop that ask for toppings until quit
# # after each topping say, you'll add it to their pizza

prompt = "\n\tWhat kind of toppings would you like?"
prompt += "\n\tEnter here, and enter 'quit' when you're finished. "

active = True

while active:
    print(f"\n-------")
    topping = input(prompt)
    if topping == 'quit':
        print(f"\n-------")
        print(f"\tThanks for your order. Your pizza be out soon.\n")
        break
    else:
        print(f"\tYum, adding {topping.title()} to your pizza.")

# # ------7-5 MOVIE TICKETS-----------------

# a theater that chargers different prices by age
# 3 < FREE
# 3-12... $10
# 12 > $15
# ask their age, and tell them the cost of the ticket

age = input("\tHow old are you?  ")
quantity = input("\tHow many tickets do you want to buy?  ")

age = int(age)
quantity = int(quantity)
# print(quantity)

price0 = 'free'
price1 = 10
price2 = 15

if age <= 3:
    print(f"---That's {quantity} tickets at {price0} each.")
if age >= 4 and age <= 12:
    print(f"---That's {quantity} tickets at ${price1} each.")
if age > 12:
    print(f"---That's {quantity} tickets at ${price2} each.")
print(f"---Enjoy your movie!\n")

# ------------------------------------
# moving items form one list to another


# a list of users that need to be verified
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user untill there arent any more to confirm
print(f"CONFIRMING {unconfirmed_users} NOW! PLEASE WAIT.")
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"\tStill verifying users: {current_user.title()}")
    confirmed_users.append(current_user)
print("-----------")

for user in confirmed_users:
    print(f"\tNow confirmed users: {user.title()}")


# # ------------------------------------
# # removing all instance of a spceific value from a list

# pets = ['dog', 'dog', 'cat', 'cat', 'goldfish', 'rabbit', 'hamster']
# print(pets)

# while 'dog' in pets:
#     pets.remove('dog')

# print(pets)


# ---MAKE A POLL----------------------
# fill a dict with user input

# empty dictionary
responses = {}

# a flag
polling_active = True

# prompt that ask for name using a while loop
while polling_active:
    name = input("\nWhat's you name?  ")
    response = input("Which mountain would you like to climb somedays?  ")

# store response in a dictionary
    responses[name] = response
# find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no)  ")
    if repeat == 'no':
        polling_active = False

# polling is complete
print("\n===POLL RESULTS===")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# ----------7.8 DELI------------------

sandwich_orders = ['turkey', 'ham', 'veggie', 'chicken', 'grilled cheese', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print(f"\nLooks like the deli ran out of pastrami. Can I get you something else?")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"<3 We've got a lot of other options including:")
for orders in sandwich_orders:
    print(f"\t{orders.title()}")

prompt = input("What item off the list would you like to get?  ")
print(f"We'll make your {prompt.title()} sandwich right away. Thanks for waiting!\n")

# Looping a list we just created
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(making_sandwich)
print("=======")

# for order in finished_sandwiches:
#     print(f"Your {order.title()} sandwich is ready! Enjoy.")

# ----------7.10 DREAM VACAY----------

responses = {}

polling_active = True

while polling_active:
    prompt1 = input("\nWhere is your dream vacation desination?  ")
    prompt2 = input("\nWho would you like to travel with?  ")
    responses[prompt1] = prompt2 
    #this line is one response—first response is the key, second response is the value

    repeat = input("\nAnywhere else you want to go? (yes/no)  ")
    repeat = str(repeat.lower()) #this makes sure any case of 'no' will be False
    if repeat == 'no':
        polling_active = False
        break

print(f"\n=====YOUR DREAM VACATION=====")
for place, buddy in responses.items():
    print(f"Your dream vacation is {place.title()} with your best bud {buddy.title()}!")