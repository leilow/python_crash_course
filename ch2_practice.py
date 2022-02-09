# chapter 2 exercises - I should label the exercises!
# writing a personal message using a variable and assignnig it a value
n = "leimomi"
print(f"Hello, {n.title()}! Would you like to go to lunch today?")

# name cases: lower case, upper case, title case
name = "roger bradley Bong"
print(f"{name.lower()}\n{name.upper()}\n{name.title()}") # should print three times in different cases

# famous quote part 1 and 2
famous_person = "albert einstein"
quote = "A person who never made a mistake never tried anything new."
message = f'{famous_person.title()} once said, "{quote}"'
print(message)

# striping away unnecessary whitespaces
my_name = ' LEIMOMI BONG '
i'm not sure this one worked??
print(my_name)
# print(my_name.lstrip())
# print(my_name.rstrip())
# print(my_name.strip())

# simple operators
# everthing should equal to the number 8
a = 4+4
b = 10-2
c = 2*4
d = 16/2
print(a,b,c,d)

#using integers and variables to show my favorite number
n = 8
message =f"My favorite number is {n}, duh."
print(message)

# Zen of Python by Tim Peters
import this