"""
This 
a very hard project
"""
guests = {'306':'Bilguuntur', '307':'Irmuun', '51':'Michael', '309':'Taivan'}
roomnumber = input('Hello customer would you please enter your room number: ')
if roomnumber in guests.keys():
    name = roomnumber in guests.keys()
    maindish=input(f"Hello {name}! What would you like to order as a main dish?")
else:
    print('Sorry there are no users with that number. Please stop being stupid.')
