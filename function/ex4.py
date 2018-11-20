#递归函数

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
    
print(fact(100))
#print(fact(1000))   #此语句造成栈溢出，可以通过尾递归来进行优化
#但是任何语言都没有针对尾递归进行优化，所以任何递归函数都存在栈溢出的问题

#用递归函数实现罗汉塔的移动：
def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(5,'A', 'B', 'C')
