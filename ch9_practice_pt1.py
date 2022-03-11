# # ====CLASSES=========================

# create a class for dog
# class is like a blue print

class Dog():
    """A simple model of a dog"""

    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name.title()} is now sitting.")
        
    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name.title()} rolled over!")

my_dog = Dog('willi', 6) 
your_dog = Dog('fuzzy', 3)


# we can use dot notation to reference attributes
# we can use dot notation to call methods too
# this is how we instantiate an object

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit() 

print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()

# # ------------------------------------

# 9- restraurant class
class Restraurant():
    """a simple restraurant class"""
    def __init__(self, restraurant_name, cuisine_type):
        self.restraurant_name = restraurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restraurant(self):
        print(f"The restraurant is called {self.restraurant_name}.")
        print(f"The cuistine type is {self.cuisine_type}.")

    def open_restraurant(self):
        """describe restuarant"""
        print(f"The restraurant {self.restraurant_name} is open.")

# give the class a variable in order to use it in a print statement

restraurant = Restraurant('Flavor Town', 'Chinese')

# next we're going to use this variable to call the class
print(f"Restraurant name: {restraurant.restraurant_name}.")
print(f"Restraurant cuisine: {restraurant.cuisine_type}.")

# instantiate the class using dot notation to call the methods above
restraurant.describe_restraurant()
restraurant.open_restraurant()
print("\n=====")


# # ---9.2 create 3 restaurants---------
# # --snip the class restraurant above--

restraurant = Restraurant('Le Vin Yard', 'French')
print(f"Restraurant name: {restraurant.restraurant_name}")
print(f"Cuisine Type: {restraurant.cuisine_type}")
restraurant.describe_restraurant()
restraurant.open_restraurant()

print("\n=====")

restraurant = Restraurant('Pig & The Lady', 'Vietnamese')
print(f"Restraurant name: {restraurant.restraurant_name}")
print(f"Cuisine Type: {restraurant.cuisine_type}")
restraurant.describe_restraurant()
restraurant.open_restraurant()

print("\n=====")

restraurant = Restraurant('Meriman\'s', 'American')
print(f"Restraurant name: {restraurant.restraurant_name}")
print(f"Cuisine Type: {restraurant.cuisine_type}")
restraurant.describe_restraurant()
restraurant.open_restraurant()

# # ---------------9.3------------------

class user():
    """a simple class for users"""

    def __init__(self, first, last, age, city):
        # define these arguments in the function parameters
        self.first = first
        self.last = last
        self.age = age
        self.city = city
    
    def describe_user(self):
        print(f"{self.first} {self.last} is a {self.age} year old member currently living in {self.city}!")

    def greet_user(self):
        print(f"Welcome, {self.first} {self.last}! Happy you're here.")

print(f"=====")
user = user('Helen', 'Howard', 33, 'Atlanta')
user.describe_user()
user.greet_user()


# # --------------------------------------

class Cars():
    """A simple car class"""

    def __init__ (self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make}, {self.model}, {str(self.year)}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer} on it.")

    # you can change an attribute by adding a new method
    def update_odometer(self, mileage):
        """set the odomete value to the give value.
        Reject the change if it tries to roll the odometer back.
        """
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print(f"You can't roll back an odometer!")

    # if you'd like to increment the milage
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer += miles

# ----------
new_car = Cars('Mazda', 'iTouring', 206)
print(new_car.get_descriptive_name())
# print(new_car.read_odometer())

# you can change the attribute using an instance
new_car.odometer = 25

#update odometer method
new_car.update_odometer(4)
print(new_car.read_odometer())

# ----------
user_car = Cars('Nissan', 'Leaf', 208)
print(user_car.get_descriptive_name())
user_car.update_odometer(25000)
print(user_car.read_odometer())
user_car.increment_odometer(00)
print(user_car.read_odometer())

# # ------------------------------------
# # 9-4 TIY------------------------------

class Restraurant():
    """a simple restraurant class"""
    def __init__(self, restraurant_name, cuisine_type):
        self.restraurant_name = restraurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restraurant(self):
        return f"The restraurant is called {self.restraurant_name}.\nThe cuistine type is {self.cuisine_type}.\nToday they served {self.number_served} customers."
        
    def open_restraurant(self):
        """describe restuarant"""
        return f"The restraurant {self.restraurant_name} is open."

    def set_number_served(self, guests):
        """set the number of customers"""
        self.number_served = guests
        return f"The maximum number {self.restraurant_name} can serve in a day is {self.set_number_served}." 

    def increment_served(self, increment):
        """increment number of customers"""
        self.number_served += increment


print(f"\n=====")
restraurant = Restraurant('Fete', 'French')
# print(restraurant.describe_restraurant())
restraurant.set_number_served(200)
print(restraurant.describe_restraurant())

print(f"\n=====")
restraurant.increment_served(00)
print(restraurant.describe_restraurant())

# # ------------------------------------
 
class Cars():
    """A simple car class"""

    def __init__ (self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make}, {self.model}, {str(self.year)}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer} on it.")

    # you can change an attribute by adding a new method
    def update_odometer(self, mileage):
        """set the odomete value to the give value.
        Reject the change if it tries to roll the odometer back.
        """
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print(f"You can't roll back an odometer!")

    # if you'd like to increment the milage
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        return f"This car has a {self.battery_size}-kWh battery."
    
    def get_battery_range(self):
        """Print a statement about the battery_range this battery provides"""
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 150:
            battery_range = 315
        return f"This car can go {battery_range} miles on a full charge."

    def upgrade_battery(self):
        """check battery and set capacity to 100"""
        if self.battery_size != 100:
            self.battery_size = 150
            return f"Upgrading battery now."

class ElectricCar(Cars): # child class
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # self.battery_size = 70 # a new attribute for electric car child class
        self.battery = Battery() # Battery is now a class we can create a new instance from

    # modifying a method of the parent class
    def fill_gas_tank(self):
           """Electric cars don't have gas tanks."""
           return f"This car doesn't need a gas tank!"

# # using the child class to make instances of Cars
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# # print(my_tesla.describe_battery())
# print(my_tesla.fill_gas_tank())

# # now that we have a battery class, we have to 1st work through it
# my_tesla.battery.describe_battery() 
# print(my_tesla.battery.describe_battery())

# # calling a new method from our battery battery_range 
my_tesla = ElectricCar('Tesla', 'Model S', 2019)
print(f"===================")
print(my_tesla.battery.describe_battery())
print(my_tesla.battery.get_battery_range())
print(my_tesla.battery.upgrade_battery())
print(my_tesla.battery.get_battery_range())


# # ------------------------------------

# # 9-6 TIY

class Restraurant():
    """a simple restraurant class"""
    def __init__(self, restraurant_name, cuisine_type):
        self.restraurant_name = restraurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restraurant(self):
        return f"The restraurant is called {self.restraurant_name}.\nThe cuistine type is {self.cuisine_type}.\nToday they served {self.number_served} customers."
        
    def open_restraurant(self):
        """describe restuarant"""
        return f"The restraurant {self.restraurant_name} is open."

class IceCreamStand(Restraurant):

    def __init__(self, restraurant_name, cuisine_type, flavors):
        """Initialize ice cream stand"""
        super().__init__(restraurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        """display ice cream flavors"""
        print(f"The flavors are:")
        for flavor in self.flavors:
            print(f"{flavor}")

ice_cream = IceCreamStand('Coldstone', 'Ice Cream', ['vanilla', 'chocolate', 'strawberry'])
print(ice_cream.describe_restraurant())
ice_cream.display_flavors()

# # ------------------------------------

# # 9.7 TIY

class user():
    """a simple class for users"""

    def __init__(self, first, last, age, city):
        # define these arguments in the function parameters
        self.first = first
        self.last = last
        self.age = age
        self.city = city
    
    def describe_user(self):
        print(f"{self.first} {self.last} is a {self.age} year old member currently living in {self.city}!")

    def greet_user(self):
        print(f"Welcome, {self.first} {self.last}! Happy you're here.")
 
# creating a separate class for privileges
class Privileges():
    """a simple privileges class"""
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        """display privileges"""
        print(f"Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# creating a specific kind of user, a new user
class Admin(user):
    """a special admin class"""

    def __init__(self, first, last, age, city, privileges):
        """initialize admin class and attributes"""
        super().__init__(first, last, age, city)
        self.first = first
        self.last = last
        self.age = age
        self.city = city
        self.privileges = Privileges(privileges)
    


admind1 = Admin('Sera', 'Tosin', 28, 'NYC', ['can post', 'can delete post', 'can ban users'])
admind1.privileges.show_privileges()
