import win32gui, win32api

className = "Chrome_WidgetWin_1"
titleName = "Python接口自动化测试实战 - 网易云课堂 - Google Chrome"
win = win32gui.FindWindow(className, titleName)
tid = win32gui.FindWindowEx(win, None, 'Intermediate D3D Window', None)  # 子窗口
win32gui.SetForegroundWindow(win)
print(win, ">>", tid)
print(win32gui.GetWindowRect(win))
print(win32gui.GetWindowRect(tid))
