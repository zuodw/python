from tkinter import Tk
from time import sleep
import win32com.client as win32

RANGE = range(3,8)

def excel():
    app = 'Excel'
    x1 = win32.gencache.EnsureDispatch('%s.Application' % app)
    ss = x1.Workbooks.Add()
    sh = ss.ActiveSheet
    x1.Visible = True
    sleep(1)
    sh.Cells(1,1).Value = 'Python-to-%s Demo' % app
    sleep(1)

    for i in RANGE:
        sh.Cells(i,1).Value = 'Line %d' % i
        sleep(1)
    sh.Cells(i+2, 1).Value = "Th-th-th-that's all folks!"

    ss.Close(False)
    x1.Application.Quit()

    if __name__ == '__main__':
        Tk().withdraw()
        excel()