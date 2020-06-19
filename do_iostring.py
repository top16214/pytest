#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
数据读写不一定是文件，也可以在内存中进行。

StringIO 顾名思义就是在内存中以 io 流的方式读写 str
'''

from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')            # 返回 5，也即写入的字符数目
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
