# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Locations in a seperate file
from tabulate import tabulate

# Array of the map, formated using tabulate

Player = 'player'
Lake1 = "lake1"
Lake2 = "lake2"
Lake3 = "lake3"
Lake4 = "lake4"
Lake5 = "lake5"
Lake6 = "lake6"
Lake7 = "lake7"
Nothingtile = 'hi'
Start = 'start'

map = [
       [None, None, Lake6, None, None],
       [None, None, None, None, None],
       [Lake5, None, None, None, Lake4],
       [None, None, None, None, None],
       [None, Lake3, None, Lake2, None],
       [None, None, Lake1, None, None],
       [None, None, None, Player, Start]
]

y = 6
x = 3


def location():
    """Commands that allow for movement on the map"""
    global x
    global y
    global map
    # While loop for continous play
    while True:
        # Prints map out in a grid style using tabulate
        print(tabulate(map, tablefmt="grid"))
        # Tells user to type q to go to the previous menu
        print('\ntype q to go back to previous menu')
        print('North')
        print('West')
        print('East')
        print('South')
        # Asks for user input of what location they would like to go to
        user = input('Select a Movement: ')
        # Makes all user inputs lower cased to match if and elif statements
        user = user.lower()
        # Checks to see if user typed in movement command
        if user == 'north':
            map = map[y-1][x-1]
            # prints out Movement
            print('Travelling North!')
        # Checks to see if user typed in movement command
        elif user == 'west':
            # prints out Movement
            print('Travelling West!')
        # Checks to see if user typed in movement command
        elif user == 'east':
            # prints out Movement
            print('Travelling East!')
        # Checks to see if user typed in movement command
        elif user == 'south':
            # prints out Movement
            print('Travelling South!')
            # Checks to see if user typed q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if user typed anything else
        else:
            # Tells user it is an invalid option
            print('invalid option')


# Creates a dictionary with a list of fishes available at each lake
locations = {'Hooligan Lake': ['Salmon', 'GoldFish', 'Guppy'],
             'Where are we now Lake': ['Hammerhead Sharks', 'The Great White',
                                       'Saw Sharks'],
             'Ethereal Lake': ['Ethereal Ultim\
atum'], 'Residential Lake': ['Shopkeeper'],
             }
location()
