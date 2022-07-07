import os, json

os.system("py s.py")
filename = "dskdata.json"
try :
    with open(filename, encoding = "UTF8") as f :
        p = json.load(f)
except FileNotFoundError :
    print("dsk.py > open dskdata.json : 找不到檔案")

import colorama
from colorama import Fore
from colorama import Style
import pymodle.dsksysfunction as dun
import pymodle.dskmod as dm
from pymodle.dskmod import GeneralTools as G
from pytube import YouTube as yt
from bs4 import BeautifulSoup
from urllib import parse
import requests

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
        pw = input ("  > ")
        ok = 0
        c = 0
        for i in userlist :
            c += 1
            if user == i :
                if pw == userlist[i] :
                    ok = 1
                else :
                    G.cs()
                    print(" password error\n")
                    break
        if ok == 1 :
            break
        else :
            G.cs()
            chose = input(" 請重新輸入\n\n login[l]\n\n register[r]\n\n     > ")
            G.cs()
            login(chose)
            break

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
            G.cs()
            login(chose)
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
        sting = input(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f" 【 DSK SYSTEM 】 {PATH} > " + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT).split()
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
            elif c == "govdo" :
                s = input("Google 搜尋 [ 影片 ] > ")
                num = int(input("頁數 > "))
                G.cs()
                a = {"q" : s}
                if num == 1 :
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
                else :
                    u = "https://www.google.com/search?" + parse.urlencode(a)
                    url =  [u,'tbm=vid', 'ei=JN3DYsX7A9biwAPMvpKwDQ', 'start=10', 'sa=N', 'ved=2ahUKEwjFnd6okuH4AhVWMXAKHUyfBNYQ8tMDegQIARBT', 'biw=1732', 'bih=981', 'dpr=1']
                    d = []
                    k = ""
                    for i in range(1, num) :
                        start = url[3]
                        ss = start[:6]
                        ss = ss + str(i*10)
                        url[3] = ss
                        urls = dm.Turning.list_turn_str(url, "&")
                        res = requests.get(urls)
                        soup = BeautifulSoup(res.text, "html.parser")
                        t = soup.find_all("a")
                        for i in t :
                            s = i["href"]
                            h = i.h3
                            for j in s[7:] :
                                if j == "&" :
                                    k = s[7:s.index(j)]
                            k = k.replace("%3F", "?")
                            k = k.replace("%3D", "=")
                            if h != None :
                                print(h.string)
                                print(k)
                                print("\n")
                        print("\n")
            elif c == "google" :
                s = input("Google 搜尋 > ")
                num = int(input("頁數 > "))
                G.cs()
                a = {"q" : s}
                u = "https://www.google.com/search?" + parse.urlencode(a)
                url =  [u, 'ei=B6rDYqSiM4KgoATN_J-YBg', 'start=0', 'sa=N', 'ved=2ahUKEwjkwdjJ4eD4AhUCEIgKHU3-B2M4FBDy0wN6BAgBEDw', 'biw=1732', 'bih=981', 'dpr=1']
                d = []
                k = ""
                for i in range(num) :
                    start = url[2]
                    ss = start[:6]
                    ss = ss + str(i*10)
                    url[2] = ss
                    urls = dm.Turning.list_turn_str(url, "&")
                    res = requests.get(urls)
                    soup = BeautifulSoup(res.text, "html.parser")
                    t = soup.find_all("a")
                    for i in t :
                        s = i["href"]
                        h = i.h3
                        for j in s[7:] :
                            if j == "&" :
                                k = s[7:s.index(j)]
                        k = k.replace("%3F", "?")
                        k = k.replace("%3D", "=")
                        if h != None :
                            print(h.string)
                            print(k)
                            print("\n")
                    print("\n")
            elif c == "pytube-down" :
                try :
                    url = input("網址\n     > ")
                    try :
                        y = yt(url)
                        print("正在下載 ...")
                        y.streams.get_highest_resolution().download('./videos')
                        print("下載完成 !!")
                    except :
                        print("輸入網址錯誤 !!")
                except KeyboardInterrupt :
                    print("dsk.py > pytube-down : 輸入錯誤!!")
        else :
            G.cs()
            print("請輸入")
    except KeyboardInterrupt :
        G.cs()
        print("\n++ 輸入錯誤 ++\n")
        pass