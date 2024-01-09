# String 2D list
# pet store

cats = ['cat1', 'cat2']
dogs = ['dog1', 'dog2', 'dog3', 'dog4']
birds = ['bird1', 'bird2', 'bird3', 'bird4', 'bird5', 'bird6']

# 2d list of animals
animals = [cats, dogs, birds]
print(animals)

# loop through nested list
for animal in (animals):
    print(animal)
    for idx, animal_group in enumerate(animal): # use enumerate to loop through the inner loop and obtain each index
        print(f"\t{idx} - {animal_group}")

# List comprehension examples
# example 1 - convert name to upper case
rand_name = "eren jaeger"
converted_name = [letter.upper() for letter in rand_name]
print("".join(converted_name))


# example 2 - concatonate strings to a list
# lets say you want to say hello to everyone in a list
list_of_names = ["craig", "jake", "emma", "lilly"]
greeting = "Hello"
greetings = [f"{greeting} {name}" for name in list_of_names]
print(greetings)

# use the above example to mail merge an email that is sent to multiple users! a way to automate a mundane task.

# example 3 - conditional statements
sentence = "my name is uchenna attah, and i am thirty one years of age learning Python at Hyperion Software engineering bootcamp"

# first add in your for condition
# then add your conditional statement 
# [result/expression | for loop | condition]
words_greater_than_three = [word for word in sentence.split(" ") if len(word) > 3]
print(words_greater_than_three)
print('-'*79)

# normal for loop way tp do this
# we used split at the end of sentence so after each space, word will form a word and not iterate each letter individually
# remove split method and use a print sentence to see the difference
words_greater_than_three_old_for = []
sentence_ = "my name is uchenna attah, and i am thirty one years of age learning Python at Hyperion Software engineering bootcamp"
for word in sentence.split(" "):
    if len(word) > 3:
        print(word)
        words_greater_than_three_old_for.append(word)
print(words_greater_than_three_old_for)

# Both methods do the same thing, however list comprehension make it cleaner to write in one line.


# value-true if condtion else value-false
rand_word = "extraordinary"

is_valid = "Sucess" if rand_word == "extraordinary" else "Fail"
print(is_valid)