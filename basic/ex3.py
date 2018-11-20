#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#python用的是Unicode编码，支持多国语言
#编码转换，只能转换一个字符
print(ord('中'))
# print(ord('中国'))---这个会报错
print(chr(20013))

#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数
print('%s 是第%d个超级英雄！' % ('Mechial', 1024))

#练习
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('小明成绩提升了%.1f' % r)
