from sneakershop import *

import os, sys, re

prompt = Log()
debug = False

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
    prompt.White("  2) Use bot for snipes.fr")
    prompt.White("  3) Use bot with from file")
    prompt.White("  4) Exit")

    return input("\n  > ")

def site_menu(site):
    clear()
    lightning()
    if (site == "solebox"):
        prompt.print(prompt.colors['yellow'], "", "Solebox.com Menu", "\n\n")
    else:
        prompt.print(prompt.colors['yellow'], "", "Snipes.fr Menu", "\n\n")
    prompt.White("Choose an option")
    prompt.White("  1) Create account")
    prompt.White("  2) Add product to cart")
    prompt.White("  3) Back")
    prompt.White("  4) Exit")

    return input("\n  > ")

def account_menu(site):
    clear()
    lightning()

    if (site == "solebox"):
        prompt.print(prompt.colors['yellow'], "", "Solebox.com New Account Menu", "\n\n")
    else:
        prompt.print(prompt.colors['yellow'], "", "Snipes.fr New Account Menu", "\n\n")

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

    print("")
    prompt.Comment("Sending request to server...")

    csrf_token, cookies = get_csrf_token(site, debug)

    if csrf_token is None:
        prompt.Error("An error occured while getting csrf_token. Maybe your Internet is down ?")
        input("Press any key to continue")
        return

    success = create_user(site, cookies, csrf_token, gender, firstName, lastName, email, password, debug)

    if (success):
        prompt.Info("Account created successfully\n")
        input("Press any key to continue")
    else:
        prompt.Error("An error occured while creating new account. Maybe your email is already in use ?")
        input("Press any key to continue")

def login(site, email, password, debug):
    print("")
    prompt.Comment("Connecting...")

    csrf_token, cookies = get_csrf_token(site, debug)

    if csrf_token is None:
        prompt.Error("An error occured while getting csrf_token. Maybe your Internet is down ?")
        input("Press any key to continue")
        return False, None

    return shop_login(site, cookies, csrf_token, email, password, debug)

def product_menu(site):
    clear()
    lightning()

    if (site == "solebox"):
        prompt.print(prompt.colors['yellow'], "", "Solebox.com Cart Menu", "\n\n")
    else:
        prompt.print(prompt.colors['yellow'], "", "Snipes.fr Cart Menu", "\n\n")

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

    success, cookies = login(site, email, password, debug)

    if (not success):
        return
    else:
        prompt.Info("Connection successful\n")

    url = ""

    if (site == "solebox"):
        check = "www.solebox.com/"
    else:
        check = "www.snipes.fr/"

    while (url.find(check) == -1):
        try:
            url = input("Please specify the URL of the product you want to add to cart: ")
        except KeyboardInterrupt:
            return

    print("")
    prompt.Comment("Fetching available sizes...\n")

    response = get_product_page(cookies, url, debug)
    sizes = get_available_shoes(site, response, debug)

    if (sizes is None):
        prompt.Error("An error occured while fetching available sizes. Maybe product is sold out or your internet is down ?")
        input("Press any key to continue")
        return

    print("Available sizes:")
    index = 0
    for size in sizes:
        index += 1
        print("  " + str(index) + ") " + size)

    size = ""
    while (not (size.isdigit() and int(size) >= 1 and int(size) <= index)):
        try:
            size = input("Please choose an option: ")
        except KeyboardInterrupt:
            return

    print("")
    prompt.Comment("Fetching available quantity...\n")

    pid = get_pid(response, debug)

    if (pid is None):
        prompt.Error("An error occured while fetching the product's PID. Are you sure you typed a valid URL ?")
        input("Press any key to continue")
        return

    quant = get_quantity_available(cookies, url, pid, sizes[int(size) - 1], debug)

    if (quant is None or not quant.isdigit()):
        prompt.Error("An error occured while fetching product's disponibility.")
        input("Press any key to continue")
        return

    quantity = ""
    while (not (quantity.isdigit() and int(quantity) >= 1 and int(quantity) <= int(quant))):
        max = 10
        if (int(quant) < 10):
            max = int(quant)

        try:
            quantity = input("Please specify the quantity you want (" + str(max) + " max): ")
        except KeyboardInterrupt:
            return

    print("")
    prompt.Comment("Sending request to server...")

    upid = get_unique_pid(cookies, url, pid, sizes[int(size) - 1], debug)
    res, msg = buy_shoe(site, cookies, url, upid, size, quantity, debug)
    if (res):
        prompt.Info("Product added successfully to your cart\n")
    else:
        prompt.Error("An error occured while adding the product to your cart: " + msg)
        input("Press any key to continue")
        return

    out = ""
    while (not (out == "y" or out == "yes" or out == "n" or out == "no")):
        try:
            out = input("Would you like to generate a file to automate future order ? (yes/no): ")
        except KeyboardInterrupt:
            return

    if (out == "y" or out == "yes"):
        filename = ""
        while (filename == ""):
            try:
                filename = input("Please specify a filename: ")
            except KeyboardInterrupt:
                return

        try:
            file = open(filename, 'w+')
        except OSError:
            prompt.Error("An error occured while creating file")
            input("Press any key to continue")
            return

        file.write(site + ';' + email + ';' + password + ';' + url + ';' + sizes[int(size) - 1] + ';' + quantity + ";\n")
        print("")
        prompt.Info("File created successfully. You can now use it from the 'Use bot with from file' option in Main Menu\n")
        input("Press any key to continue")

def from_file_menu():
    clear()
    lightning()
    prompt.print(prompt.colors['yellow'], "", "Run From File Menu", "\n\n")
    prompt.White("Choose an option")
    prompt.White("  1) Run file in current directory")
    prompt.White("  2) Run file from remote location (requires full path)")
    prompt.White("  3) Back")
    prompt.White("  4) Exit")

    return input("\n  > ")

def run_from_config_file():
    try:
        choice = from_file_menu()
    except KeyboardInterrupt:
        print("")
        return

    if (choice == "1"):
        try:
            name = input("Please specify the name of config file (the file must be in current directory): ")
        except KeyboardInterrupt:
            return
        filename = os.getcwd() + '/' + name
    elif (choice == "2"):
        try:
            filename = input("Please specify full path of config file: ")
        except KeyboardInterrupt:
            return
    elif (choice == "3"):
        return
    elif (choice == "4"):
        sys.exit(0)

    try:
        file = open(filename, 'r')
    except OSError:
        prompt.Error("An error occured while opening file")
        input("Press any key to continue")
        return

    clear()
    lightning()
    print("")

    with file:
        for line in file.readlines():
            if (line == ""):
                continue
            split = line.split(';')

            site = split[0]
            if (site != "solebox" and site != "snipes"):
                prompt.Error("Webiste " + site + " is not supported (yet)")
                continue
            email = split[1]
            password = split[2]
            url = split[3]
            size = split[4]
            quantity = split[5]
            if (not quantity.isdigit()):
                prompt.Error("Quantity is not a number")
                continue

            debug = False

            success, cookies = login(site, email, password, debug)

            if (not success):
                prompt.Error("An error occured while logging into your account: " + cookies)
                continue
            else:
                prompt.Info("Connection successful")

            prompt.Comment("Fetching available sizes...")

            response = get_product_page(cookies, url, debug)
            sizes = get_available_shoes(site, response, debug)

            if (sizes is None):
                prompt.Error("This product is not available anymore.")
                continue

            if (size not in sizes):
                prompt.Error("The size specified is not available.")
                continue

            prompt.Comment("Fetching available quantity...")

            pid = get_pid(response, debug)

            if (pid is None):
                prompt.Error("An error occured while fetching the product's PID.")
                continue

            quant = get_quantity_available(cookies, url, pid, size, debug)

            if (quant is None or not quant.isdigit()):
                prompt.Error("An error occured while fetching product's disponibility.")
                continue

            if (int(quantity) > int(quant)):
                prompt.Error("Quantity is bigger than maximum allowed.")
                continue

            upid = get_unique_pid(cookies, url, pid, size, debug)
            res, msg = buy_shoe(site, cookies, url, upid, size, quantity, debug)
            if (res):
                prompt.Info("Product added successfully to your cart\n")
            else:
                prompt.Error("An error occured while adding the product to your cart: " + msg)
    try:
        filename = input("Press any key to continue")
    except KeyboardInterrupt:
        return

def dispatcher(site):
    exit = False
    while (not exit):
        try:
            choice = site_menu(site)
        except KeyboardInterrupt:
            print("")
            return

        if (choice == "1"):
            account_menu(site)
        elif (choice == "2"):
            product_menu(site)
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
            dispatcher("solebox")
        elif (choice == "2"):
            dispatcher("snipes")
        elif (choice == "3"):
            run_from_config_file()
        elif (choice == "4"):
            exit = True

main()
sys.exit(0)
