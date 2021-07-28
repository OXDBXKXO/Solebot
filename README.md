# Solebot

This project was realized as part of the selection process for an internship in sold-out.io. It no longer works, as both solebox.com and snipes.fr implemented anti-bot technologies.

# How to use the bot

Run main.py and use the menu. Websites supported at the moment are solebox.com and snipes.fr. For both websites, you can create accounts and add products to cart through an interactive prompt. Adding to cart can be automated via config files.

# How it works

For Account Creation, the bot fetches a valid csrf_token then uses it to post an account creation request. It's that simple.

For Adding An Article To Cart, the bot fetches a valid_csrf token then uses given credentials to login. The cookies obtained are used to add product to cart. The bot will fetch available size and maximum quantity allowed for provided product's link to help user create a valid request. The request is then created and sent to server.
