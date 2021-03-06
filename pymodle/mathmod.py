from __future__ import division
try :
    from sympy import *
    import math
    import os
except :
    os.system("pip install sympy")

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
    def third_order(a : list) :
        if len(a) == 2 :
            if len(a[0]) == 2 and len(a[1]) == 2 and len(a[2]) == 2 :
                a = Matrix(a).det()
            else :
                print("dskmahsysfunction > third_order : 每行都要有兩個元素")
        else :
            print("dskmahsysfunction > third_order : 總共要兩行")
        return a


    # [a, b, c] <- row1
    # [d, e, f] <- row2
    # [g, h, i] <- row3
    def third_order(a : list) :
        if len(a) == 3 :
            if len(a[0]) == 3 and len(a[1]) == 3 and len(a[2]) == 3 :
                a = Matrix(a).det()
            else :
                print("dskmahsysfunction > third_order : 每行都要有三個元素")
        else :
            print("dskmahsysfunction > third_order : 總共要三行")
        return a


    def matrix_multiplication(A : list, B : list) :
        m = Matrix(A)
        n = Matrix(B)
        ans = m*n
        return ans

    def addmatrix(a : list, b : list) :
        m = Matrix(a)
        n = Matrix(b)
        ans = m + n
        return ans

    def subtractmatrix(a : list, b : list) :
        m = Matrix(a)
        n = Matrix(b)
        ans = m - n
        return ans

    def inverse_matrix(m : list) :
        m = Matrix(m)
        ans = m**-1
        return ans

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
        # x = symbols("x", communtation = True)
        if len(line) == 3 :
            f = symbols("f", cls = Function)
            f = MathTools.fun(2, list(line))
            return roots(f)
        else :
            print("mathmod > one_dimensional_equation : 係數總共三個")

    # Vector (a, b) | (a, b, c)
    def vector_long(v : tuple) :
        if len(v) == 2 :
            x = str(v[0]**2 + v[1]**2)
            return x + "^0.5"
        elif len(v) == 3 :
            x = str(v[0]**2 + v[1]**2 + v[2]**2)
            return x + "^0.5"

    def vecotr_plus(v1 : tuple, v2 : tuple) :
        a = []
        if len(v1) == len(v2) :
            for i in range(len(v1)) :
                a.append(v1[i] + v2[i])
        elif len(v1) != len(v2) :
            print("mathmod.py > class MathTools > vector_plus : 向量要相同長度")
        return tuple(a)

    def two_cdt_to_vector(a : list, b : list) :
        if len(a) == 3 and len(b) == 3 :
            c = int(b[0] - a[0])
            d = int(b[1] - a[1])
            e = int(b[2] - a[2])
            l = (c, d, e)
            return l
        elif len(a) == 2 and len(b) == 2 :
            c = int(b[0] - a[0])
            d = int(b[1] - a[1])
            l = (c, d)
            return l
        else :
            return "mathmod > two_cdt_to_vector : 輸入錯誤"

    def Unary_quadratic_equation(l : list):
        x = symbols("x", communtative = True)
        f = symbols("f", cls = Function)
        if len(l) == 3 :
            f = (x**2)*l[0] + l[1]*x + l[2]
        return roots(f)

    def Binary_Linear_Simultaneous_Equations(l1 : list, l2 : list):
        for i in l1 :
            l1[l1.index(i)] = sympify(i)
        for i in l2 :
            l2[l2.index(i)] = sympify(i)
        x, y = symbols("x y", communtative = True)
        f1, f2 = symbols("f1 f2", cls = Function)
        f1 = l1[0]*x + l1[1]*y + l1[2]
        f2 = l2[0]*x + l2[1]*y + l2[2]
        ans = solve((f1, f2), (x, y))
        return ans

    def df(deg : int, arg : list):
        x = symbols("x", communtation = True)
        f = symbols("f", cls = Function)
        f = arg[0]*x**deg
        if len(arg) == deg + 1 :
            deg -= 1
            for i in range(1, deg + 2) :
                f += arg[i]*x**deg
                deg -= 1
            return f.diff()
        else :
            return "mathmod > df : 係數總數比最高次多一"

    def lim(fk, d):
        x = Symbol("x")
        return limit(sympify(fk), x, d)

    def fun(deg : int, arg : list):
        x = symbols("x", communtation = True)
        f = symbols("f", cls = Function)
        f = arg[0]*x**deg
        if len(arg) == deg + 1 :
            deg -= 1
            for i in range(1, deg + 2) :
                f += arg[i]*x**deg
                deg -= 1
            return f
        else :
            return "mathmod > fun : 係數總數比最高次多一"

    def integral(deg : int, cft : list, scope = False, uplim = 0, downlim = 0) :
        if scope == False :
            x = symbols("x", communtation = True)
            c = symbols("c", communtation = True)
            f = symbols("f", cls = Function)
            cft[0] = Rational(cft[0], (deg + 1))
            f = cft[0]*x**(deg + 1)
            deg -= 1
            for i in range(1, deg + 2) :
                cft[i] = Rational(cft[i], (deg + 1))
                f += cft[i]*x**(deg + 1)
                deg -= 1
            return f + c
        else :
            x = symbols("x", communtation = True)
            c = symbols("c", communtation = True)
            f = symbols("f", cls = Function)
            cft[0] = Rational(cft[0], (deg + 1))
            f = cft[0]*x**(deg + 1)
            deg -= 1
            for i in range(1, deg + 2) :
                cft[i] = Rational(cft[i], (deg + 1))
                f += cft[i]*x**(deg + 1)
                deg -= 1
            ans = f.evalf(subs = {x : uplim}) - f.evalf(subs = {x : downlim})
            return ans

    def rotation_matrix(cdt : list, thida):
        thida = pi * Rational(thida, 180)
        a = [cos(thida), -sin(thida)]
        b = [sin(thida), cos(thida)]
        m = Matrix([a, b])
        n = Matrix(cdt)
        ans = m*n
        return ans

    def sumer(fun, min, max):
        x = Symbol("x")
        ans = summation(simplify(fun), (x, min, max))
        return ans

    def sad(f) :
        return sympify(f)

    def log_(base, true_number):
        return log(true_number, base)

    def fact(x):
        return factorial(sympify(x))

    def evaluate(f, num) :
        x = Symbol("x")
        f = sympify(f)
        return f.subs(x, num)


class Physical_Formula :

    def velocity(s : int, t : int) :
        return Rational(s, t)