import requests
import random
import time
import os
from colorama import Fore

print("   _____             ____  _                   ")
print("  |__  /__ _  __ _  / ___|| |_ ___  _ __ ___   ")
print("    / // _` |/ _` | \___ \| __/ _ \| '__/ _ \  ")
print("   / /| (_| | (_| |  ___) | || (_) | | |  __/  ")
print("  /____\__,_|\__,_| |____/ \__\___/|_|  \___|  \n")
print("=================================================")
author = "Zaa レム"
print("Author : " + author)
script = "Auto Post Discord"
print("Script : " + script)
discord = "Zaa Store"
print("Discord Name : " + discord)
dcurl = "https://discord.gg/GU3kzPRask"
print("Discord Url : " + dcurl)
print("===========================================")
print('YANG RESELL ANAK YATIM')
print("===========================================\n")

time.sleep(1)

channel_id = input("Masukkan ID channel: ")
time1 = int(input("Set Time Post 1 : "))
time2 = int(input("Set Time Post 2 : "))
time3 = int(input("Set Time Post 3 : "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.read()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': words.strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            else:
                time.sleep(time1)

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            else:
                time.sleep(time2)

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            else:
                time.sleep(time3)

