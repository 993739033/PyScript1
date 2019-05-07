import win32gui
from PIL import ImageGrab
import numpy as np

# im = ImageGrab.grab()
# im.save(r"C:\Users\gjt66\Desktop\grabImg2.jpg")

className = "ThunderRT6FormDC"
titleName = "Minesweeper X"
saveDir = r"img\items_crop\\"  # 用于保存item的文件夹

left = 0
top = 0
right = 0
bottom = 0

item_count = 8
item_h = 0
item_w = 0

# 数字1-8 周围雷数
# 0 未被打开
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


# 每一格16px
def getCenterImg():
    global left, right, top, bottom, im2, item_h, item_w
    left += 15
    top += 100
    right -= 15
    bottom -= 16
    rect = (left, top, right, bottom)
    item_w = (right - left) / item_count
    item_h = (bottom - top) / item_count
    print("item w_h:", str(item_w), str(item_h))
    im = ImageGrab.grab()
    im.save(r"C:\Users\gjt66\Desktop\grabImg3.jpg")
    if im:
        im2 = im.crop(rect)
        if im2:
            im2.save(r"C:\Users\gjt66\Desktop\grabImg4.jpg")


def getItemsColor():
    print("开始获取颜色集合》》》》")
    global itemMap, crop_offset  # 保存不同item当前表示的状态
    itemMap = np.zeros((8, 8))
    crop_offset = 2  # 表示向内部偏移一段距离进行切割 防止可能的黑线不同颜色集合不同
    for y in range(item_count):
        for x in range(item_count):
            try:

                item_img = im2.crop((y * item_w, x * item_h, (y + 1) * item_w, (x + 1) * item_h))
                item_img = item_img.crop((crop_offset, crop_offset, item_w - crop_offset, item_h - crop_offset))

                # ##                                                                       ###
                # item_img.save(saveDir + "item[%s,%s].jpg" % (y, x))  # 这里做保存切割图处理    #
                # print("[x,y]=%s:%s colors=%s" % (y, x, item_img.getcolors()))              #
                # ##                                                                       ###


            except Exception as e:
                print(e)

            if item_img.getcolors() == rgba_0:
                itemMap[x][y] = 0  # 未被打开
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
            elif item_img.getcolors() == rgba_boom:
                itemMap[x][y] = -5  # 未触发的地雷 表示地雷
            elif item_img.getcolors() == rgba_boom_red:
                itemMap[x][y] = -6  # 触发地雷 表示地雷
                global gameover
                gameover = 1
            else:
                print("无法识别图像")
                print("坐标")
                print((y, x))
                print("颜色")
                print(item_img.getcolors())


win = win32gui.FindWindow(className, titleName)
win32gui.SetForegroundWindow(win)
if win:
    print("winID", win)
    print("找到窗口")
    left, top, right, bottom = win32gui.GetWindowRect(win)
    print(win32gui.GetWindowRect(win))
    getCenterImg()
    getItemsColor()
    print("itemitemMap:>>>>>\n", itemMap)
else:
    print("未找到窗口")
