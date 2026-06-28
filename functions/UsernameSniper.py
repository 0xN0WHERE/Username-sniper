from config.settings import *
import secrets

token = MyToken()

def GenUser():
    chars = string.ascii_lowercase + string.digits + "_."
    return ''.join(secrets.choice(chars) for _ in range(4))

async def CheckName():
    os.system("cls")
    Slow(discord_banner)
    time.sleep(1.5)
    os.system("cls")
    print(f"{bracketopen}!{bracketclosed} {Fore.RED}Username sniper{Style.RESET_ALL}")
    print("")

    try:
        webhook = input(f"{bracketopen}>{bracketclosed} {Fore.RED}Webhook url -> {Style.RESET_ALL}")

        res = requests.get(webhook)

        if not res.status_code in succesStatus:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.RED} Invalid webhook url{Style.RESET_ALL}")
            time.sleep(2)
            return
        
        if token is None:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.RED} Failed to grab token{Style.RESET_ALL}")
            time.sleep(2)
            return

        headers ={
            "Authorization": token,
            "content-type": "application/json"
        }


        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.RED} Sniping usernames...{Style.RESET_ALL}")
        print("")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        while True:
            try:
                r = requests.post(
                    "https://discord.com/api/v9/users/@me/pomelo-attempt",
                    json={"username": GenUser()},
                    headers=headers,
                    timeout=5
                )
            except Exception:
                pass

            if r.status_code in succesStatus:
                data = r.json()

                if data.get("taken") is True:
                    print(f"{bracketopen2}{Fore.RED}+{Style.RESET_ALL}{bracketclosed2}{Fore.RED} Username taken  :{Style.RESET_ALL}  {GenUser()}")
                else:
                    message = {
                        "content": f"**[**+**]** ** Username available  :**  `{GenUser()}`"
                    }
                    response = requests.post(webhook, json=message) 

            elif r.status_code == 429:
                Retry = r.json().get("retry_after", 5)
                await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
            else:
                print(f"{bracketopen2}{Fore.RED}+{Style.RESET_ALL}{bracketclosed2}{Fore.RED} Failed to check :{Style.RESET_ALL}  {GenUser()}")
                
    except Exception as e:
        print("")
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.RED} Webhook unavailable{Style.RESET_ALL}")
        time.sleep(2)
    
    return None