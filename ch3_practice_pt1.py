# introduction to list
# a list goes between square brackets []. you can call on a list by using index.
bicycles = ['trek', 'redline', 'road', 'mountain']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# using individual values from a list
bicycles = ['trek', 'redline', 'road', 'mountain']
brands = ['candondale', 'kona', 'bianchi', 'orbea']
message =f"My first bicycle was a {bicycles[2].title()} bicycle made by {brands[2].title()}!"
print(message)

#3-1 names
names = 'nancy', 'roger', 'treyvon', 'aisha'
print(f'My friends name is {names[0].title()}.')
print(f'My friends name is {names[2].title()}.')
print(f'My friends name is {names[1].title()}.')
print(f'My friends name is {names[3].title()}.')

#3-2 greetings
neighbors = 'sean', 'becca', 'chaz', 'sarah'
message = f"You're the best neighbor ever, {neighbors[3].title()}!"
print(message)

neighbors = 'sean', 'becca', 'chaz', 'sarah'
print(f"You\'re the best neighbor ever, {neighbors[2].title()}!")

#3-3 your own list
travels = 'airlines', 'trains', 'busses', 'boats'
companies = 'delta', 'southwest', 'united', 'hawaiian'
print(f'My favorite way to travel is by {companies[1].title()} {travels[0].title()}.')
print(f'My least favorite way to travel is on {companies[0].title()} {travels[2].title()}. They\'re not very comfortable.')

# #modifying elements in a list
motorcycles = ['honda', 'suzuki', 'honda']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

adjectives = ['fat', 'fluffy', 'cute']
adjectives[2] = 'spicy'
# print(adjectives)
print(f'My cat is very sweet and {adjectives[2]}.')

inserting elements into a list
fruits = ['banana', 'apple', 'catalope','mango']
fruits.insert(0, 'papaya')
del fruits[1]
#removing an item using pop() method
popped_fruits = fruits.pop()
print(fruits)
print(popped_fruits)

# remove item from any position
fruits = ['apple', 'orange', 'mango', 'papaya', 'guava']
first_fruit = fruits.pop(2)
fruits.remove('orange')
print(f"The first fruit I ate as a kid was {first_fruit.title()}!")
print(fruits)

writing_items = ['pen', 'pencil', 'marker', 'crayon']
print(writing_items) #print to see the list before removing an element
cheap_items = 'pencil'
writing_items.remove(cheap_items)
print(writing_items) #print to see the list after removing the element
print(f"\nThe cheapest writing item you can buy is a {cheap_items.title()}, but they're not great.") #use the element you removed from the list

3-4 guest_list
if you could invite anyone alife/dead to dinner, who?
dinner_buds = ['prince kuhio', 'ada lovelace', 'grace hopper',] #original guest list

print(f"Hey gang! \n\tWould love it if all of you could join me for dinner.\n\tI have {dinner_buds[0].title()}, {dinner_buds[1].title()}, {dinner_buds[2].title()} on the guest list.")
print(f"\nHey dinner party, \n\tIt looks like not everyone will be ale to make it. \n\tUnfortunetly {dinner_buds[0].title()} has plans already. Inviting someone else!")

popped_dinner_buds = dinner_buds.pop(0) #got rid of the person who can't make the party
dinner_buds.append('harry potter') #added the new guest
# print(popped_dinner_buds) #used this line of code to check that PK was off the list
# print(dinner_buds) #used this line of code to add a new guest to the list

print(f"\nIt's me again,\n\tWe've got one more special guest joining us. \n\tHis name is {dinner_buds[2].title()}. He'll be bringing the drinks!\n")
print(f"\nHello friends,\n\tLooks like we have more room at the table, so I'm inviting a few more people.\n\tI think you're going to enjoy meeting them!\n")

dinner_buds.insert(0, 'lord byron')
dinner_buds.insert(2, 'annie hall')
dinner_buds.append('roger bong')
# print(dinner_buds) #used this function to see where the middle of my life was

print(f"Hey {dinner_buds[0].title()}! \nStill good for dinner? Can't wait!\n")
print(f"Hey {dinner_buds[1].title()}! \nDinner tomorrow, don't forget!\n")
print(f"Hey {dinner_buds[2].title()}! \nAny allergies? Checking for tomoorrow's dinner!\n")
print(f"Hey {dinner_buds[3].title()}! \nSee you tomorrow. Don't forget the salad!\n")
print(f"Hey {dinner_buds[0].title()}! \nWhat kind of drinks are you bringing? See you then.\n")
print(f"Hey {dinner_buds[0].title()}! \nHope you're still free tomorrow. Dinner's at 8!\n")

#3-7 shrinking the guest list
print(f"\nHey gang!\n\tTerrible news. Family emergency. Sorry this is last minute. \n\tDon't think I can host a big party, but can still have a few of you over.\n")
popped_dinner_buds = dinner_buds.pop()
popped_dinner_buds = dinner_buds.pop()
popped_dinner_buds = dinner_buds.pop()
popped_dinner_buds = dinner_buds.pop()
print(dinner_buds) #now we have two dinner guest

print(f"\nHey you two. \n\tThanks for being so flexible about the dinner I planned.\n\tIt'll be the three of us, myself, {dinner_buds[0].title()}, and {dinner_buds[1].title()}!")
del dinner_buds[0]
del dinner_buds[0]
print(dinner_buds) #now we have noone coming over for dinner