"""
# example output:

# sum all number in each column

[1, 2, 3]
[445, 5, 20]
[20, 20, 60]

sum =  461, 27, 83

get the # of rows and # of columns from each user
"""

# create the grid
num_of_row = int(input("Enter no of rows: "))
num_of_columns = int(input("Enter no of columns: "))

user_grid = [[0 for col in range(num_of_columns)]for row in range(num_of_row)]

print(user_grid)
for x in user_grid:
    print(x)


# create a row and add values in each
for row in range(len(user_grid)):

    for column in range(len(user_grid[row])):

        user_grid[row][column] = int(input("Enter a number: "))

    print(user_grid)

