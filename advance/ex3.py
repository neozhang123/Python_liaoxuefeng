#利用列表生成式，可以快速生成list，也可以通过一个list快速推导出另一个list，代码十分简洁
L = list(range(1, 11))
print(L)
L1 = [x * x for x in range(1, 11)]
print(L1)
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L2)
L3 = [m + n for m in 'ABC' for n in 'abc']
print(L3)

#dict的items()方法
d = {'x': 0, 'y': 1, 'z':2}
for k, v in d.items():
    print(k, '=', v)
L4 = [k + '=' + str(v) for k, v in d.items()]
print(L4)

#讲list中所有字符变成小写
L5 = ['HELLO', 'WORLD']
L6 = [s.lower() for s in L5]
print(L6)
