drivers = [
    ["Carol Sainz", 5],
    ["George Russell", 6],
    ["Sergio Perez", 2],
    ["Max Verstappen", 1],
    ["Lando Norris", 4],
    ["Lewis Hamilton", 3],
]

# list drivers in unordered list
print(drivers)

# loop through each row in drivers list
for driver in range(len(drivers) - 1):
    
    # looping each nested interation
    for standing in range(len(drivers) - 1):
        
        # if the position is greater number than the next value switch the driver and their positions around
        if drivers[standing][1] > drivers[standing + 1][1]:
            drivers[standing][0],drivers[standing][1], drivers[standing + 1][0], drivers[standing + 1][1] = drivers[standing + 1][0], drivers[standing + 1][1], drivers[standing][0], drivers[standing][1]

# list ordered driver list
print(drivers)

# deconstruct list and save each driver in variable
first, second, third, *rest = drivers

print(first)
print(second)
print(third)
print(rest)