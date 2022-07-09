import os, json, shutil
import sys

# os.system("py s.py")
filename = "dskdata.json"
try :
    with open(filename, encoding = "UTF8") as f :
        p = json.load(f)
except FileNotFoundError :
    print("dsk.py > open dskdata.json : 找不到檔案")
    pass

from pymodle.dskmod import GeneralTools as G
from pymodle.dskmod import FileTool
from pymodle import dskmod
import pathlib
from time import sleep
from pathlib import Path
from colorama import Style
cmdlist = p["cmdlist"]
userlist = p["userlist"]
decmdlist = p["decmdlist"]

def switch(lister : list) :                                        # switch
    cmd_ = lister[0]
    if cmd_[0] == "-" :
        cmd = cmd_[1:]
        match cmd:
            case "pit" :
                G.cs()
                o = ' '.join(lister[1:])
                print(o)
            case "et" :
                G.cs()
                if sys.argv[0] == "dsk.py" :
                    os.system("py k.py")
                print(Style.RESET_ALL)
                print(exit())
            case "cd" :
                G.cs()
                try :
                    o = " ".join(lister[1:])
                    os.chdir(o)
                except :
                    print("系統找不到路徑")
            case "path" :
                G.cs()
                print(os.getcwd())
            case "dir" :
                G.cs()
                flist = os.listdir()
                path_ = os.getcwd()
                for i in flist :
                    if os.path.isfile(os.path.join(path_, i)) :
                        print(i)
                    if os.path.isdir(os.path.join(path_, i)) :
                        print(i)
            case "cmdhelp" :
                G.cs()
                if len(lister[1:]) != 0 :
                    k = lister[1]
                    for i in decmdlist.keys():
                        if i == k :
                            print(decmdlist[k])
            case "c" :
                G.cs()
            case "cls" :
                G.cs()
            case "open" :
                G.cs()
                exten = pathlib.Path(lister[1]).suffix
                if exten == ".txt" :
                    with open(lister[1], "r", encoding = "utf8") as file:
                        if len(lister) >= 3 and lister[2]:
                            print(dskmod.border(file.read(), int(lister[2])))
                        else :
                            print(dskmod.border(file.read(), 20))
            case "defile" :
                G.cs()
                try :
                    os.remove(lister[1])
                except :
                    print("error")
            case "defolder" :
                G.cs()
                try :
                    F = input("文件夾 > ")
                    G.cs()
                    if os.path.isdir(F) :
                        shutil.rmtree(F)
                    else :
                        print(f"dsksysfunction > defolder : {F} 不是資料夾")
                except KeyboardInterrupt:
                    print("dsksysfunction > defolder : 輸入錯誤")
            case "rename" :
                G.cs()
                try :
                    os.rename(lister[1], lister[2])
                except :
                    print("error")
            case "mdf" :
                G.cs()
                ch = input("建立 :\n\n - 檔案 [f]\n\n -  資料夾 [F]\n\n      > ")
                if ch == "f" :
                    try :
                        name = input("檔案名稱\n    > ")
                        fpath = Path(name)
                        fpath.touch(exist_ok = True)
                        f = open(fpath)
                        f.close()
                    except KeyboardInterrupt :
                        print("dsksysfunction > -mdf : 輸入錯誤")
                elif ch == "F" :
                    try :
                        name = input("資料夾名稱\n    > ")
                        if not os.path.isdir(name):
                            os.mkdir(name)
                        else :
                            print(f"dsksysfunction > -mdf : {name} 存在")
                    except KeyboardInterrupt :
                        print("dsksysfunction > -mdf : 輸入錯誤")
                else :
                    print("dsksysfunction > -mdf : 輸入錯誤")
            case "all-user" :
                G.cs()
                for i in userlist :
                    print(i, userlist[i])
            case "p" :
                G.cs()
                a = str(lister[1])
                b = dskmod.Turning.list_turn_str(lister[2:], " ")
                if b == "":
                    py = "py " + a + ".py"
                else :
                    py = "py " + a + ".py" + " " + b
                os.system(py)
            case "t" :
                G.cs()
                txt = "start " + lister[1] + ".txt"
                os.system(txt)
            case "run" :
                G.cs()
                f = "start " + lister[1]
                os.system(f)
            case "ftt" :
                G.cs()
                dskmod.Turning.file_turn_txt()
            case "kaser" :
                G.cs()
                if len(lister) >= 2 :
                    fname = lister[1]
                    dal = int(lister[2])
                    try :
                        with open(fname, "r+", encoding = "utf8") as f :
                            fdata = f.readlines()
                    except FileNotFoundError :
                        print("dsksysfunction.py > kaser : 找不到檔案")
                        pass
                    re = []
                    for i in fdata :
                        if i[-1] == "\n" :
                            i = i[:len(i) - 1]
                            kaser = dskmod.StringTool.kaser(i, dal)
                            re.append(kaser)
                        else :
                            kaser = dskmod.StringTool.kaser(i, dal)
                            re.append(kaser)
                    restring = dskmod.Turning.list_turn_str(re, "\n")
                    try :
                        with open(fname, "w+", encoding = "utf8") as f :
                            f.write(restring + "\n" + str(dal))
                    except FileNotFoundError :
                        print("dsksysfunction > kaser : 找不到檔案")
                        pass
                elif len(lister) == 1 :
                    print("dsksysfunction.py > kaser : 請輸入檔名和位移量")
            case "dsk" :
                os.system("py k.py")
                os.system('py dsk.py')
                sleep(1)
                print(exit())
            case "tb" :
                fname = lister[1]
                resultname = lister[2]
                filepath = str(os.getcwd() + "\\")
                file = filepath + fname
                try :
                    filedata = dskmod.Turning.file_turn_bin(file)
                except FileNotFoundError :
                    print("dsksysfunction > tb : 找不到檔案")
                    pass
                with open(resultname, "w+", encoding = "utf8") as f :
                    f.write(filedata)
                chose = lister[3]
                if chose.lower() == "y" :
                    try :
                        os.remove(file)
                    except OSError as e :
                        print(e)
            case "allcmd" :
                print("-"*115)
                for i in cmdlist :
                    cmd =" {l:20}|{cmdd:^80}".format(l = i, cmdd = cmdlist[i])
                    cmds = dskmod.StringTool.border(cmd, 115, line = "-", boder = "down")
                    print(cmds)
            case "ad" :
                fname = "dskdata.json"
                ag = dskmod.Turning.list_turn_str(lister[1:], " ")
                if ag == "add" :
                    cmdname = input("命令名稱 :\n     > ")
                    cmdmean = input("命令作用 :\n     > ")
                    FileTool.addcmd(cmdname, cmdmean, fname)
                elif ag == "del" :
                    cmdname = input("刪除 -- 命令 :\n     > ")
                    FileTool.decmd(cmdname, fname)
                elif ag == "reload" :
                    oldcmd = input("原命令名稱 :\n   > ")
                    newcmdname = input("新命令名稱 :\n      > ")
                    newcmdmean = input("新命令作用 :\n      > ")
                    FileTool.reloadcmd(oldcmd, newcmdname, newcmdmean, fname)
            case "math" :
                os.system("py dskmathsystem.py")
                sleep(1)
                print(exit())
            case "dt" :
                dskmod.FileTool.detailcmd()
            case "mv" :
                file = input("要移動的檔案\n    > ")
                topath = input("要移動到的位址\n    > ")
                try :
                    if os.path.isfile(file) :
                        if os.path.isdir(topath) :
                            os.system(f"move {file} {topath}")
                        else :
                            os.mkdir(topath)
                            os.system(f"move {file} {topath}")
                    else :
                        print(f"dsksysfunction > mv : {file} 不是一個檔案")
                except FileNotFoundError :
                    print("dsksysfunction.py > -mv : 找不到檔案")
            case "cpf" :
                G.cs()
                ch = input("要複製 檔案[f] 還是 資料夾[F]\n   > ")
                if ch == "f" :
                    G.cs()
                    try :
                        oldfname = input("要複製的檔案\n     > ")
                        newfname = input("複製的檔案名\n     > ")
                        if os.path.isfile(oldfname) :
                            shutil.copyfile(oldfname, newfname)
                        else :
                            print(f"dsksysfunction > cpf : {oldfname} 不存在")
                    except KeyboardInterrupt:
                        print("dsksysfunction > -cpf : 輸入錯誤")
                elif ch == "F" :
                    G.cs()
                    try :
                        oldfname = input("要複製的資料夾\n     > ")
                        newfname = input("複製的資料夾名\n     > ")
                        if os.path.isdir(oldfname) :
                            shutil.copy(oldfname, newfname)
                        else :
                            print(f"dsksysfunction > cpf : {oldfname} 不存在")
                    except KeyboardInterrupt:
                        print("dsksysfunction > -cpf : 輸入錯誤")
            case "" :
                G.cs()
                print("請輸入命令")
            case _ :
                G.cs()
                print("系統找不到這個命令")
                print("請重新輸入")
    elif cmd_[0] == "+" :
        G.cs()
        cd = ' '.join(lister[1:])
        os.system(cd)