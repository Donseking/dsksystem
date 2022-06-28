import json, os
from this import s

coder = "utf8"


numlist = {
    "一" : 1,
    "二" : 2,
    "三" : 3,
    "四" : 4,
    "五" : 5,
    "六" : 6,
    "七" : 7,
    "八" : 8,
    "九" : 9,
    "十" : 10
}

class StringTool :

    def bins(BinsStrings : str) :
        re = []
        for i in BinsStrings :
            i = bin(ord(i))
            i = i[2:]
            if len(i) < 16 :
                i = '0'*(16 - len(i)) + i
            re.append(i)
        return Turning.list_turn_str(re, " ")

    def border(thrstr : str, num : int, line = "=", boder = "all") :
        if boder == "all" :
            re = line*num + "\n"  + "|" + thrstr + " "*(num - len(thrstr)) + "|" + "\n" + line*num
        elif boder == "up" :
            re = line*num + "\n"  + thrstr
        elif boder == "down" :
            re = thrstr + "\n" + line*num
        elif boder == "right" :
            re = thrstr + "|"
        elif boder == "left" :
            re = "|" + thrstr
        return re

    def bintostr(binstr : str):
        re = []
        for i in binstr.split(" ") :
            for j in i :
                if j == "1" :
                    out_str = chr(int(i[i.index(j):], 2))
                    re.append(out_str)
                    break
        return Turning.list_turn_str(re, "")


    def kaser(laws, dalta : int) :
        re = []
        if type(laws) == str :
            for i in laws :
                i = chr(ord(i) + dalta)
                re.append(i)
            return Turning.list_turn_str(re, "")
        elif type(laws) == list :
            for i in laws :
                for j in i :
                    j = chr(ord(j) + dalta)
                    re.append(j)
                re.append(' ')
            res = Turning.list_turn_str(re, "")
            return res

class FileTool :
    def __init__(self):
        pass

    def addcmd(cmdname : str, cmdmean : str, filename : str):
        if filename == "D:\dsk\pythons\dsksys\DSK System\dskdata.json" :
            with open(filename, encoding = "utf8") as f :
                p = json.load(f)
            cmdlist = p["cmdlist"]
            userlist = p["userlist"]
            decmdlist = p["decmdlist"]
            cmdlist[cmdname] = cmdmean
            p = {
                "userlist": userlist,
                "cmdlist": cmdlist,
                "decmdlist" : decmdlist
            }
            with open(filename, "w") as f :
                json.dump(p, f, indent = 4)

    def decmd(cmdname : str, filename : str) :
        if filename == "D:\dsk\pythons\dsksys\DSK System\dskdata.json" :
            with open(filename, "r+", encoding = coder) as f :
                p = json.load(f)
            cmdlist = p["cmdlist"]
            userlist = p["userlist"]
            decmdlist = p["decmdlist"]
            cmdlist.pop(cmdname, "NotFindCmd")
            p = {
                "userlist": userlist,
                "cmdlist": cmdlist,
                "decmdlist" : decmdlist
            }
            with open(filename, "w") as f :
                json.dump(p, f, indent = 4)

    def reloadcmd(OldCmdName, NewCmdName : str, NewCmdMean : str, FileName : str):
        if FileName == "D:\dsk\pythons\dsksys\DSK System\dskdata.json" :
            with open(FileName, encoding = "utf8") as f :
                p = json.load(f)
            cmdlist = p["cmdlist"]
            userlist = p["userlist"]
            decmdlist = p["decmdlist"]
            cmdlist.pop(OldCmdName, "NotFindCmd")
            cmdlist[NewCmdName] = NewCmdMean
            p = {
                "userlist": userlist,
                "cmdlist": cmdlist,
                "decmdlist" : decmdlist
            }
            with open(FileName, "w") as f :
                json.dump(p, f, indent = 4)

    def detailcmd():
        try :
            with open("D:\dsk\pythons\dsksys\DSK System\dskdata.json", encoding = "utf8") as file :
                data = json.load(file)
        except FileNotFoundError :
            print("dskmod.py - detailcmd() : 找不到檔案")
            pass
        cmdlist = data["cmdlist"]
        userlist = data["userlist"]
        decmdlist = data["decmdlist"]
        cmd_ = input("選擇的命令 : ")
        detailmean = input("命令的詳細描述:\n   > ")
        decmdlist[cmd_] = detailmean
        data = {
            "userlist" : userlist,
            "cmdlist" : cmdlist,
            "decmdlist" : decmdlist
        }
        with open("D:\dsk\pythons\dsksys\DSK System\dskdata.json", "w", encoding = "utf8") as f :
            json.dump(data, f, indent = 4)

class Turning :

    def __init__(self) -> None:
        pass

    def file_turn_bin(fname : str, md = "r+", coding = "utf8", interval = " ") :
        try :
            with open(fname, mode = md, encoding = coding) as f :
                filedata = f.read()
            dlist = filedata.split()
            for font in dlist:
                num = dlist.index(font)
                font = StringTool.bins(font)
                dlist[num] = font
            return Turning.list_turn_str(dlist, interval)
        except FileNotFoundError:
            return FileNotFoundError

    def file_turn_txt(md = "r+", coding = "utf8") : # start_file_name = None, result_file_name = None, folder = None
        start_file_name = input("文件名稱\n   > ")
        print("")
        result_file_name = input("終文件名稱\n    > ")
        print("")
        try :
            with open(start_file_name, mode = md, encoding = coding) as f :
                filedata = f.read()
            with open(result_file_name, "w+", encoding = "utf8") as f :
                f.write(filedata)
        except FileNotFoundError :
            return FileNotFoundError
        folder = input("移動至\n    > ")
        print("")
        os.system("move " + result_file_name + " " + folder)

    def list_turn_str(thelist : list, thestr : str) :
        re = thestr.join(thelist)
        return re

    def num_turn_chinese(num : int) :
        for i in numlist :
            if num == numlist[i] :
                return i

    def character_around(s : str, around = s) :
        pass

class GeneralTools :
    def cs():
        os.system("cls")

    def et() :
        print(exit())

    # def neat_array(a : list) :
    #     pass