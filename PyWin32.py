import win32con
import win32gui, win32api

className = "SunAwtFrame"
titleName = "PyScript1 [F:\PythonProject\PyScript1] - ...\PyWin32.py [PyScript1] - PyCharm"
win = win32gui.FindWindow(className, titleName)
tid = win32gui.FindWindowEx(win, None, 'Intermediate D3D Window', None)  # 子窗口
win32gui.SetForegroundWindow(win)
print(win, ">>", tid)
print(win32gui.GetWindowRect(win))
# print(win32gui.GetWindowRect(tid))
print(win32gui.GetWindowText(win))
print(win32gui.GetClassName(win))
#位移鼠标位置
win32api.SetCursorPos([500,500])
# 左右键单击
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP|win32con.MOUSEEVENTF_LEFTDOWN,0,0)
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP|win32con.MOUSEEVENTF_RIGHTDOWN,0,0)

# 发送回车键
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
# 关闭窗口
# win32gui.PostMessage(win,win32con.WM_CLOSE,0,0)
