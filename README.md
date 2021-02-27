# NordVPN Account and Connection Checker

**ONLY WORKS ON LINUX!**

A script that takes a .txt file as a password Inupt and tries to login and then connect to a server. If the account information is wrong or the connection fails, the script just moves on to the next entry.

## Before you use this:

I am a very new to both python and programming for linux so don't expect the best code. **This code is a modification** from [Behnambm's NordVPN checker](https://github.com/behnambm/nordvpn-checker). His code only checks for valid accounts and doesn't try to connect to a server. Because these accounts are often shared, only 6 people are allowed to have an active connection per account so this script checks for open slots. Full credit for his code goes to him, definetly check him out.

## You will need:

- [The NordVPN CLI tool](https://nordvpn.com/download/linux/).
- [Python 3](https://www.python.org/downloads/).
- An input .txt file containing NordVPN login entries in the  `email:password` format. Every new line is a new account.

## Usage

Clone the repository or download the python script, make sure you have the Requirements installed, navigate to the python script with cd and run:
```
$ python3 accountChecker.py -f <FilePath>
```

The FilePath should lead to your accounts text file. This process can take a while. It takes at least a few seconds for every account entry so just be patient. 
## Problems and bugs
Sometimes your browser might automatically open with the nordvpn website. I am not 100% sure why this is, but I think it is because the subscription of the given account has run out. You can just ignore it and close your browser. If all the error outputs are "Failed to Login" and are finished very fast even though the login information should work, it could be that there is a problem with NordVPN. Try connecting to an account manually and if you get the `Whoops! We're having trouble reaching our servers...` Problem you might want to try to restart your pc or someting. I'm not sure what a good fix is, but if you can't login manually, the script won't work either.
## How to connect to specifc Countries
Open the python script with any IDE of your choice and change `'canada'` in line 37 to any country you want. You can also delete the country all together and just write `['nordvpn', 'c']` then you will be automatically connected to the country with the best connection.
## Please Comment
Like I said I am very new to this and by no means perfect code. I am very much open to suggestions, so leave a comment! Thanks again to behnambm for the code! I will probably not be working on this script a lot more but there are some things to do like an easier country selection so definetly leave requests as well.
