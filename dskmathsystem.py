import colorama
from colorama import Fore
from colorama import Style
from pymodle.dskmod import GeneralTools as G
import pymodle.dsksysfunction as dun
from pymodle.dskmahsysfunction import MathMod

colorama.init()
G.cs()

print("-"*15 + "+ dskmath +" + "-"*15 + "\n")
print(Fore.BLUE + Style.BRIGHT)

while True :
    try :
        sting = input(Fore.GREEN + Style.BRIGHT + "  > " + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT).split()
        print(Fore.BLUE + Style.BRIGHT)
        if len(sting) != 0 :
            c = sting[0]
            if c[0] == '-' or c[0] == '+' :
                dun.switch(sting)
            else :
                MathMod(sting)
        else :
            G.cs()
            print("請輸入")
    except KeyboardInterrupt :
        G.cs()
        print("\n++ 輸入錯誤 ++\n")
