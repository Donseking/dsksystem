from __future__ import print_function
import ctypes, sys
import os

def is_adman() :
    try :
        return ctypes.windll.shell32.IsUserAnAdmin()
    except :
        return False

p = os.path.abspath(os.getcwd())
p = p + "\\pymodle\\bat;"
if is_adman() :
    os.system(f"setx path {p}")
else :
    if sys.version_info[0] == 3 :
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else :
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)