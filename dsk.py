import os, json

os.system("py s.py")
filename = "dskdata.json"
try :
    with open(filename, encoding = "UTF8") as f :
        p = json.load(f)
except FileNotFoundError :
    print("dsk.py > open dskdata.json : 找不到檔案")
    pass
os.system("py k.py")

import colorama
from colorama import Fore
from colorama import Style
import pymodle.dsksysfunction as dun
import pymodle.dskmod as dm
from pymodle.dskmod import GeneralTools as G
from pytube import YouTube as yt
import requests
from bs4 import BeautifulSoup
from urllib import parse

print(Fore.BLUE + Style.BRIGHT)
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
    while chose == '' :
        G.cs()
        print("請輸入\n")
        chose = input("login[l] or register[r] :\n  > ")
        if chose != '' :
            break

    while chose != 'l' and chose != 'r' :
        G.cs()
        print("請輸入\n")
        chose = input("login[l] or register[r] :\n  > ")
        if chose == 'l' or chose == "r":
            G.cs()
            login(chose)

G.cs()
chose = input("login[l] or register[r] :\n  > ")
G.cs()

if chose == "p":
    pass
else :
    login(chose)
colorama.init()
G.cs()
while True :
    PATH = os.getcwd()
    try :
        sting = input(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f" + DSK SYSTEM + {PATH} > " + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT).split()
        print(Fore.BLUE + Style.BRIGHT)
        if len(sting) != 0 :
            c = sting[0]
            if c[0] == '-' or c[0] == '+' :
                dun.switch(sting)
            elif c == "math" :
                os.system("py dskmathsystem.py")
                pass
            elif c == "py" or c == "python" :
                os.system("python")
            elif c == "google" :
                s = input("Google 搜尋 [ 影片 ] > ")
                a = {"q" : s}
                url = "https://www.google.com/search?" + parse.urlencode(a) + "&source=lnms&tbm=vid&sa=X&ved=2ahUKEwiWtIzLweD4AhUcUfUHHUBcC8AQ_AUoAXoECAMQAw&biw=1732&bih=981&dpr=1"
                res = requests.get(url)
                soup = BeautifulSoup(res.text, "html.parser")
                t = soup.find_all("h3")
                for i in t :
                    s = i.parent["href"]
                    print(i.string)
                    for j in s[7:] :
                        if j == "&" :
                            k = s[7:s.index(j)]
                    k = k.replace("%3F", "?")
                    k = k.replace("%3D", "=")
                    print(k)
                    print("\n")
            elif c == "pytube" :
                url = input("網址\n     > ")
                y = yt(url)
                print("正在下載 ...")
                y.streams.get_highest_resolution().download('./videos')
                print("下載完成 !!")
        else :
            G.cs()
            print("請輸入")
    except KeyboardInterrupt :
        G.cs()
        print("\n++ 輸入錯誤 ++\n")
        pass