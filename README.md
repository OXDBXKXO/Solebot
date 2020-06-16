# Solebot

This project has been realized as part of the selection process for an internship in sold-out.io, a start-up which
aims to rebalance chances between fans of limited edition sneakers. Indeed, current market is dominated by expensive
bots that offer unfair advantage to their users, by allowing them to buy hundreds of pairs, as limited releases follow
the "first come, first serve" rule. Sold-out provides a bot for everyone to use.

# How to use the bot

Run main.py and use the menu. Websites supported at the moment are solebox.com and snipes.fr. For both websites, you can create accounts and add products to cart through an interactive prompt. Adding to cart can be automated via config files.

# How it works

For Account Creation, the bot fetches a valid csrf_token then uses it to post an account creation request. It's that simple.
For Adding An Article To Cart, the bot fetches fetches a valid_csrf token then uses given credentials to login. The cookies obtained are used to add product to cart. The bot will fetch available size and maximum quantity allowed for provided product's link. The request is then created and sent to server.
