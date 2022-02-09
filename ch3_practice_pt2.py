# Chapter_3B_practice
# started a new project for the second half of the chapter
# these problems were focused on sorting

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(f"\nHere's the original list of cars:")
print(cars)

print(f"\nHere's the sorted list of cars:")
print(sorted(cars))

cars.sort(reverse=True)
print(f"\nHere's the reverse list of cars:")
print(cars)

print(f"\nHere's the original list of cars:")
print(cars)

print(f"\nHere's the list in reverse:")
cars.reverse()
print(cars)

#3.8 Seeing the world - practicing how to sort and resort lists
travels = ["indonesia", "amsterdam", 'berlin', 'korea','italy']
print(f"Here's the list of original order of place to travel:")
print(travels)
print(f"Here's the list of sorted order of places to travel:")
print(sorted(travels))
# print(travels)
print(f"Here's the list of reverse order of places to travel:")
travels.reverse()
print(travels)
travels.reverse()
print(f"Here's the list of resorted order (aka original) of places to travel:")
print(travels)
print(f"Here's the list in alphabetical order of places to travel:")
print(sorted(travels))
travels.sort(reverse=True)
print(f"Here's the list in reverse alphabetical order of places to travel:")
print(travels)

# 3.4 guest list and finding the length of a string

invites = ['harry potter', 'ada lovelace', 'grace hopper', 'mariah carey', 'roger bong']
len = len(invites) #using len as a class will allow us to easily change the list and count and still print it out correctly
# print(len(invites))
print(f"Number of people attending tomorrow's dinner: {len}.")

# 3.10 use every function you learned in this chapter
# list
# pop
# del / remove
# sort /sort(reverse=True)
# append
# len

languages = ['french', 'japanese', 'german', 'english']
countries = ['france', 'japan', 'germany', 'america']
cities = ['paris', 'tokyo', 'berlin', 'honolulu']

print(f"\nMy name is Lei. I'm originally from {cities[3].title()} where we speak {languages[3].title()} mostly.")

countries.sort() #sort these alphabetically... because we can lol
del countries[0] #delete my home country, because we won't be needing it

print(f"I'd like to do more traveling. My top three countries to visit are {countries[0].title()}, {countries[1].title()}, and {countries[2].title()}.")

popped_cities = cities.pop()
# print(popped_cities) #we took out our favorite city after it had been sorted alphabetically
print(f"I'm most excited to experience {cities[-2].title()}, {countries[2].title()}! I studied {languages[1].title()} for two years in college.")

# # this block only works when others are not present... have to sort it out?
# languages.sort(reverse=True)
# print(f"Oddly enough, my least favorite language is {languages[-1].title()}, because it's so difficult to read. But it's universal!")
# len_languages = len(languages)
# print(f"In total I can speak {len_languages}, including {languages[1].title()} and {languages[2].title()}. My grandparents spoke those languages.")

cities.append('Bangkok')
languages.append('Thai') #you'd know these new elements have a position of -1 since they were added to the end
print(f"Come to think of it, I'd also love to visit {cities[-1].title()} too! I listen to a lot of music in {languages[-1].title()}!\n")
# print(len(languages)) # just testing out length, I'm still not 100% sure how to use it in all situations.