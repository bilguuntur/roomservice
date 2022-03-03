"""
This 
a very hard project
"""
guests = {'306':'Bilguuntur', '307':'Irmuun', '51':'Michael', '309':'Taivan'}
roomnumber = input('Hello customer would you please enter your room number: ')
if roomnumber in guests.keys():
    print('what would you like to order')
else:
    print('sorry no such user here')
