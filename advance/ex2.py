#只要是可迭代对象，无论有无下标，都可以迭代

#比如dict就可以迭代，dict是无序的，迭代出来的顺序可能不一样,一下两个例子分别迭代key和value的值
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)

#比如字符串的迭代
for s in 'abcdefg':
    print(s)

#怎样判断一个对象是否可以进行迭代
#引入collections模块中的Iterable
#from collections import Iterable
#isinstance('abc', Iterable)
#isinstance(123, Iterable)
#isinstance([3,3,3], Iterable)

#内置的enumerate函数
l = ['A', 'B', 'C']
for j, value in enumerate(l):
    print(j, value)



#查找一个list中最大值和最小值
print('================练习=================')
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    Max = L[0]
    Mix = L[0]
    for i in L:
        if i > Max:
            Max = i
        if i < Mix:
            Mix = i
    return (Mix, Max)
L = [3,5,6,2,7,1,9]
print(findMinAndMax(L))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')



















