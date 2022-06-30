import math
import numpy as np

class MathTools :

    def __init__(self) -> None:
        pass


    # x = (xa, xb, xc)  y = (ya, yb, yc)
    def cros(x : tuple, y : tuple) :
        rxa = (x[1], x[2])
        rya = (y[1], y[2])
        na = MathTools.second_order(rxa, rya)
        rxb = (x[2], x[0])
        ryb = (y[2], y[0])
        nb = MathTools.second_order(rxb, ryb)
        rxc = (x[0], x[1])
        ryc = (y[0], y[1])
        nc = MathTools.second_order(rxc, ryc)
        return (na, nb, nc)



    # x = (xa, xb)  y = (ya, yb)  thida = 角度
    def dot(x : tuple, y : tuple, angle = False, thida = 0) :
        if angle == False :
            if len(x) == 3 and len(y) == 3 :
                ans = x[0]*y[0] + x[1]*y[1] + x[2]*y[2]
                return ans
            elif len(x) == 2 and len(y) == 2 :
                ans = x[0]*y[0] + x[1]*y[1]
                return ans
        else :
            if len(x) == 3 and len(y) == 3 :
                xlong = (x[0]**2 + x[1]**2 + x[2]**2)**0.5
                ylong = (y[0]**2 + y[1]**2 + y[2]**2)**0.5
                ans = xlong*ylong*math.cos(math.radians(thida))
                return ans
            elif len(x) == 2 and len(y) == 2 :
                xlong = (x[0]**2 + x[1]**2)**0.5
                ylong = (y[0]**2 + y[1]**2)**0.5
                ans = xlong*ylong*math.cos(math.radians(thida))
                return ans


    # [a, b] <- row1
    # [c, d] <- row2
    def second_order(row1 : list, row2 : list) :
        if len(row1) == 2 and len(row2) == 2 :
            answer = row1[0]*row2[1] - row1[1]*row2[0]
            return answer
        else :
            return None


    # [a, b, c] <- row1
    # [d, e, f] <- row2
    # [g, h, i] <- row3
    def third_order(row1 : tuple, row2 : tuple, row3 : tuple) :
        if len(row1) == 3 and len(row2) == 3 and len(row3) == 3 :
            ans1 = row1[0]*row2[1]*row3[2] + row1[1]*row2[2]*row3[0] + row2[0]*row3[1]*row1[2]
            ans2 = row1[2]*row2[1]*row3[0] + row1[0]*row2[2]*row3[1] + row1[1]*row2[0]*row3[2]
            return ans1 - ans2
        else :
            return None

    def matrix_multiplication(A : list, B : list) :
        a = False
        b = False
        if len(A[0]) == len(B) :
            rowlong = len(A[0])
            for i in range(1, len(A)) :
                if len(A[i]) != rowlong :
                    print("MathMod - matrix_pultiplication : 輸入的首矩陣列數並沒有相同的長度")
                    break
                else :
                    a = True
            rowlong = len(B[0])
            for i in range(1, len(B)) :
                if len(B[i]) != rowlong :
                    print("MathMod - matrix_pultiplication : 輸入的次矩陣列數並沒有相同的長度")
                    break
                else :
                    b = True
            if a == True and b == True :
                c = np.array(A)
                d = np.array(B)
                ans = c.dot(d)
                return ans
        else :
            print("MathMod - matrix_pultiplication : 輸入的次矩陣行數[ 橫向 ]要與首矩陣的列數[ 直向 ]相同")


    # cdt (x, y)  line [ax + by + c = 0]: (a, b, c) || cdt (x, y, z) line [ax + by + cz + d = 0]: (a, b, c, d)
    def D(cdt : tuple, line : tuple) :
        if len(cdt) == 3 and len(line) == 4 :
            down = (line[0]**2 + line[1]**2 + line[2]**2)**0.5
            up = cdt[0]*line[0] + cdt[1]*line[1] + cdt[2]*line[2] + line[3]
            ans = abs(up)/down
            return ans
        elif len(cdt) == 2 and len(line) == 3 :
            down = (line[0]**2 + line[1]**2)**0.5
            up = cdt[0]*line[0] + cdt[1]*line[1] + line[2]
            ans = abs(up)/down
            return ans

    # line : ax2 + bx + c = 0 (a, b, c)
    def one_dimensional_equation(line : tuple) :
        if (line[1]**2 - 4*line[0]*line[2]) > 0 and line[0] != 0:
            x1 = -line[1] + (line[1]**2 - 4*line[0]*line[2])**0.5
            x2 = -line[1] - (line[1]**2 - 4*line[0]*line[2])**0.5
            x1 = x1/2*line[0]
            x2 = x2/2*line[0]
            return [x1, x2]
        elif (line[1]**2 - 4*line[0]*line[2]) == 0 and line[0] != 0 :
            x1 = -line[1] + (line[1]**2 - 4*line[0]*line[2])**0.5
            x1 = x1/2*line[0]
            return x1
        else :
            return "無解"

    # Vector (a, b) | (a, b, c)
    def vector_long(v : tuple) :
        if len(v) == 2 :
            return (v[0]**2 + v[1]**2)**0.5
        elif len(v) == 3 :
            return (v[0]**2 + v[1]**2 + v[2]**2)**0.5

    def vectorplus(v1 :tuple, v2: tuple) :
        v30 = v1[0] + v2[0]
        v31 = v1[1] + v2[1]
        v32 = v1[2] + v2[2]
        return (v30, v31, v32)

    # ax + by + c = 0
    # L = (a, b, c) | M = (d, e, f) 係 數
    def intersection_of_two_lines(L : list, M : list) :
        a = L[0]
        d = M[0]
        b = 0 - (L[1]/a)
        c = L[2]/a
        for i in L :
            L[L.index(i)] = i*d
        for i in M :
            M[M.index(i)] = i*a
        bdae = L[1] - M[1]
        cdaf = L[2] - M[2]
        y = 0-(cdaf/bdae)
        x = b*y - c
        return (x, y)