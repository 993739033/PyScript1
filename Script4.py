from PIL import Image,ImageGrab
import win32api,win32con,win32gui
# im = ImageGrab.grab()
# print(im.size)
# print(im.mode)
# im.show()

# im2 = ImageGrab.grab((300,300,800,800))
# im2.show()
# im2.save(r"C:\Users\gjt66\Desktop\grabImg1.jpg")


# win32api.MessageBox(None,"hello world","hello",win32con.MB_YESNO)

# 写入文本到记事本中
win = win32gui.FindWindow('Notepad','text.txt - 记事本')#父窗口 类名+标题
win32gui.SetForegroundWindow(win)#将文件窗口置于最前方
tid = win32gui.FindWindowEx(win,None,'Edit',None)#子窗口 类名
print(win32gui.GetWindowRect(win))
print(win32gui.GetWindowRect(tid))
win32gui.SendMessage(tid, win32con.WM_SETTEXT, None, '你好hello word!')
win32gui.PostMessage(tid,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
print("%x" % tid)
print("%x" % win)
