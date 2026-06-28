from functions.UsernameSniper import *

#Menu 1
def main():
    while True:
        os.system("cls")
        Slow(banner)
        print("")
        Slow(menu)

        command = input(f"""{Fore.RED} ┌──({Fore.WHITE}{username}{Fore.RED})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.RED}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
                
        if command == "1" or command == "01":
            asyncio.run(CheckName())
        elif command == "2" or command == "02":
            sys.exit()
                
main()