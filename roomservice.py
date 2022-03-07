"""
This 
a very hard project
"""
mainorder = 0
sideorder = 0
drinkorder = 0
mainmenu = ['Spaghetti','Pizza','Burger']
guests = {'306':'Bilguuntur', '307':'Irmuun', '51':'Michael', '309':'Taivan'}
roomnumber = input('Hello customer would you please enter your room number: ')
if roomnumber in guests.keys():
    while mainorder < 1:
        name = guests[roomnumber]
        print (mainmenu)
        maindish =input (f"Hello {name}! What would you like to order from the list above as a main dish?")
        if maindish in mainmenu:
            mainorder = 1
            print('e')
else:
    print('Sorry there are no users with that number. Please stop being stupid.')
