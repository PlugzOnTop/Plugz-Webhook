import os
import requests
import time
from threading import Thread
from colorama import init, Fore, Back, Style
import os.path
import ctypes
from colorama import Fore
from time import sleep
from pystyle import *

warning = """     
        ╔═╗╔╦╗╦ ╦╔═╗╔═╗╔╦╗╦╔═╗╔╗╔╔═╗╦      
        ║╣  ║║║ ║║  ╠═╣ ║ ║║ ║║║║╠═╣║      
        ╚═╝═╩╝╚═╝╚═╝╩ ╩ ╩ ╩╚═╝╝╚╝╩ ╩╩═╝    
        ╔═╗╦ ╦╦═╗╔═╗╔═╗╔═╗╔═╗╔═╗  ╔═╗╔╗╔╦ ╦ ╦
        ╠═╝║ ║╠╦╝╠═╝║ ║╚═╗║╣ ╚═╗  ║ ║║║║║ ╚╦╝
        ╩  ╚═╝╩╚═╩  ╚═╝╚═╝╚═╝╚═╝  ╚═╝╝╚╝╩═╝╩ 
        """
print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter(warning)))
time.sleep(3)

ctypes.windll.kernel32.SetConsoleTitleW("Plugz Webhook Tools | .gg/logger")


def deletewebhook(url):
	return requests.delete(url)


os.system('cls')


logo = """
                /$$$$$$$  /$$                                                     
                | $$__  $$| $$                                                     
                | $$  \ $$| $$ /$$   /$$  /$$$$$$  /$$$$$$$$                       
                | $$$$$$$/| $$| $$  | $$ /$$__  $$|____ /$$/                       
                | $$____/ | $$| $$  | $$| $$  \ $$   /$$$$/                        
                | $$      | $$| $$  | $$| $$  | $$  /$$__/                         
                | $$      | $$|  $$$$$$/|  $$$$$$$ /$$$$$$$$                       
                |__/      |__/ \______/  \____  $$|________/                       
                                        /$$  \ $$                                 
                                        |  $$$$$$/                                 
                                        \______/                                  
        /$$      /$$           /$$       /$$                           /$$      
        | $$  /$ | $$          | $$      | $$                          | $$      
        | $$ /$$$| $$  /$$$$$$ | $$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$
        | $$/$$ $$ $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/
        | $$$$_  $$$$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/ 
        | $$$/ \  $$$| $$_____/| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_  $$ 
        | $$/   \  $$|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$
        |__/     \__/ \_______/|_______/ |__/  |__/ \______/  \______/ |__/  \__/
                                                                         
                    ╔════════════════════════════════════════╗
                    ║              1 > Deleter               ║
                    ║              2 > Spammer               ║ 
                    ║              3 > Info                  ║
                    ╚════════════════════════════════════════╝         
                                   PRESS ENTER                                   
        """
Anime.Fade(Center.Center(logo), Colors.green_to_cyan, Colorate.Vertical, interval=0.025, enter=True)

print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter(logo)))

choice = Write.Input("Choose -> ", Colors.green_to_cyan, interval=0.008)

if choice == '1':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Plugz Webhook Tools | Deleter | .gg/logger")
        webhook = Write.Input("Webhook URL -> ", Colors.green_to_cyan, interval=0.008)
        deletewebhook(webhook)


elif choice == "2":
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Plugz Webhook Tools | Spammer | .gg/logger")
        actual = Write.Input("Webhook URL -> ", Colors.green_to_cyan, interval=0.008)
        msg = Write.Input("Message -> ", Colors.green_to_cyan, interval=0.008)
        for x in range(1000):
            print('Sent Message ' + msg)
            sendwebhook = requests.post(actual, json={'content': msg})
        time.sleep(0)


elif choice == "3":
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Plugz Webhook Tools | Info | .gg/logger")
        warning = """     
        Proudly Made By: Verse#2963 | Made For: plugz#7397
        Features: Webhook Spammer And Deleter
        Version: 1.0.0.0
        Updates: 0
        More Info: .gg/logger
        """
        print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter(warning)))
        time.sleep(7)