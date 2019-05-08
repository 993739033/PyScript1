import win32gui, win32api, win32con
from PIL import ImageGrab
import numpy as np
import random
import time

# im = ImageGrab.grab()
# im.save(r"C:\Users\gjt66\Desktop\grabImg2.jpg")

className = "ThunderRT6FormDC"
titleName = "Minesweeper X"
saveDir = r"img_crop\items_crop\\"  # 用于保存item的文件夹
saveDirPic = r"img_crop\img\\"  # 用于保存大图的文件夹

# 此脚本只使用于win XP 风格扫雷软件

left = 0
top = 0
right = 0
bottom = 0
# 注意这里需要设置你当前选择的布局行数及列数 不然会报错 也可以使用自动 设置isAuto =True
item_count_y = 45  # 表示行数
item_count_x = 45  # 表示列数
isAuto = True  # 是否自动获取行列数
item_wh = 16  # 默认每个item宽高为16
item_h = 0
item_w = 0

# 数字1-8 周围雷数
# 0 未被打开
# -1 已经打开
# -4  插旗
# ed 被打开 空白
# hongqi 红旗
# boom 普通雷
# boom_red 踩中的雷
rgba_ed = [(144, (192, 192, 192))]
rgba_hongqi = [(12, (255, 255, 255)), (17, (255, 0, 0)), (93, (192, 192, 192)), (22, (0, 0, 0))]
rgba_0 = [(12, (255, 255, 255)), (132, (192, 192, 192))]
rgba_1 = [(104, (192, 192, 192)), (40, (0, 0, 255))]
rgba_2 = [(79, (192, 192, 192)), (65, (0, 128, 0))]
rgba_3 = [(62, (255, 0, 0)), (82, (192, 192, 192))]
rgba_4 = [(88, (192, 192, 192)), (56, (0, 0, 128))]
rgba_5 = [(74, (192, 192, 192)), (70, (128, 0, 0))]
rgba_6 = [(72, (192, 192, 192)), (72, (0, 128, 128))]
rgba_7 = [(100, (192, 192, 192)), (44, (0, 0, 0))]
rgba_8 = [(68, (192, 192, 192)), (76, (128, 128, 128))]
rgba_boom = [(4, (255, 255, 255)), (66, (192, 192, 192)), (74, (0, 0, 0))]
rgba_boom_red = [(4, (255, 255, 255)), (66, (255, 0, 0)), (74, (0, 0, 0))]

padding_left = 15
padding_top = 100
padding_right = 15
padding_bottom = 16
gameover = False
itemMap = np.zeros((item_count_x, item_count_y))


# 初始化参数
def initParms():
    global left, right, top, bottom, item_h, item_w, rect, item_count_x, item_count_y
    left += padding_left
    top += padding_top
    right -= padding_right
    bottom -= padding_bottom
    item_w = (right - left) / item_count_x
    item_h = (bottom - top) / item_count_y
    rect = (left, top, right, bottom)
    if isAuto:
        item_count_x = int((right - left) / item_wh)
        item_count_y = int((bottom - top) / item_wh)
        item_w = item_wh
        item_h = item_wh


# 每一格16px
def getCenterImg():
    global item_w, item_h, rect, im2
    print("item w_h:", str(item_w), str(item_h))
    im = ImageGrab.grab()
    im.save(saveDirPic + "cropImg1.jpg")
    if im:
        im2 = im.crop(rect)
        if im2:
            im2.save(saveDirPic + "cropImg2.jpg")


# 获取地图的数组集合
def getMap():
    getCenterImg()
    print("开始获取颜色集合》》》》")
    global itemMap, crop_offset, gameover  # 保存不同item当前表示的状态
    itemMap = np.zeros((item_count_x, item_count_y))
    crop_offset = 2  # 表示向内部偏移一段距离进行切割 防止可能的黑线不同颜色集合不同 识别报错时可以适当加大建议【2<=crop_offset<16】
    hasBlock = False
    for x in range(item_count_x):
        for y in range(item_count_y):
            # print("x:%s,y:%s"%(x,y))
            try:
                item_img = im2.crop((x * item_w, y * item_h, (x + 1) * item_w, (y + 1) * item_h))
                item_img = item_img.crop((crop_offset, crop_offset, item_w - crop_offset, item_h - crop_offset))

                # ##                                                                       ###
                # item_img.save(saveDir + "item[%s,%s].jpg" % (x, y))  # 这里做保存切割图处理    #
                # print("[x,y]=%s:%s colors=%s" % (x, y, item_img.getcolors()))              #
                # ##                                                                       ###

            except Exception as e:
                print(e)
            if item_img.getcolors() == rgba_0:
                itemMap[x][y] = 0  # 未被打开
                hasBlock = True
            elif item_img.getcolors() == rgba_1:
                itemMap[x][y] = 1
            elif item_img.getcolors() == rgba_2:
                itemMap[x][y] = 2
            elif item_img.getcolors() == rgba_3:
                itemMap[x][y] = 3
            elif item_img.getcolors() == rgba_4:
                itemMap[x][y] = 4
            elif item_img.getcolors() == rgba_5:
                itemMap[x][y] = 5
            elif item_img.getcolors() == rgba_6:
                itemMap[x][y] = 6
            elif item_img.getcolors() == rgba_7:
                itemMap[x][y] = 7
            elif item_img.getcolors() == rgba_8:
                itemMap[x][y] = 8
            elif item_img.getcolors() == rgba_ed:
                itemMap[x][y] = -1  # 已经打开
            elif item_img.getcolors() == rgba_hongqi:
                itemMap[x][y] = -4  # 插旗
            elif item_img.getcolors() == rgba_boom or item_img.getcolors() == rgba_boom_red:
                itemMap[x][y] = -5  # 未触发的地雷 表示地雷
                gameover = True
                print("Game OVER!!")
                if item_img.getcolors() == rgba_boom_red:
                    itemMap[x][y] = -6  # 触发地雷 表示地雷
                return
            else:
                print("无法识别图像")
                print("坐标")
                print((x, y))
                print("颜色")
                print(item_img.getcolors())
                gameover = True  # 防止成功后弹窗导致无法停止
                break
    if not hasBlock:
        gameover = True
        print("可能成功了！！")


# 进行插旗操作
def checkWithflag():
    global itemMap
    getMap()
    # print("flag itemMap:>>>\n", itemMap)
    for x in range(item_count_x):
        for y in range(item_count_y):
            boomNum = itemMap[x][y]
            if 1 <= boomNum and boomNum <= 8:
                blockCount = 0
                flagCount = 0
                for xx in range(x - 1, x + 2):
                    for yy in range(y - 1, y + 2):
                        if 0 <= xx and 0 <= yy and xx < item_count_x and yy < item_count_y:
                            if not (xx == x and yy == y):
                                itemValue = itemMap[xx][yy]
                                if itemValue == 0:
                                    blockCount += 1
                                elif itemValue == -4:
                                    flagCount += 1
                if boomNum == flagCount + blockCount and blockCount > 0:
                    for xx in range(x - 1, x + 2):
                        for yy in range(y - 1, y + 2):
                            if 0 <= xx and 0 <= yy and xx < item_count_x and yy < item_count_y:
                                if not (xx == x and yy == y):
                                    if itemMap[xx][yy] == 0:
                                        rightClickXY(xx, yy)
                                        itemMap[xx][yy] = -4


# 进行点击安全区域操作
def checkWithSafeBlock():
    global itemMap
    getMap()
    # print("safeBlock itemMap:>>>\n", itemMap)
    needLuck = True  # 是否需要luck点击
    for x in range(item_count_x):
        for y in range(item_count_y):
            boomNum = itemMap[x][y]
            if 1 <= boomNum and boomNum <= 8:
                blockCount = 0
                flagCount = 0
                for xx in range(x - 1, x + 2):
                    for yy in range(y - 1, y + 2):
                        if 0 <= xx and 0 <= yy and xx < item_count_x and yy < item_count_y:
                            if not (xx == x and yy == y):
                                itemValue = itemMap[xx][yy]
                                if itemValue == 0:
                                    blockCount += 1
                                elif itemValue == -4:
                                    flagCount += 1
                if boomNum == flagCount and blockCount > 0:
                    for xx in range(x - 1, x + 2):
                        for yy in range(y - 1, y + 2):
                            if 0 <= xx and 0 <= yy and xx < item_count_x and yy < item_count_y:
                                if not (xx == x and yy == y):
                                    if itemMap[xx][yy] == 0:
                                        leftClickXY(xx, yy)
                                        itemMap[xx][yy] = -1
                                        needLuck = False
    if needLuck:
        godLuck()


def godLuck():
    getMap()
    random_x = random.randint(0, item_count_x - 1)
    random_y = random.randint(0, item_count_y - 1)
    if itemMap[random_x][random_y] == 0:
        leftClickXY(random_x, random_y)


def leftClickXY(x, y):
    print("left click[%s,%s]" % (x, y))
    win32api.SetCursorPos((int(left + x * item_w + item_w // 2), int(top + y * item_h + item_h // 2)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def rightClickXY(x, y):
    win32api.SetCursorPos((int(left + x * item_w + item_w // 2), int(top + y * item_h + item_h // 2)))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


# 重新开始
def restart():
    global gameover
    gameover = False
    win32api.SetCursorPos((left + int((item_count_x * item_w) / 2), top - 25))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


win = win32gui.FindWindow(className, titleName)
win32gui.SetForegroundWindow(win)
if win:
    print("winID", win)
    print("找到窗口")
    left, top, right, bottom = win32gui.GetWindowRect(win)
    print(win32gui.GetWindowRect(win))
    initParms()
    time.sleep(0.5)
    restart()
    time.sleep(0.5)
    getMap()
    print("itemitemMap:>>>>>\n", itemMap)
    while (not gameover):
        print("game over is>>", str(gameover))
        checkWithflag()  # 查找能够插旗的位置进行插旗
        checkWithSafeBlock()  # 查找能够点击的白块进行点击
        # godLuck()
        # getMap()
        print("itemitemMap:>>>>>\n", itemMap)
else:
    print("未找到窗口")
