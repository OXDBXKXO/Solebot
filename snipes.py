from request import Requet, Log

def snipes_create_user(dwsid, csrf_token, email, password, debug):
    '''
    Tries to create a new user with given arguments, returns success as boolean
    '''
    mail = email.replace('@', '%40')
    req = Requet(True, 'www.snipes.fr')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet('/on/demandware.store/Sites-snse-FR-Site/fr_FR/Account-SubmitRegistration?rurl=1&format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.snipes.fr'
    	},
        cookies='__cfduid=d32c0115900f91834eb15d6699395cea11592231557; \
        dwac_b78308dbaa35331802b697f4fd=7LBiMHKKyVwpNu1wGnx4fUZIdq5_du5Cob0%3D|dw-only|||EUR|false|Europe%2FBerlin|true; \
        cqcid=debO3fMb71mcO20EpaR90cLiti; \
        dwanonymous_9d5ff9e4444e5b7160ea60697b69e60f=debO3fMb71mcO20EpaR90cLiti; \
        sid=7LBiMHKKyVwpNu1wGnx4fUZIdq5_du5Cob0; \
        __cq_dnt=0; \
        dw_dnt=0; \
        dwsid=' + dwsid + '; \
        test; \
        _pxhd=4b10b97743ae79b8db53809f643571bd714951a87223f3c1c838630a9f22e93b:14f36191-af15-11ea-8ab2-1511889cdcf4; \
        _gcl_au=1.1.1639395752.1592231568; \
        customerCountry=fr; \
        scarab.visitor=%22387988C27C3662EB%22; \
        _pxvid=14f36191-af15-11ea-8ab2-1511889cdcf4; \
        _ga=GA1.2.1244552872.1592231576; \
        _gid=GA1.2.1660666474.1592231576; \
        _px3=e5de32f99bdbc26a765778ad147ad49d2c24acc1e0b0b03c14401bb6709b3d7b:DgoXQaa/VLZYBd674h9AFfjh9uZxpUGjKJBSjxGNkBJTJOQTlSXXD4syOCCuvHUsd4Nwu3+bOJD5M3we0PnEzg==:1000:X4bI4Jf8wdsssNvf/LxnaSNRbv0Q2BR330OxVJctU/jr3ala/FLdyLSGVwnuRRX/v3xXA/F36lVH2dr6S56UYDYKwfmzb16BhZuKI5oSFjI052Ocs/nBuERBtGtU4i/4g2LH5ruTOUkHVuU/USYIWr5EZgRtnqQsBT/k/UYf/0w=; \
        __cq_uuid=1735b070-af15-11ea-b427-63494b46880e; \
        __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; \
        _uetsid=64dcb78c-aa28-9028-6d54-44a9a8fbf7ba; \
        _uetvid=18eeb148-f51e-1682-9f12-ac021fce8e83; \
        _fbp=fb.1.1592231596473.2000859664; \
        hideHeaderContent=true',


    	body='dwfrm_profile_register_title=mr&dwfrm_profile_register_firstName=Test&dwfrm_profile_register_lastName=TEST&dwfrm_profile_register_email=' + email + '&dwfrm_profile_register_emailConfirm=' + email + '&dwfrm_profile_register_password=' + password + '&dwfrm_profile_register_passwordConfirm=' + password + '&dwfrm_profile_register_phone=&dwfrm_profile_register_birthday=&dwfrm_profile_register_acceptPolicy=true&csrf_token=' + csrf_token
    )

    if debug:
        print(rep)

    return "\"success\": true" in rep

def snipes_login(dwsid, csrf_token, email, password, debug):
    '''
    Tries to login with given arguments, returns success as a dictionary, either None or containing session cookies
    '''
    mail = email.replace('@', '%40')
    req = Requet(True, 'www.snipes.fr')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep, cookies = req.requet2('/authentication?rurl=1&format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.snipes.fr'
    	},
        cookies=':__cfduid=d32c0115900f91834eb15d6699395cea11592231557; \
        dwac_b78308dbaa35331802b697f4fd=7LBiMHKKyVwpNu1wGnx4fUZIdq5_du5Cob0%3D|dw-only|||EUR|false|Europe%2FBerlin|true; \
        cqcid=debO3fMb71mcO20EpaR90cLiti; \
        dwanonymous_9d5ff9e4444e5b7160ea60697b69e60f=debO3fMb71mcO20EpaR90cLiti; \
        sid=7LBiMHKKyVwpNu1wGnx4fUZIdq5_du5Cob0; \
        __cq_dnt=0; \
        dw_dnt=0; \
        dwsid=' + dwsid + '; \
        test; \
        _pxhd=4b10b97743ae79b8db53809f643571bd714951a87223f3c1c838630a9f22e93b:14f36191-af15-11ea-8ab2-1511889cdcf4; \
        _gcl_au=1.1.1639395752.1592231568; \
        customerCountry=fr; \
        scarab.visitor=%22387988C27C3662EB%22; \
        _pxvid=14f36191-af15-11ea-8ab2-1511889cdcf4; \
        _ga=GA1.2.1244552872.1592231576; \
        _gid=GA1.2.1660666474.1592231576; \
        _px3=e5de32f99bdbc26a765778ad147ad49d2c24acc1e0b0b03c14401bb6709b3d7b:DgoXQaa/VLZYBd674h9AFfjh9uZxpUGjKJBSjxGNkBJTJOQTlSXXD4syOCCuvHUsd4Nwu3+bOJD5M3we0PnEzg==:1000:X4bI4Jf8wdsssNvf/LxnaSNRbv0Q2BR330OxVJctU/jr3ala/FLdyLSGVwnuRRX/v3xXA/F36lVH2dr6S56UYDYKwfmzb16BhZuKI5oSFjI052Ocs/nBuERBtGtU4i/4g2LH5ruTOUkHVuU/USYIWr5EZgRtnqQsBT/k/UYf/0w=; \
        __cq_uuid=1735b070-af15-11ea-b427-63494b46880e; \
        __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; \
        _uetsid=64dcb78c-aa28-9028-6d54-44a9a8fbf7ba; \
        _uetvid=18eeb148-f51e-1682-9f12-ac021fce8e83; \
        _fbp=fb.1.1592231596473.2000859664; \
        hideHeaderContent=true',


    	body='dwfrm_profile_customer_email=' + mail + '&dwfrm_profile_login_password=' + password + '&csrf_token=' + csrf_token
    )

    if debug:
        print(rep)

    if "\"success\": true" in rep:
        return cookies
    else:
        return None

def snipes_buy_shoe(pid, size, dwsid, debug):
    '''
    Tries to add a product with given pied and size, returns success as boolean
    '''
    req = Requet(True, 'www.snipes.fr')

    req.debug = debug
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet('/on/demandware.store/Sites-snse-FR-Site/fr_FR/Cart-AddProduct?format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.snipes.fr'
    	},
        cookies=':__cfduid=d32c0115900f91834eb15d6699395cea11592231557; \
        dwac_b78308dbaa35331802b697f4fd=7LBiMHKKyVwpNu1wGnx4fUZIdq5_du5Cob0%3D|dw-only|||EUR|false|Europe%2FBerlin|true; \
        cqcid=debO3fMb71mcO20EpaR90cLiti; \
        dwanonymous_9d5ff9e4444e5b7160ea60697b69e60f=debO3fMb71mcO20EpaR90cLiti; \
        sid=7LBiMHKKyVwpNu1wGnx4fUZIdq5_du5Cob0; \
        __cq_dnt=0; \
        dw_dnt=0; \
        dwsid=' + dwsid + '; \
        test; \
        _pxhd=4b10b97743ae79b8db53809f643571bd714951a87223f3c1c838630a9f22e93b:14f36191-af15-11ea-8ab2-1511889cdcf4; \
        _gcl_au=1.1.1639395752.1592231568; \
        customerCountry=fr; \
        scarab.visitor=%22387988C27C3662EB%22; \
        _pxvid=14f36191-af15-11ea-8ab2-1511889cdcf4; \
        _ga=GA1.2.1244552872.1592231576; \
        _gid=GA1.2.1660666474.1592231576; \
        _px3=e5de32f99bdbc26a765778ad147ad49d2c24acc1e0b0b03c14401bb6709b3d7b:DgoXQaa/VLZYBd674h9AFfjh9uZxpUGjKJBSjxGNkBJTJOQTlSXXD4syOCCuvHUsd4Nwu3+bOJD5M3we0PnEzg==:1000:X4bI4Jf8wdsssNvf/LxnaSNRbv0Q2BR330OxVJctU/jr3ala/FLdyLSGVwnuRRX/v3xXA/F36lVH2dr6S56UYDYKwfmzb16BhZuKI5oSFjI052Ocs/nBuERBtGtU4i/4g2LH5ruTOUkHVuU/USYIWr5EZgRtnqQsBT/k/UYf/0w=; \
        __cq_uuid=1735b070-af15-11ea-b427-63494b46880e; \
        __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; \
        _uetsid=64dcb78c-aa28-9028-6d54-44a9a8fbf7ba; \
        _uetvid=18eeb148-f51e-1682-9f12-ac021fce8e83; \
        _fbp=fb.1.1592231596473.2000859664; \
        hideHeaderContent=true',


    	body='pid=' + pid + '&options=%5B%7B%22optionId%22%3A%22212%22%2C%22selectedValueId%22%3A%22' + size + '%22%7D%5D&quantity=1'
    )

    if debug:
        print(rep)

    return "\"error\": false" in rep
