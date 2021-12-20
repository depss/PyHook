from dhooks import Webhook
from colorama import Fore, Back, Style
import time
import colorama
import os

colorama.init()
logo = Fore.YELLOW + '''
 ▄▄▄· ▄· ▄▌ ▄ .▄            ▄ •▄ 
▐█ ▄█▐█▪██▌██▪▐█ ▄█▀▄  ▄█▀▄ █▌▄▌▪
 ██▀·▐█▌▐█▪██▀▀█▐█▌.▐▌▐█▌.▐▌▐▀▀▄·
▐█▪·• ▐█▀·.██▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌
.▀     ▀ • ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀
----------------------------------
Written by: depss
----------------------------------
    '''

print(Fore.YELLOW + '''
 ▄▄▄· ▄· ▄▌ ▄ .▄            ▄ •▄ 
▐█ ▄█▐█▪██▌██▪▐█ ▄█▀▄  ▄█▀▄ █▌▄▌▪
 ██▀·▐█▌▐█▪██▀▀█▐█▌.▐▌▐█▌.▐▌▐▀▀▄·
▐█▪·• ▐█▀·.██▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌
.▀     ▀ • ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀
----------------------------------
Written by: depss
----------------------------------
    ''') 
print(Fore.CYAN)
hook = Webhook(input('Webhook Url:\r\n'))
hook.get_info()

def main():
    mod = input("Would you like to change or modify your webhook?[Y/N]: ")

    if mod == "Y":
        os.system('cls')
        print(logo)
        pass
    if mod == "N":
        os.system('cls')
        message()

    print(Fore.CYAN)
    a = input("Would you like to change the webhook name?[Y/N]: ")
    if a == 'Y':
        print(Fore.GREEN)
        usrnm = input("Webhook name:\r\n")
        hook.username = usrnm
    else:
        pass

    print(Fore.CYAN)
    c = input("Would you like to change your webhook Avatar?[Y/N]: ")
    if c == "Y":
        print(Fore.GREEN)
        picurl = input("Picture Url: ")
        hook.avatar_url = picurl
        os.system('cls')
        message()
    else:
        os.system('cls')
        message()

def message():
    print(logo)
    print(Fore.CYAN)
    msg = input("What message would you like to send: ")
    hook.send(msg)
    time.sleep(1.5)
    print(Fore.GREEN)
    print('Message Sent!')

    print(Fore.MAGENTA)
    rerun = input("Would you like to rerun?[Y/N]: ")
    if rerun == "Y":
        os.system('cls')
        print(logo)
        print(Fore.CYAN)
        main()
    else:
        exit()


if __name__ == '__main__':
    main()
