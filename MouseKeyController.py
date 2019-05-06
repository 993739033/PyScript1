import pynput
from pynput.mouse import Button, Controller
import time


def printMousePos(m):
    print("mouse position:{0}".format(m.position))  # 获取鼠标位置信息


mouser = Controller()
printMousePos(mouser)
# mouser.position = (100, 200) #移动绝对位置
# mouser.move(50,-50)#移动相对位置
# 左键点击及释放
# mouser.press(Button.left)
# mouser.release(Button.left)
# 以下快速刷新功能
time.sleep(1)


def mouseEvent1():
    for i in range(100):
        time.sleep(0.2)
        mouser.press(Button.right)
        mouser.move(70, 70)
        mouser.release(Button.right)
        mouser.press(Button.left)
        mouser.release(Button.left)
        mouser.move(-70, -70)


# mouseEvent1()
mouser.scroll(0, 200)

print(" end  >>>")

from pynput.mouse import Listener


def on_move(x, y):
    # 监听鼠标移动
    print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    # 监听鼠标点击
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    # 监听鼠标滚轮
    print('Scrolled {0}'.format((x, y)))


# 连接事件以及释放
# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()

from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press(Key.space)
keyboard.release(Key.space)

with keyboard.pressed(Key.shift):
    # keyboard.press("a")
    # keyboard.release("a")
    with keyboard.pressed("a"):
        pass
keyboard.type('Hello World')  # 直接输入字符

## 监听键盘
from pynput.keyboard import Key, Listener

def on_press(key):
    # 监听按键
    print('{0} pressed'.format(key))

def on_release(key):
    # 监听释放
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# 连接事件以及释放
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
# pynput.mouse.Listener.stop() 用于停止监听 引发StopException 来停止
