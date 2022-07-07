import json
from pymodle.mathmod import MathTools as m
from pymodle.dskmod import GeneralTools as G
import pymodle.dskmod as dm

def MathMod(cmd : list) :
    prefix = cmd[0]
    # for i in cmd[1:] :
    #     cmd[cmd.index(i)] = int(i)
    if prefix[0] != "#" :
        match prefix :
            case "D" :
                G.cs()
                ans = None
                cdt = input(" 請輸入 ( x, y )\n     > ").split()
                L = input(" 請輸入方程式的所有係數\n    > ").split()
                cdt = list(map(int, cdt))
                L = list(map(int, L))
                if len(L) == 4 and len(cdt) == 3 :
                    ans = m.D(cdt, L)
                elif len(L) == 3 and len(cdt) == 2 :
                    ans = m.D(cdt, L)
                G.cs()
                if ans != None :
                    print(ans)
                else :
                    print("輸入錯誤，請重新輸入")
            case "od-3" :
                ans = None
                r1 = input("輸入第一列 > ").split()
                r2 = input("輸入第二列 > ").split()
                r3 = input("輸入第三列 > ").split()
                r1 = list(map(int, r1))
                r2 = list(map(int, r2))
                r3 = list(map(int, r3))
                if len(r1) == 3 and len(r2) == 3 and len(r3) == 3 :
                    ans = m.third_order(r1, r2, r3)
                G.cs()
                if ans != None :
                    print(ans)
                else :
                    print("輸入錯誤，請重新輸入")
            case "od-2" :
                row1 = input("輸入第一列 > ").split()
                row2 = input("輸入第二列 > ").split()
                for i in row1 :
                    row1[row1.index(i)] = int(i)
                for i in row2 :
                    row2[row2.index(i)] = int(i)
                if len(row1) == 2 and len(row1) == len(row2) :
                    ans = m.second_order(row1, row2)
                G.cs()
                print(ans)
            case "cros" :
                G.cs()
                x = input("第一個向量 > ").split()
                y = input("第二個向量 > ").split()
                x = tuple(list(map(int, x)))
                y = tuple(list(map(int, y)))
                if len(x) == 3 and len(y) == 3 :
                    ans = m.cros(x, y)
                else :
                    print("輸入錯誤")
                print(ans)
            case "dot" :
                G.cs()
                x = input("第一個向量 > ").split()
                y = input("第二個向量 > ").split()
                x = tuple(list(map(int, x)))
                y = tuple(list(map(int, y)))
                ch = input("是否需要角度 [y/n] > ")
                if ch == "Y" or ch == "y" :
                    an = int(input("角度 > "))
                    if len(x) == 3 or len(x) == 2 :
                        if len(y) == 3 or len(y) == 2 :
                            ans = m.dot(x, y, angle = True, thida = an)
                            print(ans)
                        else :
                            print("輸入錯誤")
                    else :
                        print("輸入錯誤")
                else :
                    ans = m.dot(x, y)
                    print(ans)
            case "mxm" :
                G.cs()
                A = []
                B = []
                row = int(input("首矩陣的行數 > "))
                for i in range(row) :
                    x = input(f"首矩陣第 {i + 1} 行的元素 > ").split()
                    x = list(map(int, x))
                    A.append(x)
                G.cs()
                row = int(input("次矩陣的行數 > "))
                if row == len(A[0]) :
                    for i in range(row) :
                        y = input(f"次矩陣第 {i + 1} 行的元素 > ").split()
                        y = list(map(int, y))
                        B.append(y)
                    ans = m.matrix_multiplication(A, B)
                    print(ans)
                else :
                    print("次矩陣的行數必須和首矩陣的列數相同 [ 直向 ]")
                    pass
            case "ode" :
                num = tuple(list(map(int, input("一元二次方程式的係數 [ 空格相隔 ] > ").split())))
                ans = m.one_dimensional_equation(num)
                if type(ans) == list :
                    for i in ans :
                        print(i)
                else :
                    print(ans)
            case "itl" :
                l = input("首直線方程式係數 ( a, b, c )\n   > ").split()
                lm = input("首直線方程式係數 ( d, e, f )\n   > ").split()
                l = list(map(int, l))
                lm = list(map(int, lm))
                if len(l) == 3 and len(lm) :
                    ans = m.intersection_of_two_lines(l, lm)
                for i in ans :
                    print(i)
            case "vct" :
                a = input("第一個座標點 > ").split()
                b = input("第二個座標點 > ").split()
                a = list(map(int, a))
                b = list(map(int, b))
                ans = m.two_cdt_to_vector(a, b)
                print(ans)
            case "vlon" :
                v = input("向量 > ").split()
                v = tuple(list(map(int, v)))
                ans = m.vector_long(v)
                print(ans)
            case "v+" :
                v1 = input("首向量 > ").split()
                v2 = input("次向量 > ").split()
                v1 = tuple(list(map(int, v1)))
                v2 = tuple(list(map(int, v2)))
                if len(v1) == len(v2) :
                    ans = m.vecotr_plus(v1, v2)
                    print(ans)
                elif len(v1) != len(v2) :
                    print("dskmahsysfunction.py > mathmod > v+(cmd) : 向量要相同長度")
            case "uqe" :
                """
                    一元二次方程式
                """
                try :
                    la = input("方程係數 ax + by + c = 0 [ a, b, c ] \n    > ").split()
                    la = list(map(int, la))
                    if len(la) == 3 :
                        ans = m.Unary_quadratic_equation(la)
                        print(ans)
                    else :
                        print("dskmahsysfunction > uqe : 係數只能有三個")
                except KeyboardInterrupt :
                    print("dskmahsysfunction > uqe : 輸入錯誤")
            case "blse" :
                l1 = list(map(int, input("首聯立方程係數 [ a, b, c ]\n    > ").split()))
                l2 = list(map(int, input("次聯立方程係數 [ a, b, c ]\n    > ").split()))
                if len(l1) == 3 and len(l2) == 3 :
                    ans = m.Binary_Linear_Simultaneous_Equations(l1, l2)
                    print(ans)
                else :
                    print("dskmathsysfunction > blse : 方程係數一次只能有三個")
            case "df" :
                pass
            case _ :
                G.cs()
                print("沒有這個數學函式命令")

    elif prefix[0] == "#" :
        match prefix[1:] :
            case "ad" :
                cmdes = input("要增加的命令 > ")
                d = input("命令的簡單描述\n     > ")
                de = input("命令的詳細描述\n     > ")
                try :
                    with open("pymodle\\mathcmddata.json", "r", encoding = "UTF8") as f :
                        c = json.load(f)
                    mathcmdlist = c["mathcmdlist"]
                    decmdlist = c["decmdlist"]
                    mathcmdlist[cmdes] = d
                    decmdlist[cmdes] = de
                    c = {
                        "mathcmdlist": mathcmdlist,
                        "decmdlist" : decmdlist
                    }
                    with open("pymodle\\mathcmddata.json", "w") as f :
                        json.dump(c, f, indent = 4)
                except FileNotFoundError :
                    print("dskmahsysfunction.py > mathmod > ad : 找不到檔案")
            case "mathcmd" :
                try :
                    with open("pymodle\\mathcmddata.json", "r", encoding = "utf8") as f :
                        data = json.load(f)
                    mathcmdlist = data["mathcmdlist"]
                    print(mathcmdlist[cmd[1]])
                except FileNotFoundError :
                    print("dskmahsysfunction.py > mathmod > mathcmd : 找不到檔案")
            case "dicmd" :
                try :
                    with open("pymodle\\mathcmddata.json", "r", encoding = "utf8") as f :
                        data = json.load(f)
                    decmdlist = data["decmdlist"]
                    print(decmdlist[cmd[1]])
                except FileNotFoundError :
                    print("dskmahsysfunction.py > mathmod > mathcmd : 找不到檔案")
            case _:
                print("dskmahsysfunction.py > mathmod > mathcmd : 沒有這個指令")