"""
This 
a very hard project
"""
mainmenu = ['Spaghetti','Pizza','Burger']
guests = {'306':'Bilguuntur', '307':'Irmuun', '51':'Michael', '309':'Taivan'}
roomnumber = input('Hello customer would you please enter your room number: ')
if roomnumber in guests.keys():
    name = guests[roomnumber]
    print (mainmenu)
    maindish =input (f"Hello {name}! What would you like to order from the list above as a main dish?")
    if maindish in mainmenu:
        print('e')
    else:
        print (mainmenu)
        maindish=input ("Please choose one of the items above: ")
else:
    print('Sorry there are no users with that number. Please stop being stupid.')
