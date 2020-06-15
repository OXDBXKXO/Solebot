from solebox import *
from snipes import *

################################################################################
#                                  SOLEBOX
################################################################################

def solebox():

    #CSRF bypass (Get a look at REAMDE.md to know how to get valid dwsid & token)
    dwsid = "ReipGMWtZ2vkVO63tR-i3-blqBF9BKgNfjrtkKFhjVXiCuJKZBj014u-NBo7TPnAVk4AJkZlsfe0z9AXuAI4ww=="
    csrf_token = "Pvcj7N5CACmKXT4Hnto5R7qh8a8pna8zLZgIyydNuc3G7a4HzID3bbyAdTEmjrNJ5nHhhXhIOdlCL0Y9--EPGQNyWDQvcqxBeB8nyNncKg9bCshHMjqHnWDqYh6xUTDMKtbQ2uuN8O725AQRMMmalXBSJJcHhRtMFBRBY3eFFxotIISKSlw%3D"

    #Credentials
    email = "test10@test.test"
    password = "TESTtest123"

    #Product info
    pid = "0181863000000008"
    size = "44"

    #Debug mode (True/False)
    debug = False


    if solebox_create_user(dwsid, csrf_token, email, password, debug):
        print("Account created successfuly")
    else:
        print("An error occured while creating new user")

    cookies = solebox_login(dwsid, csrf_token, email, password, debug)

    if cookies is not None:
        print("Login successful")
        if solebox_buy_shoe(pid, size, cookies["dwsid"], debug):
            print("Product added successfuly")
        else:
            print("An error occured while adding product to cart")
    else:
        print("An error occured during connection")


################################################################################
#                                  SNIPES
################################################################################

def snipes():

    #CSRF bypass (Get a look at REAMDE.md to know how to get valid dwsid & token)
    dwsid = "ReipGMWtZ2vkVO63tR-i3-blqBF9BKgNfjrtkKFhjVXiCuJKZBj014u-NBo7TPnAVk4AJkZlsfe0z9AXuAI4ww=="
    csrf_token = "Pvcj7N5CACmKXT4Hnto5R7qh8a8pna8zLZgIyydNuc3G7a4HzID3bbyAdTEmjrNJ5nHhhXhIOdlCL0Y9--EPGQNyWDQvcqxBeB8nyNncKg9bCshHMjqHnWDqYh6xUTDMKtbQ2uuN8O725AQRMMmalXBSJJcHhRtMFBRBY3eFFxotIISKSlw%3D"

    #Credentials
    email = "test10@test.test"
    password = "TESTtest123"

    #Product info
    pid = "0001380178974200000004"
    size = "41"

    #Debug mode (True/False)
    debug = False


    if snipes_create_user(dwsid, csrf_token, email, password, debug):
        print("Account created successfuly")
    else:
        print("An error occured while creating new user")

    cookies = snipes_login(dwsid, csrf_token, email, password, debug)

    if cookies is not None:
        print("Login successful")
        if snipes_buy_shoe(pid, size, cookies["dwsid"], debug):
            print("Product added successfuly")
        else:
            print("An error occured while adding product to cart")
    else:
        print("An error occured during connection")

solebox()
snipes()
