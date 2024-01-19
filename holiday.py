def line_break(symbol):
    # create a decorator on the terminal which breaks up the code when printed.
    return f"{symbol*79}"

def destinations_err_msg():
    """
    The function `destinations_err_msg` prints an error message with possible
    reasons for the error and a list of available destinations.
    """
    print(lb)
    print("ERROR:")
    print("You have not met our criteria, please see below where your issue may lie:")
    print('\n')
    print("1) You have not entered a valid numerical value or a value that is at least 0 for car rental or hotel stay")
    print("2) You may have chosen a destination not available in our database. Please see below for what's available.")
    print('\n')
    display_destinations() # post the destinations again for the user
    print(lb)

def display_destinations():
    print("Destinations:")
    for destination in destinations.keys():
        print(f"- {destination}")
    print(lb)

def hotel_cost(num_nights):
    """
    The function calculates the total cost of a hotel stay based on the number of
    nights.
    
    :param num_nights: The number of nights the person will be staying at the hotel
    :return: the total cost of the hotel stay.
    """
    
    cost_per_night = 120
    total_cost = cost_per_night * int(num_nights)
    print(f"Hotel cost at £{cost_per_night} per night, for {num_nights} days.")
    return total_cost

def plane_cost(destination):
    """
    The function "plane_cost" prints the destination and returns the cost of a
    return flight to that destination.
    
    :param destination: The parameter "destination" is a string that represents the
    desired destination for the flight
    :return: the cost of a return flight to the specified destination.
    """
    print(lb)
    print("Return flights to:")
    print(f"- {destination}")
    return destinations[destination]

def car_rental(rental_days):
    """
    The function calculates the total cost of car rental based on the number of
    rental days.
    
    :param rental_days: The number of days the car is being rented for
    :return: the total cost of the car rental.
    """
    cost_per_day = 40
    total_cost = cost_per_day * int(rental_days)
    print(f"Car rental at £{cost_per_day} per night, for {rental_days} days.")
    return total_cost

def holiday_cost(hotel_cost, plane_cost, car_rental):
    """
    The function `holiday_cost` calculates the total cost of a holiday by adding
    the costs of a hotel, plane tickets, and car rental, and then prints a
    breakdown of the costs.
    
    :return: a string that includes the breakdown of the holiday cost and the total
    cost.
    """
    print('\n')
    print("Please see your breakdown above:")
    print(f"Your holiday will cost you in total: ")

    # Header
    print('='*30)
    print("Your Recipt:")
    print('='*30)

    # Items
    print(f"Flights -- £{hotel_cost}")
    print(f"Hotel -- £{plane_cost}")
    print(f"Car rental - £{car_rental}")

    total_holiday_cost = hotel_cost + plane_cost  + car_rental
    return f"{('-'*30)}\nTotal: £{total_holiday_cost:.2f}\n{('='*30)}\n"

destinations = {
    "London": 125,
    "Medellin": 850,
    "Sydney": 1200,
    "Tokyo": 900,
    "Berlin": 95,
    "Washington": 400,
    "Johannesburg": 700,
}

lb = line_break('-')
holiday_valid = False
print("Welcome! See our available flight destinations:")
display_destinations() # show the user the destinations.
while (not holiday_valid):

    city_flight = input("Please select from the listed destinations where you want to fly: ").strip().capitalize()
    num_nights = input("Enter the number of nights you will stay at the hotel (i.e. 3): ").strip()
    rental_days = input("Please enter the number of days you require car rental (i.e. 5): ").strip()

    # I need some help putting this on multiple lines as when i try it does not work lol
    if len(city_flight) == 0 or city_flight.isnumeric() or city_flight not in destinations.keys() or num_nights == '' or num_nights.isalpha() or int(num_nights) < 0 or rental_days == '' or rental_days.isalpha() or int(rental_days) < 0:
        destinations_err_msg()

    else:
        book_plane = plane_cost(city_flight)
        destinations_duration = hotel_cost(num_nights)
        car_duration = car_rental(rental_days)
        user_holiday = holiday_cost(book_plane, destinations_duration, car_duration)
        print(user_holiday)
        print("We hope to see you again soon, Goodbye")
        holiday_valid = True