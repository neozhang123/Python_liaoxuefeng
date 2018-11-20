names = ['a', 'b', 'c', 'd']
#for x in ...就是把每个元素带入到变量x，然后执行缩进的语句
for name in names:
    print(name)
#range(n+1)生成0-n的整数序列
sum = 0
for x in range(101):
  sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#练习
L = ['zhangsan', 'lisi', 'wangwu']
for l in L:
    print('Hello, %s' % l)
