import os
import time

os.system("adb shell input swipe 100 100 100 600")
time.sleep(2)
os.system("adb shell input swipe  100 900 100 100")