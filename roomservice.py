guests = {'306':'Bilguuntur', '307':'Irmuun', '308':'Tengis', '309':'Taivan'}
roomnumber = input('Hello customer would you please enter your room number: ')
if roomnumber in guests.keys():
    print('what would you like to order')
else:
    print('sry no such user here')
