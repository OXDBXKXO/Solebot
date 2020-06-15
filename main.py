from solebox import *

################################################################################
#                                  SOLEBOX
################################################################################

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


if solebox_create_user(dwsid, csrf_token, email, password, debug):
    print("An error occured while creating new user")

cookies = solebox_login(dwsid, csrf_token, "test10@test.test", "TESTtest123", debug)

if cookies is not None:
    if solebox_buy_shoe(pid, size, cookies["dwsid"], debug):
        print("Product added successfuly")
    else:
        print("An error occured while adding product to cart")
else:
    print("An error occured during connection")


################################################################################
#                                  SNIPES
################################################################################
