from lib import Requet, Log
import json

def solebox_create_user(email, password, debug):
    mail = email.replace('@', '%40')
    req = Requet(False, 'www.solebox.com')

    req.debug = True
    req.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

    rep = req.requet('/on/demandware.store/Sites-solebox-Site/en_FR/Account-SubmitRegistration?rurl=1&format=ajax',
    	method='post',
    	headers={
    		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://www.solebox.com'
    	},
        cookies='__cfduid=d123ae9b9fdbba5d75931bf63487ad7961591874808; dwsid=rkx8oJm1ZlEuZI-s1AUd01O_6O-NolbtFmD9irQf4_BKajSlVQ08dHElJxWA3odH_CU992G_nN1dUz05DV3-mg==; dwac_6915a153f1e2381a3decf47a04=JRUTrBzNbWSQBbWZm9cWBtjmh-MI2l3YqAE%3D|dw-only|||EUR|false|Europe%2FBerlin|true; sid=JRUTrBzNbWSQBbWZm9cWBtjmh-MI2l3YqAE; dwanonymous_0e5f1b8bd4b7e281cbecc26270bd55c1=abximE99b268auJVQuCLzXGevf; __cq_dnt=1; dw_dnt=1; test; _pxhd=28aa1be4c068a34c59e9a71dbcea4ed4e32ad618c39d529b5428a3fcda8f4e93:76d987a1-abd6-11ea-95dd-3587cd26823e; _gcl_au=1.1.562668024.1591874820; customerCountry=fr; _ga=GA1.2.1607499967.1591874823; _gid=GA1.2.2019216406.1591874823; _pxvid=76d987a1-abd6-11ea-95dd-3587cd26823e; hideLocalizationDialog=true; _fbp=fb.1.1591874830153.1517504993; _px3=0365771f561a046aec158edc09b8cfd79434870ae4e005aaf5ff896f06099c3e:yD4fNOVCzJDWJ5q9B31JDNb3f7ofeS0h0Llmi4nwZuPgCnXtI8Y92f/rApFm2bvv80mcLJkn0ZjMJeQwJL3L+g==:1000:4mghaN2WqaYja63zuLRSSxtScifQeqdMNLQrMYitB6Ra7Tz994I1xfFcjLc5Eqwz5NSBt2pGZ8OCK6FDxjnXJlZQ84XW4o6WxJUe6vV41UKKDokCYZi/b/JR8tVtlsiXYZwjok3MT4QnVooNPVQAo7q0SrBnOn9LbrtCii/u/C4=; _uetsid=0e9cb852-3f68-4237-5167-c60b20aea97b; _uetvid=dd4f966a-dec0-14b2-9d5c-fea46686f6fe; _gat_UA-3768969-1=1',
    	body='dwfrm_profile_register_title=mr&dwfrm_profile_register_firstName=TEST&dwfrm_profile_register_lastName=TEST&dwfrm_profile_register_email=' + mail + '&dwfrm_profile_register_emailConfirm=' + mail + '&dwfrm_profile_register_password=' + password + '&dwfrm_profile_register_passwordConfirm=' + password + '&dwfrm_profile_register_phone=&dwfrm_profile_register_birthday=&dwfrm_profile_register_acceptPolicy=true&csrf_token=rMX0KPRwjreSWDe8W9fSM7bdPSyJv1r1_qkzqa-ZA-LJ6twqebsCvElAGRy8iLnw6rIQH3Lt4vMpkwwZWvum_TLYHZuEKOIwlEKbXTtwg5SdrCMLsvk1PGt02nK_RQYRkNPNNsgrPeH9E6oiCVl8c333VynNx1ynGrS8F2aBiaQZGxncxeY%3D'
    )

    if debug:
        print(rep)

    return "\"form\": {\n\"valid\": true" in rep

solebox_create_user("test4@test.test", "TESTtest123", False)
