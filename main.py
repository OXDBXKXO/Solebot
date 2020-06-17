from solebox import *
from snipes import *

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
    if (site == "solebox"):
        csrf_token, cookies = solebox_get_csrf_token(debug)
    else:
        csrf_token, cookies = snipes_get_csrf_token(debug)

    if csrf_token is None:
        prompt.Error("An error occured while getting csrf_token. Maybe your Internet is down ?")
        input("Press any key to continue")
        return


    if (site == "solebox"):
        success = solebox_create_user(cookies, csrf_token, gender, firstName, lastName, email, password, debug)
    else:
        success = snipes_create_user(cookies, csrf_token, gender, firstName, lastName, email, password, debug)

    if (success):
        prompt.Info("Account created successfully\n")
        input("Press any key to continue")
    else:
        prompt.Error("An error occured while creating new account. Maybe your email is already in use ?")
        input("Press any key to continue")

def login(site, email, password, debug):
    print("")
    prompt.Comment("Connecting...")
    if (site == "solebox"):
        csrf_token, cookies = solebox_get_csrf_token(debug)
    else:
        csrf_token, cookies = snipes_get_csrf_token(debug)

    if csrf_token is None:
        prompt.Error("An error occured while getting csrf_token. Maybe your Internet is down ?")
        input("Press any key to continue")
        return

    if (site == "solebox"):
        success, cookies = solebox_login(cookies, csrf_token, email, password, debug)
    else:
        success, cookies = snipes_login(cookies, csrf_token, email, password, debug)

    return success, cookies

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
        prompt.Error("An error occured while logging into your account: " + cookies)
        input("Press any key to continue")
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

    if (site == "solebox"):
        sizes = solebox_get_available_shoes(cookies, url, debug)
    else:
        sizes = snipes_get_available_shoes(cookies, url, debug)

    if (sizes is None):
        prompt.Error("An error occured while fetching available sizes. Maybe product is sold out ?")
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

    if (site == "solebox"):
        pid = solebox_get_pid(cookies, url, debug)
    else:
        pid = snipes_get_pid(cookies, url, debug)

    if (pid is None):
        prompt.Error("An error occured while fetching the product's PID. Are you sure you typed a valid URL ?")
        input("Press any key to continue")
        return

    if (site == "solebox"):
        quant = solebox_quantity_available(cookies, url, pid, sizes[int(size) - 1], debug)
    else:
        quant = snipes_quantity_available(cookies, url, pid, sizes[int(size) - 1], debug)

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

    if (site == "solebox"):
        upid = solebox_get_unique_pid(cookies, url, pid, sizes[int(size) - 1], debug)
        res, msg = solebox_buy_shoe(cookies, upid, size, quantity, debug)
        if (res):
            prompt.Info("Product added successfully to your cart\n")
        else:
            prompt.Error("An error occured while adding the product to your cart")
            input("Press any key to continue")
            return
    else:
        upid = snipes_get_unique_pid(cookies, url, pid, sizes[int(size) - 1], debug)
        res, msg = snipes_buy_shoe(cookies, upid, size, quantity, debug)
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

            if (site == "solebox"):
                sizes = solebox_get_available_shoes(cookies, url, debug)
            else:
                sizes = snipes_get_available_shoes(cookies, url, debug)

            if (sizes is None):
                prompt.Error("This product is not available anymore.")
                continue

            if (size not in sizes):
                prompt.Error("The size specified is not available.")
                continue

            prompt.Comment("Fetching available quantity...")

            if (site == "solebox"):
                pid = solebox_get_pid(cookies, url, debug)
            else:
                pid = snipes_get_pid(cookies, url, debug)

            if (pid is None):
                prompt.Error("An error occured while fetching the product's PID.")
                continue

            if (site == "solebox"):
                quant = solebox_quantity_available(cookies, url, pid, size, debug)
            else:
                quant = snipes_quantity_available(cookies, url, pid, size, debug)

            if (quant is None or not quant.isdigit()):
                prompt.Error("An error occured while fetching product's disponibility.")
                continue

            if (int(quantity) > int(quant)):
                prompt.Error("Quantity is bigger than maximum allowed.")
                continue

            if (site == "solebox"):
                upid = solebox_get_unique_pid(cookies, url, pid, size, debug)
                res, msg = solebox_buy_shoe(cookies, upid, size, quantity, debug)
                if (res):
                    prompt.Info("Product added successfully to your cart\n")
                else:
                    prompt.Error("An error occured while adding the product to your cart: " + msg)
            else:
                upid = snipes_get_unique_pid(cookies, url, pid, size, debug)
                res, msg = snipes_buy_shoe(cookies, upid, size, quantity, debug)
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
token, cookies = solebox_get_csrf_token(False)
#print(snipes_get_pid(cookies, "https://www.snipes.fr/p/adidas-nmd__r1_neon_pack-ftwr_white%2Fcore_black%2Fsolar_green-00013801822085.html", True))
url = "https://www.solebox.com/en_FR/p/nike-space_hippie_04_grey-volt-grey%2Fvolt-black-01834676.html"
#print(solebox_get_available_shoes(cookies, url, False))
pid = solebox_get_pid(cookies, url, False)
print(pid)
#print(solebox_get_unique_pid(cookies, url, pid, "42", False))
print(snipes_get_available_shoes(cookies, url, debug))
print(snipes_quantity_available(cookies, url, pid, "42", True))

test = "<a href=\"https://www.solebox.com/en_FR/p/vans-vault_ua_og_chukka_lx_canvas%2Fcheckerboard-heliotrope-01794708.html\"\
                            class=\"js-pdp-attribute-btn b-pdp-swatch-link js-pdp-attribute-btn--size\"\
                            data-attr-id=\"size\"\
                            data-value=\"42.5\"\
                            data-href=\"/en_FR/p/vans-vault_ua_og_chukka_lx_canvas%2Fcheckerboard-heliotrope-01794708.html?chosen&#x3D;size&amp;dwvar_01794708_212&#x3D;42.5\">\
                            <span data-attr-value=\"42.5\"\
                                class=\"\
                                    js-pdp-attribute-tile\
                                    b-size-value\
                                    js-size-value\
                                    b-swatch-circle\
                                    b-swatch-value\
                                    \
                                     b-swatch-value--selectable \
                                        b-swatch-value--orderable\
                                \"\
                            >\
                                    42.5\
                            </span>\
                            </a>"

#print(re.findall(r"selectable.+?b-swatch-value--orderable.+?\">.+?([.0123456789]+).+?<\/span>", test, re.S))
