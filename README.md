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
>`python3 accountChecker.py -f <FilePath>`

The FilePath shuold lead to your accounts text file. This process can take a while. It takes at least a few seconds for every account entry so just be patient. Sometimes your browser might automatically open with the nordvpn website. I am not 100% sure why this is, but I think it is because the subscription of the given account has run out. You can just ignore it and close your browser.
