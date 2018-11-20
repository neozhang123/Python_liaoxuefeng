def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
#如果没有返回值，则return None，或者简写成return
#导入函数语句格式：
#   from 文件名 import 函数名

#空函数：用来做占位符，后续补充代码
#pass语句可以放在其他语境下，作占位符
def nop():
    pass
print('================函数的参数检查==================')
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数错啦！')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-1111))
print(my_abs('abc'))


