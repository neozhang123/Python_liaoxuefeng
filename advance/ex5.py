#------------迭代器----------------
#直接作用在for循环的对象称为：可迭代对象（Iterable）
#可以被next()调用不断返回下一个的叫做迭代器（Iterator）
#1、集合数据类型：list, tuple, dict, set, str
#2、generator

#用isinstance()判断一个对象是否是Iterable对象
"""
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
"""
#用isinstance()判断一个对象是否为Iterator对象
"""
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
"""
#list, dict ,str不是Iterator
#Iterator是惰性的，只有在需要返回值得情况下才会计算


















