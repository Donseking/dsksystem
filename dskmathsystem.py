from pymodle.mathmod import MathTools as m
import colorama
from colorama import Fore
from colorama import Style
from pymodle.dskmod import GeneralTools as G
import pymodle.dsksysfunction as dun

def MathMod(cmd : list) :
    prefix = cmd[0]
    for i in cmd[1:] :
        cmd[cmd.index(i)] = int(i)
    if prefix[0] == "#" :
        pre = prefix[1:]
        match pre :
            case "D" :
                cdt = input(" 請輸入 ( x, y )\n     > ").split()
                L = input(" 請輸入方程式的所有係數\n    > ").split()
                cdt = list(map(int, cdt))
                L = list(map(int, L))
                if len(L) == 4 and len(cdt) == 3 :
                    ans = m.D(cdt, L)
                elif len(L) == 3 and len(cdt) == 2 :
                    ans = m.D(cdt, L)
                print(ans)
            case "od-3" :
                r1 = input("輸入第一列 > ").split()
                r2 = input("輸入第二列 > ").split()
                r3 = input("輸入第三列 > ").split()
                r1 = list(map(int, r1))
                r2 = list(map(int, r2))
                r3 = list(map(int, r3))
                ans = m.third_order(r1, r2, r3)
                print(ans)
            case "od-2" :
                row1 = input("輸入第一列 > ").split()
                row2 = input("輸入第二列 > ").split()
                for i in row1 :
                    row1[row1.index(i)] = int(i)
                for i in row2 :
                    row2[row2.index(i)] = int(i)
                if len(row1) == 2 and len(row1) == len(row2) :
                    ans = m.second_order(row1, row2)
                print(ans)
            case "cros" :
                pass
            case _ :
                pass

G.cs()
colorama.init()
while True :
    print(Fore.BLUE + Style.BRIGHT)
    print("-"*5 + "+ dskmath +" + "-"*5 + "\n")
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
