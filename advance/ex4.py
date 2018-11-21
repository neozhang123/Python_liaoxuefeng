#生成器generator：一边循环一边计算的机制

#生成式和生成器的区别在于[]变成()
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
for n in g:
    print(n)

#斐波那契数列的普通函数做法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))
#generator改写：讲print(b)改写为yield b
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))
for n in fib(6):
    print(n)

print('---------------杨辉三角------------------')
def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
#测试
results = []
n = 0
for t in triangles():
    print(t)
    #results.append(t)
    n = n + 1
    if n == 10:
        break





















    
    















    
