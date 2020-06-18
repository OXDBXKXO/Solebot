from request import Requet, Log
import re

def get_csrf_token(site, debug):
    '''
    Gets csrf_token needed for further operations
    '''
    if (site == "solebox"):
        req = Requet(True, 'www.solebox.com', timeout=90)
        target = '/en_FR/login'
    else:
        req = Requet(True, 'www.snipes.fr', timeout=30)
        target = '/login'

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

    rep, cookies = req.requet2(target,
        method='get',
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
    	}
        )

    if rep is None:
        return None, None

    matches = re.findall('csrf_token" value="(.+?)"', rep)

    if len(matches) > 0:
        return matches[0], cookies
    else:
        return None, None

def create_user(site, cookies, csrf_token, gender, firstName, lastName, email, password, debug):
    '''
    Tries to create a new user with given arguments, returns success as boolean
    '''
    mail = email.replace('@', '%40')

    if (site == "solebox"):
        req = Requet(True, 'www.solebox.com', timeout=90)
        target = '/on/demandware.store/Sites-solebox-Site/en_FR/Account-SubmitRegistration?rurl=1&format=ajax'
    else:
        req = Requet(True, 'www.snipes.fr', timeout=30)
        target = '/on/demandware.store/Sites-snse-FR-Site/fr_FR/Account-SubmitRegistration?rurl=1&format=ajax'

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet(target,
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest'
    	},
        cookies=cookies,
    	body='dwfrm_profile_register_title=' + gender + '&dwfrm_profile_register_firstName=' + firstName + '&dwfrm_profile_register_lastName=' + lastName + '&dwfrm_profile_register_email=' + email + '&dwfrm_profile_register_emailConfirm=' + email + '&dwfrm_profile_register_password=' + password + '&dwfrm_profile_register_passwordConfirm=' + password + '&dwfrm_profile_register_phone=&dwfrm_profile_register_birthday=&dwfrm_profile_register_acceptPolicy=true&csrf_token=' + csrf_token
    )

    if rep is None:
        return False

    if debug:
        print(rep)

    return "\"success\": true" in rep

def shop_login(site, cookies, csrf_token, email, password, debug):
    '''
    Tries to login with given arguments, returns success as a dictionary, either None or containing session cookies
    '''
    mail = email.replace('@', '%40')

    if (site == "solebox"):
        req = Requet(True, 'www.solebox.com', timeout=90)
        target = '/en_FR/authentication?rurl=1&format=ajax'
    else:
        req = Requet(True, 'www.snipes.fr', timeout=30)
        target = '/authentication?rurl=1&format=ajax'

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep, cookies = req.requet2(target,
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest'
    	},
        cookies=cookies,
    	body='dwfrm_profile_customer_email=' + mail + '&dwfrm_profile_login_password=' + password + '&csrf_token=' + csrf_token
    )

    if debug:
        print(rep)

    if rep is None:
        return False, "Internet is down"

    if "\"success\": true" in rep:
        return True, cookies
    else:
        matches = re.findall(r"\"error\": \[[ \n]+?\"(.+?)\"[ \n]+?\],", rep, re.S)[0]
        if (len(matches) > 0):
            if (debug):
                print(matches)
            return False, matches[0]
        else:
            return False, "Unknown error"

def buy_shoe(site, cookies, url, pid, size, quantity, debug):
    '''
    Tries to add a product with given pied and size, returns success as boolean
    '''

    if (site == "solebox"):
        req = Requet(True, 'www.solebox.com', timeout=90)
        target = '/en_FR/add-product?format=ajax'
        origin = 'https://www.solebox.com'
    else:
        req = Requet(True, 'www.snipes.fr', timeout=60)
        target = '/on/demandware.store/Sites-snse-FR-Site/fr_FR/Cart-AddProduct?format=ajax'
        origin = 'https://www.snipes.fr'

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet(target,
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Origin': origin,
            'Referer': url
    	},
        cookies=cookies,
    	body='pid=' + pid + '&options=%5B%7B%22optionId%22%3A%22212%22%2C%22selectedValueId%22%3A%22' + size + '%22%7D%5D&quantity=' + quantity
    )

    if debug:
        print(rep)

    if rep is None:
        return False, "Internet is down"

    if (site == "solebox"):
        check = "\"message\": \"Product added to cart\""
    else:
        check = "\"message\": \"Ajouté\""

    if check in rep:
        return True, ""
    else:
        error = re.findall(r"\"message\": \"(.+?)\",", rep, re.S)
        if (len(error) > 0):
            return False, error[0]
        else:
            return False, "Anti-Bot Security (Consider changing IP)"

def get_product_page(cookies, url, debug):
    '''
    Gets content of product page to optimize requests
    '''
    #Remove variables from URL
    if ('?' in url):
        split = url.split('?')
        url = split[0]

    #Separate host from target
    split = url.split("/", 3)
    if (len(split) != 4):
        return None

    host = split[2]
    target = split[3]

    req = Requet(True, host, timeout=90)

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

    rep = req.requet('/' + target,
        method='get',
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
    	},
        cookies=cookies
        )

    if debug:
        print(rep)

    return rep

def get_pid(response, debug):
    '''
    Gets the product pid from given reponse (as string), returns success as string, either None or pid
    '''

    matches = re.findall('data-pid="(.+?)"', response)

    if len(matches) > 0:
        if debug:
            print(matches[0])
        return matches[0]
    else:
        return None

def get_available_shoes(site, response, debug):
    '''
    Gets available sizes for given response (as string). Returns list of available sizes, None if product is soldout
    '''

    if (site == "solebox"):
        regex = r"selectable[ \n]+?b-swatch-value--orderable[ \n]+?\"[ \n]+?>[ \n]+?([\.\d]+[ ]?[\d\/]+?)[ \n]+?<\/span>"
    else:
        regex = r"selectable[ \n]+?b-swatch-value--orderable[ \n]+?\">[ \n]+?([\.\d]+[ ]?[\d\/]+?)[ \n]+?<\/span>"

    matches = re.findall(regex, response, re.S)
    if len(matches) > 0:
        if debug:
            print(matches)
        return matches
    else:
        return None

def get_unique_pid(cookies, url, pid, size, debug):
    '''
    Gets size-related unique pid from given URL and model pid, returns success as string, either None or pid
    '''

    #Remove variables from URL
    if ('?' in url):
        split = url.split('?')
        url = split[0]

    #Separate host from target
    split = url.split("/", 3)
    if (len(split) != 4):
        return None

    host = split[2]
    target = split[3]

    #URL Encode size
    size = size.replace(" ", "%20")
    size = size.replace("/", "%2F")

    req = Requet(True, host, timeout=90)

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

    rep = req.requet('/' + target + '?chosen=size&dwvar_' + pid + '_212=' + size + '&format=ajax',
        method='get',
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
    	},
        cookies=cookies
        )

    if debug:
        print(rep)

    if rep is None:
        return None

    matches = re.findall(r"\"uuid\": \"[\w]+?\",[\n ]+?\"id\": \"([\d]+?)\"", rep, re.S)

    if len(matches) > 0:
        if debug:
            print(matches[0])
        return matches[0]
    else:
        return None

def get_quantity_available(cookies, url, pid, size, debug):
    '''
    Gets quantity available from given URL and model pid, returns success as string, either None or pid
    '''

    #Remove variables from URL
    if ('?' in url):
        split = url.split('?')
        url = split[0]

    #Separate host from target
    split = url.split("/", 3)
    if (len(split) != 4):
        return None

    host = split[2]
    target = split[3]

    #URL Encode size
    size = size.replace(" ", "%20")
    size = size.replace("/", "%2F")

    req = Requet(True, host, timeout=90)

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

    rep = req.requet('/' + target + '?chosen=size&dwvar_' + pid + '_212=' + size + '&format=ajax',
        method='get',
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
    	},
        cookies=cookies
        )

    if debug:
        print(rep)

    if rep is None:
        return None

    isLimited = re.findall(r"\"isLimited\": ([\w]+?),", rep, re.S)
    if (len(isLimited) > 0 and isLimited[0] == "true"):
        matches = re.findall(r"\"isLimitReached\": [\w]+?,[ \n]+?\"limitedTo\": ([\d]+?)[ \n]+?\}", rep, re.S)
    else:
        matches = re.findall(r"\"error\": [\w]+?,[ \n]+?\"available\": ([\d]+?)[ \n]+?\},", rep, re.S)

    if len(matches) > 0:
        if debug:
            print(matches[0])
        return matches[0]
    else:
        return None
