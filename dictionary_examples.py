# String 2D list
# pet store

cats = ['cat1', 'cat2']
dogs = ['dog1', 'dog2', 'dog3', 'dog4']
birds = ['bird1', 'bird2', 'bird3', 'bird4', 'bird5', 'bird6']

# dictionary snippet
dict_of_animals = {
    "cats": cats, "dogs": dogs, "birds": birds,
    }

print(dict_of_animals)
print(dict_of_animals['dogs'][2]) # for nested lists in a dict, you need to access the index! not the key!