"""
# general syntax of function follows

def functionName(parameters):
    statements
    return (expression)

The expression will be returned.

You can write functions that return a value by calling the function

You can also write functions that just do something, and does not return a value

def functionName():
    output(statements)

It's good practice to call your functions at the top of the file and call them later in the code.

functionName(argument)

You can call a function by using the function name, followed by the the values you would like to pass into parameters.


"""
name = "uchenna"

def modify_name():
    name = 'emily'
    name_reversed = ''

    for letter in range(len(name), 0, -1):
        name_reversed += f'{name[letter -1]}'
    
    print(name_reversed)
modify_name()
print('-'*79)

def shout_name(persons_name):

    shout = persons_name.upper()
    return shout

function_result = shout_name("Bob")
print(function_result)

def whisper_name(person_name):
    whisper = person_name.lower()
    print(whisper)

output_function = whisper_name("JACKSON")
print(output_function) # This returned None because there is no return value in the function

# You can call a function and print out the code in a single line statement
print(f"I have been told that my name is {shout_name('Dwayne the rock johnson')}")


# Using functions make your code procedual instead of sequential.

# Benefits
# Make code reusable
# Functions make error checking and validation easier, each function as a module can be tested independantly.
# Functions divide code into manageable chunks - easier to understand and troubleshoot.

# Function scope
# Functions can call variables that are outside the function, but the rest of the code cannot call variables that are defined inside the function.
print("-"*79)

def join_name(first, last):

    full_name = f"{first} {last}"
    return full_name

first_name = "Uchenna"
last_name = "Attah"

output_full_name = join_name(first_name, last_name)
print(output_full_name)
print(f"My name is {join_name(first_name, last_name)}") # using function call within a single line statement.

print("-"*79)


def display_your_location(area):

    full_sentence = f"{sentence} {area}"
    return full_sentence

location = "London" # using values outside of the function as values/args
sentence = "lives in" # using values outside of the function as values/args
area = "Manchester" # using values outside of the function as values/args

user_location = display_your_location(area)
print(user_location)
print(f"This person {display_your_location(location)}") # using function call within a single line statement.

print("-"*79)

def display_stats():

    user_dialogue = "Hmph! "
    damage = 55
    stats = {
        "name": '',
        "weapon": '',
        "damage": damage,
        "colour": '',
    }

    return stats

try:
    print(user_dialogue, display_stats()) # variables defined in a function cannot be called externally!
except NameError:
    print("This value cannot be read!")

# Default values
# Default values can be assigend to the parameteres of a function using "<param>=<default_value>".
def generate_person(first="john", last="doe", age="25"):

    person = {
        "firstname": first,
        "lastname": last,
        "age": age,
    }

    return person

first_person = generate_person()
print(first_person) # default values were assigned
print(generate_person("jane", "doe", 22)) # when all values are input

first_name = "Harry"
last_name = "Kane"
print(generate_person(first_name, last_name))# when only some values are used i.e. age

print('-'*79)

# We can also call the function keyword arguments so that the order in which we write the arguments does not matter

# Using hardcoded values by using variables
mandolorian_first_name = "Din"
mandolorian_last_name = "Jarin"
second_person = generate_person(age= 40, last= mandolorian_last_name, first= mandolorian_first_name)
print(second_person)

# using hardcoded values where order does not matter
third_person = generate_person(last= "Johson", age= 51, first= "Dwayne")
print(third_person)

# Always specify the names of the other params or else it will fail
fourth_person = generate_person() # "paul", age= 51, "Rudd" - This order will throw a SyntaxError
print(fourth_person)
