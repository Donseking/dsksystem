import pymodle.dskmod as dskmod
import sys


filename = "dskdata.json"

d = []
c = sys.argv

try :
    with open(filename, "r", encoding = "UTF8") as f :
        d = f.readlines()
except FileNotFoundError :
    print("dsk.py > open dskdata.json : 找不到檔案")
    pass
re = []
for i in d :
    if i[-1] == "\n" :
        i = i[:len(i) - 1]
        kaser = dskmod.StringTool.kaser(i, -4)
        re.append(kaser)
    else :
        kaser = dskmod.StringTool.kaser(i, -4)
        re.append(kaser)
restring = dskmod.Turning.list_turn_str(re, "\n")
try :
    with open(filename, "w+", encoding = "utf8") as f :
        f.write(restring + "\n")
except FileNotFoundError :
    print("dsk.py > open dskdata.json : 找不到檔案")
    pass