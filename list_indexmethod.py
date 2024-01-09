list_of_letters = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ]
    
is_found = False

letter_to_find = 'a'
found_row = ''
letter_index = ''

while (not is_found):

    # loop through each row in 2d loop
    for i, row in enumerate(list_of_letters):
        
        # look for this character in each row
        if letter_to_find in row:
            found_row = i # obtain the index of the row the letter has been found
            letter_index = row.index(letter_to_find) # obtain the index for the letter in the established row
            is_found = True
    else:
        print('Loop has been stopped as we cannot find that letter')
        #is_found = True

# use the indexes found in the loop and use to print in this variable
letter = list_of_letters[found_row][letter_index]
print(f"'{letter}' can be found using these indexes: [{found_row}][{letter_index}]")
