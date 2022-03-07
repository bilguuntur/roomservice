"""
This 
a very hard project
"""
mainorder = 0
sideorder = 0
drinkorder = 0
mainmenu = ['Spaghetti','Pizza','Burger']
sidemenu = ['Fries','Salad','Fruit']
drinkmenu = ['Orange Juice','Coca Cola','Water']
guests = {'306':'Bilguuntur', '307':'Irmuun', '51':'Michael', '309':'Taivan'}
roomnumber = input('Hello customer would you please enter your room number: ')
if roomnumber in guests.keys():
    while mainorder < 1:
        name = guests[roomnumber]
        print (mainmenu)
        maindish = input (f"Hello {name}! What would you like to order from the list above as a main dish?")
        if maindish in mainmenu:
            mainorder = 1
            while sideorder < 1:
                print (sidemenu)
                sidedish = input ('What would you like to order from the list above as a side dish?')
                if sidedish in sidemenu:
                    sideorder = 1
                    while drinkorder < 1:
                        print (drinkmenu)
                        drink = input ('What would you like to order from the list above as a drink?')
                        if drink in drinkmenu:
                            drinkorder = 1
                            print (f"Thank you for ordering, please wait as your {maindish}, {sidedish}, and {drink} arrive to your hotel room shortly.")
else:
    print('Sorry there are no users with that number. Please stop being stupid.')
