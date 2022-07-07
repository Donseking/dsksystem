import json
from pymodle.mathmod import MathTools as m
from pymodle.dskmod import GeneralTools as G
import pymodle.dskmod as dm

class DskError(Exception):
    pass

def MathMod(cmd : list) :
    prefix = cmd[0]
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
                G.cs()
                num = tuple(list(map(int, input("一元二次方程式的係數 [ 空格相隔 ] > ").split())))
                ans = m.one_dimensional_equation(num)
                if type(ans) == list :
                    for i in ans :
                        print(i)
                else :
                    print(ans)
            case "vct" :
                G.cs()
                a = input("第一個座標點 > ").split()
                b = input("第二個座標點 > ").split()
                a = list(map(int, a))
                b = list(map(int, b))
                ans = m.two_cdt_to_vector(a, b)
                print(ans)
            case "vlon" :
                G.cs()
                v = input("向量 > ").split()
                v = tuple(list(map(int, v)))
                ans = m.vector_long(v)
                print(ans)
            case "v+" :
                G.cs()
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
                G.cs()
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
                G.cs()
                l1 = list(map(int, input("首聯立方程係數 [ a, b, c ]\n    > ").split()))
                l2 = list(map(int, input("次聯立方程係數 [ a, b, c ]\n    > ").split()))
                if len(l1) == 3 and len(l2) == 3 :
                    ans = m.Binary_Linear_Simultaneous_Equations(l1, l2)
                    print(ans)
                else :
                    print("dskmathsysfunction > blse : 方程係數一次只能有三個")
            case "df" :
                G.cs()
                deg = int(input("函式最高次\n   > "))
                al = list(map(int, input("函式係數\n    > ").split()))
                ans = m.df(deg, al)
                print(ans)
            case "itgl" :
                G.cs()
                deg = int(input("函式最高次\n   > "))
                ct = list(map(int, input("函式係數\n    > ").split()))
                ch = input("是否有界 [ Y / N ]\n    > ").lower()
                if ch == "y" :
                    scp = list(map(int, input("上界 下界\n    > ").split()))
                    if len(scp) == 2 :
                        ans = m.integral(deg, ct, scope = True, uplim = scp[0], downlim = scp[1])
                        print(ans)
                    else :
                        print("dskmahsysfunction > itgl : 上界下界總共兩個")
                elif ch == "n" :
                    ans = m.integral(deg, ct)
                    print(ans)
                else :
                    print("dskmathsysfunction > itgl : 請正確輸入")
            case "fun" :
                G.cs()
                deg = int(input("函式最高次 > "))
                ct = list(map(int, input("函式係數 > ").split()))
                print(m.fun(deg, ct))
            case "lim" :
                G.cs()
                f = input("Function > ")
                approach = input("趨近於 > ")
                if approach == "oo" :
                    ans = m.lim(f, approach)
                    print(ans)
                else :
                    approach = int(approach)
                    ans = m.lim(f, approach)
                    print(ans)
            case "rm" :
                G.cs()
                cdt = list(map(int, input("旋轉點 > ").split()))
                td = int(input("角度 > "))
                ans = m.rotation_matrix(cdt, td)
                print(ans)
            case "sum" :
                G.cs()
                f = input("方程式\n    > ")
                mm = list(map(int, input("min max > ").split()))
                ans = m.sumer(f, mm[0], mm[1])
                print(ans)
            case "log" :
                G.cs()
                b = int(input("底數 > "))
                tn = int(input("真數 > "))
                print(m.log_(b, tn))
            case "fc" :
                G.cs()
                try :
                    x = input("階乘 > ")
                    print(m.fact(x))
                except :
                    print("dsksysfunction > fct : 輸入錯誤")
            case _ :
                G.cs()
                try :
                    f = dm.Turning.list_turn_str(cmd, " ")
                    ans = m.symadd(f)
                    if type(ans) != type(m.symadd("c")):
                        G.cs()
                        print(ans)
                    else :
                        raise DskError
                except DskError:
                    print("系統沒有這個指令")

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