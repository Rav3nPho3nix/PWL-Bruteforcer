import requests
from pystyle import *
banner = '''                                                                                        
 _____ _ _ _ __       _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|  _  | | | |  |     | __  | __  |  |  |_   _|   __|   __|     | __  |     |   __| __  |
|   __| | | |  |__   | __ -|    -|  |  | | | |   __|   __|  |  |    -|   --|   __|    -|
|__|  |_____|_____|  |_____|__|__|_____| |_| |_____|__|  |_____|__|__|_____|_____|__|__| v1.0 '''
print(banner)
print("\nWEBSITE BRUTE-FORCER BY @Rav3nPho3nix")
url = input("Enter the url: ")
file_path = input("Drag/Drop your wordlist file: ")
with open(file_path, 'r') as file:
    words = [line.strip() for line in file]
for word in words:
    yel = Colors.yellow
    r = requests.get(f'{url}/{word}')
    if r.status_code == 200:
        print(Colors.yellow+f">> {url}{word} | Status:{r.status_code}"+Colors.white)
    else:
        print(f"> {url}{word} | Status:{r.status_code}")
