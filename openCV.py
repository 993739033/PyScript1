import cv2
import time
import numpy as np
im = cv2.imread(r"C:\Users\gjt66\Desktop\meizi.jpg",1)
print(im.shape)
im= cv2.resize(im,(250,250))
gary = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow("Imge",im)
cv2.imshow("Imge_gary",gary)
cv2.imwrite(r"img_crop\meizi1.jpg",im)
# 等待下一个按键 0为等待时间(单位毫秒) 之后销毁所有界面窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# 好像是调用摄像头
# im1= cv2.VideoCapture(0)

# 1、 颜色空间转换  ??
# im2 = cv2.imread(r"C:\Users\gjt66\Desktop\meizi.jpg",1)
# imtemp = cv2.resize(im2,(300,300))
# lower_blue = np.array([110,50,50])# 设定蓝色的阈值
# upper_blue = np.array([130,255,255])
# mask = cv2.inRange(imtemp, lower_blue, upper_blue)# 根据阈值构建掩模
# res = cv2.bitwise_and(imtemp, imtemp, mask=mask)# 对原图像和掩模进行位运算
#
# cv2.imshow("img2",imtemp)
# cv2.imshow("img2_mask",mask)
# cv2.imshow("img2_bit",res)
# cv2.waitKey(0)