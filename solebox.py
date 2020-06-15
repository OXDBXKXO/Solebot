from request import Requet, Log
import re

def solebox_get_csrf_token(debug):
    '''
    Gets csrf_token needed for further operations
    '''
    req = Requet(True, 'www.solebox.com')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

    rep, cookies = req.requet2('/en_FR/login',
        method='get',
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
    	}
        )

    matches = re.findall('csrf_token" value="(.+?)"', rep)

    if len(matches) > 0:
        return matches[0], cookies
    else:
        return None, None

def solebox_create_user(cookies, csrf_token, gender, firstName, lastName, email, password, debug):
    '''
    Tries to create a new user with given arguments, returns success as boolean
    '''
    mail = email.replace('@', '%40')
    req = Requet(True, 'www.solebox.com')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet('/on/demandware.store/Sites-solebox-Site/en_FR/Account-SubmitRegistration?rurl=1&format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.solebox.com'
    	},
        cookies=cookies,
    	body='dwfrm_profile_register_title=' + gender + '&dwfrm_profile_register_firstName=' + firstName + '&dwfrm_profile_register_lastName=' + lastName + '&dwfrm_profile_register_email=' + mail + '&dwfrm_profile_register_emailConfirm=' + mail + '&dwfrm_profile_register_password=' + password + '&dwfrm_profile_register_passwordConfirm=' + password + '&dwfrm_profile_register_phone=&dwfrm_profile_register_birthday=&dwfrm_profile_register_acceptPolicy=true&csrf_token=' + csrf_token
    )

    if debug:
        print(rep)

    return "\"success\": true" in rep

def solebox_login(cookies, csrf_token, email, password, debug):
    '''
    Tries to login with given arguments, returns success as a dictionary, either None or containing session cookies
    '''
    mail = email.replace('@', '%40')
    req = Requet(True, 'www.solebox.com')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep, cookies = req.requet2('/en_FR/authentication?rurl=1&format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.solebox.com'
    	},
        cookies=cookies,
    	body='dwfrm_profile_customer_email=' + mail + '&dwfrm_profile_login_password=' + password + '&csrf_token=' + csrf_token
    )

    if debug:
        print(rep)

    if "\"success\": true" in rep:
        return cookies
    else:
        return None

def solebox_buy_shoe(cookies, pid, size, quantity, debug):
    '''
    Tries to add a product with given pied and size, returns success as boolean
    '''
    req = Requet(True, 'www.solebox.com')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet('/en_FR/add-product?format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.solebox.com'
    	},
        cookies=cookies,
    	body='pid=' + pid + '&options=%5B%7B%22optionId%22%3A%22212%22%2C%22selectedValueId%22%3A%22' + size + '%22%7D%5D&quantity=' + quantity
    )

    if debug:
        print(rep)

    return "\"error\": false" in rep

def solebox_get_pid(cookies, url, debug):
    '''
    Get the product pid from given URL, returns success as string, either None or pid
    '''

    split = url.split("/", 3)

    if (len(split) != 4):
        return None

    host = split[2]
    target = split[3]

    req = Requet(True, host, timeout=30)

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

    matches = re.findall('data-pid="(.+?)"', rep)

    if len(matches) > 0:
        if debug:
            print(matches[0])
        return matches[0]
    else:
        return None
