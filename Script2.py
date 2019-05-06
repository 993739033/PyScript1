import time, threading
from collections import namedtuple
from datetime import datetime
from collections import defaultdict
import numpy
import pandas


def loop():
    print("thread name %s " % threading.current_thread().name)
    for i in range(5):
        time.sleep(1)
        print("thread end name %s" % threading.current_thread().name)


print("thread current name %s" % threading.current_thread().name)
t = threading.Thread(target=loop, name="looper")
# t.start()
# t.join()
print("end>>")

print(datetime.now())
time = datetime(2019, 12, 12, 12, 12)
print(time)

Pint = namedtuple("Point", ["x", "y"])
p = Pint(1, 2)
print(p.x, p.y)
print(isinstance(p, Pint))
print(type(p))

Circle = namedtuple("Circle", ["x", "y", "r"])
c = Circle(12, 3, 7)
print(c)

dd = defaultdict(lambda: "isnull")
dd["key1"] = "dd"
print(dd["key1"])
print(dd["key2"])
