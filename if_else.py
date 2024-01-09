import string

letters = list(string.ascii_lowercase)
print(letters) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    #  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letter_to_find = '0' # A string that is not in the list.

if letter_to_find in letters:
    for index, letter in enumerate(letters):
        if letter_to_find == letter:
            print(f"{letter_to_find} is at position {index}")
            break # As soon as letter is found break loop
else:
    print("Item is not in the list of letters")

# Research how to use SQL with Python
        # SQL lite with Python
        # How to use a databse with Python
# == when working with variables
# in when working with lists
    

# a list of football players
football_squad = [
    {"vdv": 31}, {"romero": 34}, {"vicario": 32}, {"emerson": 38}, {"gil": 36},
    {"richarlison": 37}, {"kulusevski": 28}, {"solomon": 38}, {"skipp": 31}, {"johnson": 31},
    ]
    
player_found = False
footballer_to_find = "simon"
found_dict = ''
found_dict_index = ''

for list_index, squad_dict in enumerate(football_squad):
    
    if footballer_to_find in squad_dict:
        found_dict = football_squad[list_index][footballer_to_find]
        found_dict_index = list_index
        player_found = True
        break
    else:
        continue
    
if player_found == True:
    football_squad.pop(found_dict_index)
    print(football_squad)
elif player_found == False:
    print(f"Footballer '{footballer_to_find}' not found")