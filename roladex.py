class Contact():

    has_been_viewed = False

    def __init__(self, name, number):
        self.name = name
        self.number = number

    
    def populate_roladex(self):
        new_contact = {}
        new_contact["name"] = self.name
        new_contact["contact"] = self.number

        roladex.append(new_contact)
        test_roladex.append(new_contact) # add a new user into roladex.
    

    def mark_as_viewed(self):

        if self.has_been_viewed == False:
            self.has_been_viewed = True
            return self.has_been_viewed
        

def add_new():
    name = input("add Name: ")
    number = input("add Number: ")

    new_contact = Contact(name, number)
    return new_contact


def list_emails():
    for number, contact in enumerate(roladex, 1):
        print(number, contact.name, contact.number)


def read_email(user_input):
    user_input -= 1
    print(roladex[user_input].name)
    print(roladex[user_input].number)
    roladex[user_input].mark_as_viewed()
    print(f"Roladex page for {roladex[user_input].name}, has been read")

roladex = []

# Hard Code contacts
contact_1 = Contact("Bruce Wayne", "555-555-5555")
contact_2 = Contact("Clark Kent", "222-222-2222")
contact_3 = Contact("Wally West", "999-999-9999")

# Hard code data being appended into Roladex
roladex.append(contact_1)
roladex.append(contact_2)
roladex.append(contact_3)

# list all the emails in order
list_emails()

# Mark list item 3 as viewed using mark_as_viewed using dot notation.
print(contact_1.name, contact_1.has_been_viewed)
contact_1.mark_as_viewed()
print(contact_1.name, contact_1.has_been_viewed)
print('-'*80)

# Mark list item 3 as viewed using mark_as_viewed Func
read_email(3)

# Mark list item 2 as viewed using mark_as_viewed Func
read_email(2)

# updating the Boolean value of has been viewed
print(contact_1.name,contact_1.has_been_viewed)
print(contact_2.name,contact_2.has_been_viewed)
print(contact_3.name,contact_3.has_been_viewed)


# User Menu

def user_menu():
    MENU = f"""
        User Options

        1. View email.
        2. View unread emails.
        3. Quit.

    """
    MENU += f": "

    return MENU

user_option = input(user_menu())


# Menu option functionality.
if user_option == '1':

    list_emails()

    while True:

        user_input = input("Enter a list number: ")
        if user_input.isnumeric and int(user_input) <= len(roladex):
            read_email(int(user_input))
            break
        
elif user_option == '2':

    # Flag which will be set True if loop finds an unread email
    unread_email_found = False
    
    for roladex_page in roladex:

        if roladex_page.has_been_viewed == False:
            print(roladex_page.name)
            unread_email_found = True
    
    # line 62, 67, 70 includes method to toggle boolean vals for roladex list items    
    if unread_email_found == False:
        print("You have no emails to read.")
 
    

elif user_option == '3':

    print('Goodbye.')

print('-'*80)

names = [
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Gareth Bale"
    ]

numbers = [
    "111-111-1111",
    "222-222-2222",
    "333-333-3333",
]

test_roladex = []

# Create three separate users to populate the Roladex.
for i in range(len(names)):

    pass
    # create a user
    # using the index from the name and numbers lists
    name = names[i]
    number = numbers[i]

    # pass values into the Contact class to make a user.
    new_contact = Contact(name, number)

    # Pass new contact into Class Method to populate list
    new_contact.populate_roladex()

    # Display list being populated into list
    print(test_roladex)
