import keyboard
import pyautogui
import time
import ctypes
import PIL.ImageGrab
import PIL.Image
import winsound 
import os
import mouse
import subprocess
import requests
import sys
import mss
from colorama import Fore, Style, init
from playsound import playsound
from PIL import Image

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
        time.sleep(0.01)

def Main_Program():
    if hwid in r.text:
        os.system("cls")
        Color = CColor()
        printSlow(f"{Color.Green}Access Granted!\r\n")
        printSlow(f"{Color.Cyan}TRIGGERBOT Ver.11{Color.White} WILL BE LAUNCHED!\r\n")
        printSlow(f"{Color.Red}Warning!{Color.White}This Not A Test!")
        time.sleep(0)
        print(f"\r\n")
        os.system('pause')
        
    else:
        os.system("cls")
        Color = CColor()
        print(f"{Color.White}Token License Kamu{Color.Red} UNVERIFIED!")
        print(f"{Color.Yellow}Copy-Paste Kode Token di bawah ke{Color.Cyan} Discord{Color.Green} Zexal9709\r\n\r\n\r\n")
        printSlow(f"{Color.Red}Kode Request License: {Color.White}\r\n" + hwid)
        print(f"\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n")
        print(f"{Color.Red}==================================================================")
        print(f"{Color.Yellow} Copyright 2020–2024 Outlaws Triggerbot")
        print(f"{Color.Yellow}               ALL RIGHTS RESERVED.")
        print(f"{Color.Red}==================================================================")
        print(f"{Color.Red} Instagram : {Color.Yellow}@jualcheatvalorantindo")
        print(f"{Color.Red} Discord   : {Color.Yellow}Zexal9709")
        print(f"{Color.Red} Server    : {Color.Yellow}discord.gg/uwwp9U6DJD")
        os.system('pause >NUL')
        os._exit(1)

def titlescreen():
    os.system("cls")
    print(Fore.CYAN + "      TRIGGERBOT Version 11 (Rebuilt)  " + Style.RESET_ALL)
    print(Fore.YELLOW + "         Copyright 2020–2024           " + Style.RESET_ALL)
    print(f"\r\n")

HOLD_KEY = "ALT"

def set_custom_keybind():
    global HOLD_KEY
    titlescreen()
    if input("    Atur Manual Tombol Hold? (yes/no): ")[:1] in "yY":
        titlescreen()
        print(f"Tombol Hold Keyboard: [{Fore.GREEN}{HOLD_KEY}{Style.RESET_ALL}]")
        print("\nPress [ESC] to continue")
        while True:
            new_key = keyboard.read_key()
            if new_key == "esc":
                break
            else:
                HOLD_KEY = new_key
                titlescreen()
                print(f"Current keybind: [{Fore.GREEN}{HOLD_KEY}{Style.RESET_ALL}]")
                print("\nPress [ESC] to continue")
    else:
        titlescreen()
        print(f"Current keybind: [{Fore.GREEN}{HOLD_KEY}{Style.RESET_ALL}]")
        print("\nPress any key to continue")
        keyboard.wait()

if __name__ == "__main__":
    set_custom_keybind()
    SWITCH_KEY = "F1"
    TRIGGER_KEY = "F2"
    HOLD_BUTTONKEY = "F3"
    BUNNY_KEY = "F5" 
    AUTOREFRESH = "F8"  
    S_HEIGHT, S_WIDTH = (1366, 768)
    PURPLE_R, PURPLE_G, PURPLE_B = (250, 100, 250)
    TOLERANCE = 60
    GRABZONE = 6
    mods = ["PHASE-01 [OPERATOR/MARSHAL/SHERIFF]", "PHASE-02 [GUARDIAN/PISTOL]", "PHASE-03 [VANDAL/PHANTOM/SPECTRE]"]
    pyautogui.FAILSAFE = False
    HOLDFUNCTION = False
    
    class FoundEnemy(Exception):
        pass

    class triggerBot:
        def __init__(self) -> None:
            self.toggled = False
            self.keyhold = True
            self._bunny = False
            self._refreshed = True
            self.mode = 0
            self.last_reac = 0

        def toggle(self) -> None:
            self.toggled = not self.toggled

        def bunnyy(self) -> None:
            self._bunny = not self._bunny

        def keyholdd(self) -> None:
            self.keyhold = not self.keyhold
    
        def refresh(self) -> None:
            self._refreshed = not self._refreshed

        def switch(self):
            if self.mode != 2:
                self.mode += 1
            else:
                self.mode = 0
            if self.mode == 0:
                time.sleep(0)
            if self.mode == 1:
                time.sleep(0)
            if self.mode == 2:
                time.sleep(0)


        def normalclick(self) -> None:
                keyboard.press('l')
                keyboard.release('l') 

        def keyclick(self) -> None:
                if keyboard.is_pressed(HOLD_KEY):
                    keyboard.press('l')
                    keyboard.release('l')            
        
                     
        
        def approx(self, r, g ,b) -> bool: return PURPLE_R - TOLERANCE < r < PURPLE_R + TOLERANCE and PURPLE_G - TOLERANCE < g < PURPLE_G + TOLERANCE and PURPLE_B - TOLERANCE < b < PURPLE_B + TOLERANCE
 
        def grab(self) -> None:
            with mss.mss() as sct:
                bbox=(int(S_HEIGHT/2-GRABZONE), int(S_WIDTH/2-GRABZONE), int(S_HEIGHT/2+GRABZONE), int(S_WIDTH/2+GRABZONE))
                sct_img = sct.grab(bbox)
                return PIL.Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        
                   
        
        def normalscan(self) -> None:
            start_time = time.time()
            pmap = self.grab()
            
            try:
                for x in range(0, GRABZONE*2):
                    for y in range(0, GRABZONE*2):
                        r, g, b = pmap.getpixel((x,y))
                        if self.approx(r, g, b): raise FoundEnemy
            except FoundEnemy:
                self.last_reac = int((time.time() - start_time)*500)
                self.normalclick()
                if self.mode == 0: time.sleep(0.5)
                if self.mode == 1: time.sleep(0.3)
                if self.mode == 2: time.sleep(0.2)
                print_banner(self)
            
        def keyscan(self) -> None:
            start_time = time.time()
            pmap = self.grab()
        
            try:
                for x in range(0, GRABZONE*2):
                    for y in range(0, GRABZONE*2):
                        r, g, b = pmap.getpixel((x,y))
                        if self.approx(r, g, b): raise FoundEnemy
            except FoundEnemy:
                self.last_reac = int((time.time() - start_time)*500)
                self.keyclick()
                if self.mode == 0: time.sleep(0.5)
                if self.mode == 1: time.sleep(0.2)
                if self.mode == 2: time.sleep(0)
                print_banner(self)


        def bunny(self) -> None:
            if(keyboard.is_pressed("space")):
                    keyboard.press_and_release("space")
                    keyboard.unhook_all()
                    time.sleep(0)
                
        def refreshed(self) -> None:
            if(keyboard.is_pressed(HOLD_KEY)):
                    keyboard.press_and_release(";")
                    keyboard.unhook_all()
                    time.sleep(0)

    
def print_banner(bot: triggerBot) -> None:
    os.system("cls")
    print(Fore.CYAN + "          TRIGGERBOT Version 11 (Rebuilt)          " + Style.RESET_ALL)
    print(Fore.YELLOW + "              Copyright 2020–2024           " + Style.RESET_ALL)
    print(f"\r\n")
    print(Fore.CYAN + "  PANEL STATUS " + Style.RESET_ALL)
    print("     Mode                     :", Fore.CYAN + mods[bot.mode] + Style.RESET_ALL)
    print("     Triggerbot Status        :", (Fore.GREEN if bot.toggled else Fore.RED) + ("On" if bot.toggled else "Off") + Style.RESET_ALL)
    print("     Hold Function Key-Board  :", (Fore.GREEN if bot.keyhold else Fore.RED) + ("On" if bot.keyhold else "Off") + Style.RESET_ALL)
    print("     Auto Refesh Start 30s    :", (Fore.GREEN if bot._refreshed else Fore.RED) + ("On" if bot._refreshed else "Off") + Style.RESET_ALL)
    print("     Bunny Hop                :", (Fore.GREEN if bot._bunny else Fore.RED) + ("On" if bot._bunny else "Off") + Style.RESET_ALL)
    print("     Reaction Time            :", Fore.CYAN + str(bot.last_reac) + Style.RESET_ALL + " ms ("+str((bot.last_reac)/(GRABZONE*GRABZONE))+"ms/pix)")
    print(f"\r\n")
    print(Fore.CYAN + "  KONTROL HOLD_KEY" + Style.RESET_ALL)
    print("     Switch Mode        :", Fore.YELLOW + SWITCH_KEY + Style.RESET_ALL)
    print("     Activate Trigger   :", Fore.YELLOW + TRIGGER_KEY + Style.RESET_ALL)
    print("     Hold Keyboard      :", Fore.YELLOW + HOLD_BUTTONKEY + Fore.CYAN + "  |KEY PRESSED( " + Fore.RED + HOLD_KEY + Fore.CYAN + " )|" + Style.RESET_ALL)
    print("     AUTO REFRESH       :", Fore.YELLOW + AUTOREFRESH + Style.RESET_ALL)
    print("     Bunny Hop          :", Fore.YELLOW + BUNNY_KEY + Style.RESET_ALL)
    print(f"\r\n\r\n")
    print(Fore.CYAN + "  =========================================" + Style.RESET_ALL)
    print(Fore.WHITE + "   Copyright 2020–2024 Outlaws Triggerbot" + Style.RESET_ALL)
    print(Fore.WHITE + "            ALL RIGHTS RESERVED." + Style.RESET_ALL)
    print(Fore.CYAN + "  =========================================" + Style.RESET_ALL)
    print(Fore.CYAN + "   Instagram : " + Fore.WHITE + "@jualcheatvalorantindo" + Style.RESET_ALL)
    print(Fore.CYAN + "   Discord   : " + Fore.WHITE + "Zexal9709" + Style.RESET_ALL)
    print(Fore.CYAN + "   Server    : " + Fore.WHITE + "discord.gg/uwwp9U6DJD" + Style.RESET_ALL)
 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

                                
if __name__ == "__main__":
    bot = triggerBot()
    print_banner(bot)
    while True:
        if keyboard.is_pressed(SWITCH_KEY):
            bot.switch()
            print_banner(bot)
            while keyboard.is_pressed(SWITCH_KEY): pass
        if keyboard.is_pressed(TRIGGER_KEY):
            bot.toggle()
            print_banner(bot)
            if bot.toggled: time.sleep(0)
            else: time.sleep(0)
            while keyboard.is_pressed(TRIGGER_KEY): pass
        if keyboard.is_pressed(AUTOREFRESH):
            bot.refresh()
            print_banner(bot)
            if bot._refreshed: time.sleep(0)
            else: time.sleep(0)
            while keyboard.is_pressed(AUTOREFRESH): pass
        if keyboard.is_pressed(BUNNY_KEY): 
            bot.bunnyy()
            print_banner(bot)
            if bot._bunny: time.sleep(0)
            else: time.sleep(0)
            while keyboard.is_pressed(BUNNY_KEY): pass
        if keyboard.is_pressed(HOLD_BUTTONKEY):
            bot.keyholdd()
            print_banner(bot)
            if bot.keyhold: time.sleep(0)
            else: time.sleep(0)
            while keyboard.is_pressed(HOLD_BUTTONKEY): pass

                 
        if bot.toggled:
            if bot.keyhold: bot.keyscan()
            else:
                bot.normalscan() 
                
        if bot._bunny: bot.bunny()
        if bot._refreshed: bot.refreshed()
        
