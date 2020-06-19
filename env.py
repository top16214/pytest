# -*- coding:utf-8 -*-

import sys
from site import getsitepackages

# python的搜索路径
# the list of directories Python goes through to search for modules and files
print("Python's search path:\n{}".format(sys.path))
# python执行文件路径
print(sys.executable)
# 包的安装路径
print(getsitepackages())
# python版本号
print(sys.version_info)
print("Python major version is: {}".format(sys.version_info[0]))
# system平台
print("OS platform:{}".format(sys.platform))
# 系统最大整数值、最大unicode值
print("OS max int value: {}\nOS max unicode value: {}".format(sys.maxsize, sys.maxunicode))
print()
# 任意对象占用内存字节数
li = [3.14, 2, "j", "hello,world!", {"name": "neo", "age": 38}]
for item in li:
    print("{} occupies {} bytes.".format(item, sys.getsizeof(item)))

print()
