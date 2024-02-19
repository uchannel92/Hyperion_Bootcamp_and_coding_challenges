# --- Define base class and create 2 subclasses --- #

class Mammal:

    def __init__(self, name:str) -> None: # Annotations included for documentation
        self.name = name

    
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def eat(self):
        return f"*crunch* *crunch*.. {self.name} is eating."


    def sleep(self):
        return f"Zzzz... {self.name} is sleeping."
    

    def walk(self):
        return f"*tap tap tap*... {self.name} is walking."


# passing Mamal into class Human means Human will inherit all methods and attributes from class Mammal
class Human(Mammal):

    def walk(self):
        return f"* tap tap tap tap tap tap *.. {self.name} is walking fast!"
    

    def eat(self):
        return f"{self.name} just ate a burger"
    

class Dolphin(Mammal):

    def swim(self):
        return f"{self.name} can swim so fast and far!"
    

    def eat(self):
        return f"{self.name} just ate a clown fish :'("
    

# create instances of Human and Doplhin classes
person = Human("John", 99)
fish = Dolphin("Daisy", 15)

print(person.walk())
print(fish.eat())


# --- Multiple inheritence --- #

class Vehicle:

    def __init__(self, brand) -> None:
        self.brand = brand


    def drive(self):
        return self.brand, "is driving.."
    

class Electric:

    def __init__(self) -> None:
        pass


    def charge(self):
        return "Charging the electric vehicle..."
    
 
# HybridCar will inherit from both Vehicle and Electric car classes
class HybridCar(Vehicle, Electric):

    def __init__(self, brand, fuel_type) -> None:
        # you can do either
        # super().__init__(brand)

        # you can do either
        Vehicle.__init__(self, brand) 
        Electric.__init__(self)

        self.fuel_type = fuel_type

    # Method overriding as drive is already called in class Vehicle
    def drive(self):
        return f"{self.brand} hums away silently with it's {self.fuel_type} fuel"
    

# Create an instance
car = HybridCar("Tesla", "electric")

# Use methods from Vehicle
print(car.drive())

# Use methods Electric
print(car.charge())