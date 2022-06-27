import colorama
from colorama import Fore
from colorama import Style
import pymodle.dsksysfunction as dun
from pymodle.dskmod import GeneralTools as G
import json, os

filename = "D:\dsk\pythons\dsksys\DSK System\dskdata.json"

print(Fore.BLUE + Style.BRIGHT)
G.cs()
chose = input("login[l] or register[r] :\n  > ")
G.cs()

with open(filename, encoding = "utf8") as f:
    p = json.load(f)
cmdlist = p["cmdlist"]
userlist = p["userlist"]
decmdlist = p["decmdlist"]

def login(ch) :                                                 # login
    chose = ch
    while chose == "l" :
        print("User :")
        user = input("  > ")
        print("Password :")
        pw = input ("   > ")
        ok = 0
        c = 0
        for i in userlist :
            c += 1
            if user == i :
                if pw == userlist[i] :
                    ok = 1
                else :
                    G.cs()
                    print("password error")
                    break
            elif user != i and c == len(userlist) :
                print("user error")
        if ok == 1 :
            break
        else :
            print(exit())

    while chose == "r" :
        print("User :")
        user = input("  > ")
        print("Password :")
        pw = input ("   > ")
        ok = 0
        for i in userlist :
            if user == i :
                if pw == userlist[i] :
                    ok = 1
                    break
                else :
                    G.cs()
                    print("user name already exists")
                    break
            else :
                G.cs()
                userlist[user] = pw
                jso = {
                    "userlist" : userlist,
                    "cmdlist" : cmdlist,
                    "decmdlist" : decmdlist
                }
                with open("dskdata.json", "w") as file :
                    json.dump(jso, file, indent = 4)
                ok = 1
                break
        if ok == 1 :
            break
        else :
            print(exit())
    while chose == '' or (chose != 'l' and chose != 'r') :
        G.cs()
        print("請輸入\n")
        chose = input("login[l] or register[r] :\n  > ")
        if chose != '' :
            break

if chose == "p":
    pass
else :
    login(chose)
G.cs()
colorama.init()
while True :
    PATH = os.getcwd()
    try :
        sting = input(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f" +DSK SYSTEM+ {PATH} > " + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT).split()
        print(Fore.BLUE + Style.BRIGHT)
        if len(sting) != 0 :
            c = sting[0]
            if c[0] == '-' or c[0] == '+' :
                dun.switch(sting)
            elif c == "dskmath" :
                os.system("py dskmathsystem.py")
            elif c == "chat" :
                os.system("python D:\\dsk\\pythons\\socket_practice\\chat.py")
        else :
            G.cs()
            print("請輸入")
    except KeyboardInterrupt :
        G.cs()
        print("\n++ 輸入錯誤 ++\n")