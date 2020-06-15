# Solebot

This project has been realized as part of the selection process for an internship in sold-out.io, a start-up which
aims to rebalance chances between fans of limited edition sneakers. Indeed, current market is dominated by expensive
bots that offer unfair advantage to their users, by allowing them to buy hundreds of pairs, as limited releases follow
the "first come, first serve" rule. Sold-out provides a bot for everyone to use.

# How to use the bot

Both solebox.com and snipes.fr use anti-CSRF attack tokens, so you must get a valid pair of dwsid cookie / csrf_token.
As both websites use Saleforces.com's Commerce-Cloud for hosting, the same token will work for both website.

### Get valid csrf_token
1) Reach login page of solebox.com or snipes.fr
2) Open Developer Tools (F12 for Chrome and Safari)
3) Choose 'Network' tab
4) Enter valid email and random password, then click 'Login'
5) Check the 'Network' tab for a POST request directed to '/authentication?rurl=1&format=ajax'
6) Click on the request to explore its data
7) In 'Cookies' tab, locate the 'dwsid' cookie and copy its value in main.py
8) In 'Request' tab, locate the 'csrf_token' field and copy its value in main.py
9) Edit login info in main.py
    
### Get started
Once you got a valid csrf_token, you're good to go ! By default, the script will try to create the account given in parameters,
then login and add the desired product (using its pid) to the cart
