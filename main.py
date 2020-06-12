from lib import Requet, Log


#CSRF bypass
dwsid = "g3RwuW3Z1eOFTltJ16egKtIbUYeWEcvLChCJ6A9zJWmPgUqO1KkQlLo2Oe8AyQsijW9jrXZgzYgQoitvjPnSeg=="
csrf_token = "sXAsYsdV_HVPif8NdXb6DY1FlXR6gyXacL7w7BgpdlAVgkqMM0gIhBAIkyw7YJjtBE721X68VyEFlLCi6sMZ6pGziBvYUW_s1prQb6o4qHKNc4U1jvKg0JStiTw1FHWCwaBWdbKODgMu10Mbl_jqPqt4HqlJAy9rzIwNHejzEgZaatei-Dc%3D"

#Credentials
email = "test10@test.test"
password = "TESTtest123"

#Product info
pid = "0181863000000008"
size = "44"

#Debug mode (True/False)
debug = False



def solebox_create_user(dwsid, csrf_token, email, password, debug):
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
        cookies=':__cfduid=d123ae9b9fdbba5d75931bf63487ad7961591874808; \
        dwanonymous_0e5f1b8bd4b7e281cbecc26270bd55c1=acZxdpaVm51ROHfzyF0BZEKdAO; \
        _pxhd=28aa1be4c068a34c59e9a71dbcea4ed4e32ad618c39d529b5428a3fcda8f4e93:76d987a1-abd6-11ea-95dd-3587cd26823e; \
        _gcl_au=1.1.562668024.1591874820; \
        customerCountry=fr; \
        _ga=GA1.2.1607499967.1591874823; \
        _gid=GA1.2.2019216406.1591874823; \
        _pxvid=76d987a1-abd6-11ea-95dd-3587cd26823e; \
        _fbp=fb.1.1591874830153.1517504993; \
        dwsid=' + dwsid + '; \
        dwac_6915a153f1e2381a3decf47a04=8GWa7R2N2PoL1MA6qDQGxSTH-EiJAxlPqkg%3D|dw-only|||EUR|false|Europe%2FBerlin|true; \
        sid=8GWa7R2N2PoL1MA6qDQGxSTH-EiJAxlPqkg; \
        __cq_dnt=1; \
        dw_dnt=1; \
        test; \
        hideLocalizationDialog=true; \
        _gat_UA-3768969-1=1; \
        _px3=85862b021d9e3c2e1e7ea0150446fa64d5b6113b5a0a6bc9284a8313451989ba:hR7FFjV0tJkH+Ilmm9ERxroRkskQ4YtKb3DqS/e9tkExuhV5lIaIv+2Kx9aDwJNcYhgbNUhMA04VJrYsw+ykwQ==:1000:f0SZHiA3SXzKhQQgAkk0AMD/7XYtfex5gQ7ojHhz4Fa29fLgmFKi/gMhBOTeh9JZ9+7Fcnd35tZWBL9v26lndmKw6LupvMYO2bGRPn6vEGAULteg4W2U76OUAdzKUGUUwfHumZ2XoaLYwhBGynoM/9aOV9yW1KmMVVzg926m+0A=; \
        _uetsid=0e9cb852-3f68-4237-5167-c60b20aea97b; \
        _uetvid=dd4f966a-dec0-14b2-9d5c-fea46686f6fe',
    	body='dwfrm_profile_register_title=mr&dwfrm_profile_register_firstName=TEST&dwfrm_profile_register_lastName=TEST&dwfrm_profile_register_email=' + mail + '&dwfrm_profile_register_emailConfirm=' + mail + '&dwfrm_profile_register_password=' + password + '&dwfrm_profile_register_passwordConfirm=' + password + '&dwfrm_profile_register_phone=&dwfrm_profile_register_birthday=&dwfrm_profile_register_acceptPolicy=true&csrf_token=' + csrf_token
    )

    if debug:
        print(rep)

    return "\"form\": {\n\"valid\": true" in rep

def solebox_login(dwsid, csrf_token, email, password, debug):
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
        cookies=':__cfduid=d123ae9b9fdbba5d75931bf63487ad7961591874808; \
        dwanonymous_0e5f1b8bd4b7e281cbecc26270bd55c1=acZxdpaVm51ROHfzyF0BZEKdAO; \
        _pxhd=28aa1be4c068a34c59e9a71dbcea4ed4e32ad618c39d529b5428a3fcda8f4e93:76d987a1-abd6-11ea-95dd-3587cd26823e; \
        _gcl_au=1.1.562668024.1591874820; \
        customerCountry=fr; \
        _ga=GA1.2.1607499967.1591874823; \
        _gid=GA1.2.2019216406.1591874823; \
        _pxvid=76d987a1-abd6-11ea-95dd-3587cd26823e; \
        _fbp=fb.1.1591874830153.1517504993; \
        dwsid=' + dwsid + ' \
        dwac_6915a153f1e2381a3decf47a04=8GWa7R2N2PoL1MA6qDQGxSTH-EiJAxlPqkg%3D|dw-only|||EUR|false|Europe%2FBerlin|true; \
        sid=8GWa7R2N2PoL1MA6qDQGxSTH-EiJAxlPqkg; \
        __cq_dnt=1; \
        dw_dnt=1; \
        test; \
        hideLocalizationDialog=true; \
        _gat_UA-3768969-1=1; \
        _px3=85862b021d9e3c2e1e7ea0150446fa64d5b6113b5a0a6bc9284a8313451989ba:hR7FFjV0tJkH+Ilmm9ERxroRkskQ4YtKb3DqS/e9tkExuhV5lIaIv+2Kx9aDwJNcYhgbNUhMA04VJrYsw+ykwQ==:1000:f0SZHiA3SXzKhQQgAkk0AMD/7XYtfex5gQ7ojHhz4Fa29fLgmFKi/gMhBOTeh9JZ9+7Fcnd35tZWBL9v26lndmKw6LupvMYO2bGRPn6vEGAULteg4W2U76OUAdzKUGUUwfHumZ2XoaLYwhBGynoM/9aOV9yW1KmMVVzg926m+0A=; \
        _uetsid=0e9cb852-3f68-4237-5167-c60b20aea97b; \
        _uetvid=dd4f966a-dec0-14b2-9d5c-fea46686f6fe',
    	body='dwfrm_profile_customer_email=' + mail + '&dwfrm_profile_login_password=' + password + '&csrf_token=' + csrf_token
    )

    if debug:
        print(rep)

    if "\"success\": true" in rep:
        return cookies
    else:
        return None

def solebox_buy_shoe(pid, size, dwsid, debug):
    '''
    Tries to add a product with given pid and size, returns success as boolean
    '''
    req = Requet(True, 'www.solebox.com')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet('/en_FR/add-product?format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.solebox.com',
            'referer': 'https://www.solebox.com/en_FR/p/vans-vault_ua_og_chukka_lx_x_fergus_purcell-cornershop%2Fdrink-01818630.html'
    	},
        cookies='test; __cfduid=d123ae9b9fdbba5d75931bf63487ad7961591874808; \
        dwanonymous_0e5f1b8bd4b7e281cbecc26270bd55c1=acZxdpaVm51ROHfzyF0BZEKdAO; \
        _pxhd=28aa1be4c068a34c59e9a71dbcea4ed4e32ad618c39d529b5428a3fcda8f4e93:76d987a1-abd6-11ea-95dd-3587cd26823e; _gcl_au=1.1.562668024.1591874820; customerCountry=fr; _ga=GA1.2.1607499967.1591874823; _gid=GA1.2.2019216406.1591874823; _pxvid=76d987a1-abd6-11ea-95dd-3587cd26823e; _fbp=fb.1.1591874830153.1517504993; dwsid=' + dwsid + '; dwac_6915a153f1e2381a3decf47a04=ZbxwRG86yw36dFxhUsdrEMrh3wo_J5Eknsc%3D|dw-only|||EUR|false|Europe%2FBerlin|true; sid=ZbxwRG86yw36dFxhUsdrEMrh3wo_J5Eknsc; __cq_dnt=1; dw_dnt=1; test; hideLocalizationDialog=true; acceptCookie=true; _uetsid=0e9cb852-3f68-4237-5167-c60b20aea97b; _uetvid=dd4f966a-dec0-14b2-9d5c-fea46686f6fe',
    	body='pid=' + pid + '&options=%5B%7B%22optionId%22%3A%22212%22%2C%22selectedValueId%22%3A%22' + size +'%22%7D%5D&quantity=1'
    )

    if debug:
        print(rep)

    return "\"error\": false" in rep



if solebox_create_user(dwsid, csrf_token, email, password, debug):
    print("An error occured while creating new user")

cookies = solebox_login(dwsid, csrf_token, email, password, debug)

if cookies is not None:
    if solebox_buy_shoe(pid, size, cookies["dwsid"], debug):
        print("Product added successfuly")
    else:
        print("An error occured while adding product to cart")
else:
    print("An error occured during connection")
