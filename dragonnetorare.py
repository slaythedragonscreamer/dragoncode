import ctypes
import os
import keyboard
import time
import win32api,win32gui
import mss
import PIL.ImageGrab
import PIL.Image
import winsound
import threading
import mouse
import subprocess
import requests
import sys
from colorama import Fore, Style, init
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile

class CColor:
        Red = '\u001B[31m'
        Green = '\u001B[32m'
        Yellow = '\u001B[33m'
        Blue = '\u001b[34m'
        Cyan = '\u001b[36m'
        White = '\u001B[37m'
        Bold ='\u001B[1m'
        
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://github.com/slaythedragonscreamer/dragoncode/blob/main/dragonname.txt")

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.07)

def Main_Program():
    if hwid in r.text:
        os.system("cls")
        Color = CColor()
        printSlow(f"{Color.Green}Access Granted!\r\n")
        time.sleep(0)
        print(f"\r\n")
        
    else:
        os.system("cls")
        Color = CColor()
        print(f"{Color.White}Token License Kamu{Color.Red} UNVERIFIED!")
        print(f"{Color.Yellow}Copy-Paste Kode Token di bawah ke{Color.Cyan} Discord{Color.Green} Zexal#9709\r\n\r\n\r\n")
        printSlow(f"{Color.Red}Kode Request License: {Color.White}\r\n" + hwid)
        print(f"\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n")
        print(f"{Color.Red}==================================================================")
        print(f"{Color.Yellow} Copyright 2020–2023 Outlaws Triggerbot")
        print(f"{Color.Yellow}               ALL RIGHTS RESERVED.")
        print(f"{Color.Red}==================================================================")
        print(f"{Color.Red} Instagram : {Color.Yellow}@jualcheatvalorantindo")
        print(f"{Color.Red} Discord   : {Color.Yellow}Zexal#9709")
        print(f"{Color.Red} Server    : {Color.Yellow}discord.gg/uwwp9U6DJD")
        os.system('pause >NUL')
        os._exit(1)

if __name__ == "__main__":
    Main_Program()
    
banner = r"""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀     ▓▓▓▓▓▀▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀       ▄▓▓▓    ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▄      ▐▓▓▀      ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀╦╜      ▄▓║╛     ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀╔╜      ▄▀╓╩      ╓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▄▀▄╝      ╓▓▓▓▀▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ╓▓▓ ─      ╔▓▓▀    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ╔▓▓▓      ▄▓▓▀      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ╔▓▓ ▓▓    ┌▓▀╔      ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▀▓▓▓▓▓▓▓▓▓▓▓▓▄▓▓   ▓▌  ╓▓▀▄▀      ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ╙▓▓▓▓▓▓▓▓▓▓▓     ▓▌╓▓▀╦╜      ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓      ▓▓▀ ╜      ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▀▓▓▓▓▓     ╓▓▓       ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ▀▓▓▓     ╢▓▓     ╫▓▓╜   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┐        ╙      ╢▓▓   ╓▓▓╜     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╖             ╢▓▓ ╔▓▀─     ╓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄           ▓▓▓╢╬      ╒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄     ╔▓▓▓▓╓╝       ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄ ▄▓▓▓▓╜╘      ╓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓═      ╓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓═    ╒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓═   ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓═ ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

"""[1:]

Anime.Fade(Center.Center(banner), Colors.red_to_white, Colorate.Vertical, enter=True)
time.sleep(0.1)

S_HEIGHT, S_WIDTH = (1920, 1080)
GRABZONE = 10
GRABZONE2 = 10

MODE1 = "F1"
MODE2 = "F2"
MODE3 = "F3"
MODE4 = "F4"
MODE5 = "F5"
MODE6 = "F6"
HOLDFUNCTION = "F7"
AUTOREFRESH = "F8"
HOLDKEYPRESSED = "alt"
BUNNYHOP = "F9"

bBhop = False
bTriggerbot = False
bSniperMode = False
bAutoMode = False
bAimLock = False
bStopThread = False
bRunning = False
bPressing = False
bRefresh = False
bSheriff = False
bSniperClutch = False
bHoldFunction = False
bRightSniperClutch = False
bShotgun = False  




class Found(Exception):
        pass

class isSpectating(Exception):
        pass

class CColor:
        Red = '\033[31m'
        Green = '\033[92m'
        Yellow = '\033[90m'
        Blue = '\u001b[34m'
        Cyan = '\u001b[36m'
        White = '\033[0m'
        Yellow2 = '\033[33m'

def bhop():
        if(keyboard.is_pressed("space")):
                keyboard.press_and_release("space")
                keyboard.unhook_all()
                time.sleep(0)
                
def autorefresh():
        if(keyboard.is_pressed("alt")):
                keyboard.press_and_release(";")
                keyboard.unhook_all()
                time.sleep(0)

def approx(r, g ,b):
        return 250 - 60 < r < 250 + 60 and 100 - 60 < g < 100 + 60 and 250 - 60 < b < 250 + 60

def isSpectating():
        try:
                spectating = pyautogui.locateOnScreen("isSpectate.png",confidence=0.8)
                if spectating is not None:
                        print("spectating")
                        raise isSpectating
                else:
                        return False
        except isSpectating:
                return True
                

def shotgun(): #raging triggerbot
        img = grab()   
        try:
                for x in range(0,GRABZONE):
                        for y in range(0,GRABZONE):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                keyboard.press('l') 
                keyboard.release('l')
                time.sleep(0.1)
                                
def holdshotgun(): #raging triggerbot
        img = grab()   
        try:
                for x in range(0,GRABZONE):
                        for y in range(0,GRABZONE):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                if(keyboard.is_pressed(HOLDKEYPRESSED)):
                        keyboard.press('l') 
                        keyboard.release('l')
                        keyboard.unhook_all()
                        time.sleep(0.1)     
                
def triggerbot(): #raging triggerbot
        img = grab()   
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                keyboard.press('l') 
                keyboard.release('l')
                time.sleep(0)
                
                
def holdtriggerbot():
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                if(keyboard.is_pressed(HOLDKEYPRESSED)):
                        keyboard.press('l') 
                        keyboard.release('l')
                        keyboard.unhook_all()
                        
def automode(): #tap-no recoil
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                keyboard.press('l') 
                keyboard.release('l')
                time.sleep(0.15)

def holdautomode():
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                if(keyboard.is_pressed(HOLDKEYPRESSED)):
                        keyboard.press('l') 
                        keyboard.release('l')
                        keyboard.unhook_all()
                        time.sleep(0.15)
                        
def guardian(): #guardian
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                keyboard.press('l') 
                keyboard.release('l')
                time.sleep(0.3)
                
def holdguardian(): #guardian
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                if(keyboard.is_pressed(HOLDKEYPRESSED)):
                        keyboard.press('l') 
                        keyboard.release('l')
                        keyboard.unhook_all()
                        time.sleep(0.3)
                        
def chamber(): #sheriff sniper chamber
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                keyboard.press('l') 
                keyboard.release('l')
                time.sleep(0.35)
                
                
def holdchamber(): #sheriff sniper chamber
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                if(keyboard.is_pressed(HOLDKEYPRESSED)):
                        keyboard.press('l') 
                        keyboard.release('l')
                        keyboard.unhook_all()
                        time.sleep(0.35)
                        
                        
def sniperclutch():
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                keyboard.press('l') 
                keyboard.release('l')
                time.sleep(0.5)
                
def holdsniperclutch():
        img = grab()
        try:
                for x in range(0,GRABZONE2):
                        for y in range(0,GRABZONE2):
                                r,g,b = img.getpixel((x,y))
                                if approx(r,g,b):
                                        raise Found
        except Found:
                if(keyboard.is_pressed(HOLDKEYPRESSED)):
                        keyboard.press('l') 
                        keyboard.release('l')
                        keyboard.unhook_all()
                        time.sleep(0.5)
                        
                       
                        


def grab():
        with mss.mss() as sct:
            bbox=(int(S_HEIGHT/2-GRABZONE), int(S_WIDTH/2-GRABZONE), int(S_HEIGHT/2+GRABZONE), int(S_WIDTH/2+GRABZONE))
            sct_img = sct.grab(bbox)
            return PIL.Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
            
def printgui():
        os.system("cls")
        Color = CColor()
        print(f"{Color.Green}-----------------------------TRIGGERBOT-----------------------------")
        print(f"{Color.Red}                            [UPDATED{Color.Yellow} V.9{Color.Yellow2} Rework{Color.Red}]\r\n")
        print(Fore.GREEN + "[" + Fore.YELLOW + MODE1 + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Mode 1{Color.Red} (Full-Spray)       : {Color.Green}{bTriggerbot}{Color.Yellow}{Color.White}  |PHANTOM/VANDAL|")
        print(Fore.GREEN + "[" + Fore.YELLOW + MODE2 + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Mode 2{Color.Red} (Burst 90%)        : {Color.Green}{bAutoMode}{Color.Red}{Color.White}  |VANDAL/CLASSIC/GHOST/JETT ULT|")
        print(Fore.GREEN + "[" + Fore.YELLOW + MODE3 + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Mode 3{Color.Red} (Sniper Lock-on)   : {Color.Green}{bSniperClutch}{Color.Yellow}{Color.White}  |MARSHAL/OPERATOR/SHERIFF|")
        print(Fore.GREEN + "[" + Fore.YELLOW + MODE4 + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Mode 4{Color.Red} (Shotgun Gay)      : {Color.Green}{bShotgun}{Color.Yellow}{Color.White}  |BUCKY/JUDGE|")
        print(Fore.GREEN + "[" + Fore.YELLOW + MODE5 + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Mode 5{Color.Red} (Chamber Supreme)  : {Color.Green}{bSheriff}{Color.Red}{Color.White}  |CHAMBER's SHERIFF/OPERATOR|")
        print(Fore.GREEN + "[" + Fore.YELLOW + MODE6 + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Mode 6{Color.Red} (Guardian Supreme) : {Color.Green}{bRunning}{Color.Red}{Color.White}  |GUARDIAN|")
        print(f"{Color.Green}__________________________________________________________________")
        print(Fore.GREEN + "[" + Fore.YELLOW + HOLDFUNCTION + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Hold Function{Color.Red}", Fore.RED + "[" + Fore.YELLOW + HOLDKEYPRESSED + Fore.RED + "]" + Style.RESET_ALL, f"{Color.Red}      : {Color.Green}{bHoldFunction}{Color.Yellow}{Color.White}  |CHANGE ALL MODE TO HOLD|")
        print(Fore.GREEN + "[" + Fore.YELLOW + AUTOREFRESH + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Auto Refresher     {Color.Red}",  f"{Color.Red}      : {Color.Green}{bRefresh}{Color.White}  |REFRESH PROGRAM CACHE|")
        print(f"{Color.Green}__________________________________________________________________")
        print(Fore.GREEN + "[" + Fore.YELLOW + BUNNYHOP + Fore.GREEN + "]" + Style.RESET_ALL, f"{Color.Yellow}Bunny Hop {Color.Red}(Hold SPACE)    : {Color.Green}{bBhop}{Color.Yellow}{Color.White}  |FASTER ROTATE|\r\n\r\n\r\n\r\n")
        print(f"{Color.Red}==================================================================")
        print(f"{Color.Yellow} Copyright 2020–2022 Valorantcheat.id Triggerbot")
        print(f"{Color.Yellow}               ALL RIGHTS RESERVED.")
        print(f"{Color.Red}==================================================================")
        print(f"{Color.Red} Instagram : {Color.Yellow}@jualcheatvalorantindo")
        print(f"{Color.Red} Discord   : {Color.Yellow}Zexal#9709")
        print(f"{Color.Red} Server    : {Color.Yellow}discord.gg/uwwp9U6DJD")
        
        

printgui()

while True:
        hWnd = win32gui.FindWindow(None,"VALORANT  ")
        if(hWnd == win32gui.GetForegroundWindow()):
                #bhop
                if(bBhop == True):
                        bhop()
                        
                if(bRefresh == True):
                        autorefresh()
                                        
                if(bSniperClutch == True):
                        if(bHoldFunction == True):
                                holdsniperclutch()
                        else:
                                sniperclutch()    
                                
                if(bTriggerbot == True):
                        if(bHoldFunction == True):
                                holdtriggerbot()
                        else:
                                triggerbot()
                        
                        
                if(bAutoMode == True):
                        if(bHoldFunction == True):
                                holdautomode()
                        else:
                                automode()
                                
                if(bSheriff == True):
                        if(bHoldFunction == True):
                                holdchamber()
                        else:
                                chamber()
                                
                if(bRunning == True):
                        if(bHoldFunction == True):
                                holdguardian()
                        else:
                                guardian()
                                
                if(bSniperMode == True):
                        if(bHoldFunction == True):
                                holdtapmode()
                        else:
                                tapmode()

                if(bShotgun == True):
                        if(bHoldFunction == True):
                                holdshotgun()
                        else:
                                shotgun()

       

        if(keyboard.is_pressed(MODE1)):
                bTriggerbot = not bTriggerbot
                if(bTriggerbot == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
                
        if(keyboard.is_pressed(MODE2)):
                bAutoMode = not bAutoMode
                if(bAutoMode == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
                

                
        if(keyboard.is_pressed(MODE3)):
                bSniperClutch = not bSniperClutch
                if(bSniperClutch == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
        
        if(keyboard.is_pressed(MODE4)):
                bShotgun = not bShotgun
                if(bShotgun == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
                
        if(keyboard.is_pressed(MODE5)):
                bSheriff = not bSheriff
                if(bSheriff == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
                

        if(keyboard.is_pressed(MODE6)):
                bRunning = not bRunning
                if(bRunning == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
                
        if(keyboard.is_pressed(HOLDFUNCTION)):
                bHoldFunction = not bHoldFunction
                if(bHoldFunction == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
        
        if(keyboard.is_pressed(AUTOREFRESH)):
                bRefresh = not bRefresh
                if(autorefresh == True):
                        time.sleep(0.4)
                else:
                        time.sleep(0.4)
                printgui()
                
                
        if(keyboard.is_pressed(BUNNYHOP)):
                bBhop = not bBhop
                if(bBhop == True):
                        time.sleep(0.4)
                else:   
                        time.sleep(0.4)
                printgui()


        if(keyboard.is_pressed("delete")):
                print("Have a great day !")
                os._exit(1)
