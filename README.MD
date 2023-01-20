** Script used to walk through several housing queues and do a login

Usage:
1 - Install packages from requirements.txt
2 - create a telegram bot and get the token (https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/#:~:text=Type%20%2Fnewbot%20%2C%20and%20follow%20the,access%20to%20the%20Telegram%20API.&text=Note%3A%20Make%20sure%20you%20store,can%20easily%20manipulate%20your%20bot.)
3 - Walk through all websites mentioned in "generic_sites.py & "non_generic_sites.py and register an account with each one
4 - Update Account object for each website with the correct credentials (login, password, phrase to check at the website if the login was successful -> typically makes sense to check your Last Name). I created a files module/secrets.py to store the passwords
5 - Run the script using run.py file