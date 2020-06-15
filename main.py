from solebox import *
from snipes import *

import os, sys

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
    debug = True


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


prompt = Log()
debug = True

def clear():
    os.system('clear')

def lightning():
    prompt.print(prompt.colors['yellow'], "",
"\n            ,/\n\
          ,'/\n\
        ,' /\n\
      ,'  /_____,\n\
    .'____    ,'\n\
         /  ,'\n\
        / ,'\n\
       /,'\n\
      /'", "\n")

def greetings():
    lightning()
    prompt.print(prompt.colors['yellow'], "", "Welcome to Solebot !", "\n\n")

def main_menu():
    prompt.White("Choose an option")
    prompt.White("  1) Use bot for solebox.com")
    prompt.White("  2) Use bot for snipes.fr (COMING SOON)")
    prompt.White("  3) Use bot with config file (COMING SOON)")
    prompt.White("  4) Exit")

    return input("\n  > ")

def solebox_menu():
    clear()
    lightning()
    prompt.print(prompt.colors['yellow'], "", "Solebox.com Menu", "\n\n")
    prompt.White("Choose an option")
    prompt.White("  1) Create account")
    prompt.White("  2) Add product to cart")
    prompt.White("  3) Back")
    prompt.White("  4) Exit")

    return input("\n  > ")

def solebox_account_menu():
    clear()
    lightning()
    prompt.print(prompt.colors['yellow'], "", "Solebox.com New Account Menu", "\n\n")

    gender = ""
    while (gender != "mr" and gender != "mrs"):
        try:
            gender = input("Please specify a gender (mr/mrs): ")
        except KeyboardInterrupt:
            return

    firstName = ""
    while (firstName == ""):
        try:
            firstName = input("Please specify your first name: ")
        except KeyboardInterrupt:
            return

    lastName = ""
    while (lastName == ""):
        try:
            lastName = input("Please specify your last name: ")
        except KeyboardInterrupt:
            return

    email = ""
    while (email == ""):
        try:
            email = input("Please specify your email address: ")
        except KeyboardInterrupt:
            return
    email2 = ""
    while (email != email2):
        try:
            email2 = input("Please confirm your email address: ")
        except KeyboardInterrupt:
            return

    password = ""
    while (password == ""):
        try:
            password = input("Please specify your password: ")
        except KeyboardInterrupt:
            return
    password2 = ""
    while (password != password2):
        try:
            password2 = input("Please specify your password: ")
        except KeyboardInterrupt:
            return

    csrf_token, cookies = solebox_get_csrf_token(debug)

    if solebox_create_user(cookies, csrf_token, gender, firstName, lastName, email, password, debug):
        prompt.Info("Account created successfully")
        input("Press any key to continue")
    else:
        prompt.Error("An error occured while creating new account. Maybe your email is already in use ?")
        input("Press any key to continue")

def solebox_product_menu():
    clear()
    lightning()
    prompt.print(prompt.colors['yellow'], "", "Solebox.com Cart Menu", "\n\n")

    email = ""
    while ("@" not in email):
        try:
            email = input("Please specify your email address: ")
        except KeyboardInterrupt:
            return

    password = ""
    while (password == ""):
        try:
            password = input("Please specify your password: ")
        except KeyboardInterrupt:
            return

    csrf_token, cookies = solebox_get_csrf_token(debug)
    cookies = solebox_login(cookies, csrf_token, email, password, debug)

    if cookies is None:
        prompt.Error("An error occured while logging into your account. Maybe your mistyped your credentials ?")
        input("Press any key to continue")
        return
    else:
        prompt.Info("Connection successful")

    url = ""
    while ("www.solebox.com/" not in url):
        try:
            url = input("Please specify the URL of the product you want to add to cart: ")
        except KeyboardInterrupt:
            return

    pid = solebox_get_pid(cookies, url, debug)
    if (pid is None):
        prompt.Error("An error occured while fetching the product's PID. Are you sure you typed a valid URL ?")
        input("Press any key to continue")
        return
    else:
        prompt.Info("PID fetched successfully")

    size = ""
    while (not size.isdigit()):
        try:
            size = input("Please specify the size you want: ")
        except KeyboardInterrupt:
            return

    quantity = ""
    while (not quantity.isdigit()):
        try:
            quantity = input("Please specify the quantity you want: ")
        except KeyboardInterrupt:
            return

    if (solebox_buy_shoe(cookies, pid, size, quantity, debug)):
        prompt.Info("Product added successfully to your cart")
        input("Press any key to continue")
    else:
        prompt.Error("An error occured while adding the product to your cart")
        input("Press any key to continue")

def solebox():
    exit = False
    while (not exit):
        try:
            choice = solebox_menu()
        except KeyboardInterrupt:
            print("")
            return

        if (choice == "1"):
            solebox_account_menu()
        elif (choice == "2"):
            solebox_product_menu()
        elif (choice == "3"):
            exit = True
        elif (choice == "4"):
            sys.exit(0)


def main():
    exit = False
    while (not exit):
        clear()
        greetings()

        try:
            choice = main_menu()
        except KeyboardInterrupt:
            print("")
            sys.exit(0)

        if (choice == "1"):
            solebox()
        elif (choice == "2"):
            #Snipes
            break
        elif (choice == "3"):
            #File
            break
        elif (choice == "4"):
            exit = True

main()
