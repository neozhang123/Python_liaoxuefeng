#利用循环构造一个list
L = []
n = 0
while n <= 99:
    L.append(n)
    n = n + 1
print(L)
#L[m:n] 取到第m到第n个元素（索引范围：m~(n-1)）
print(L[0:3])
print(L[-2:-1])
print(L[-4:-1])
print(L[:10])   #取前十个数
print(L[-10:])  #取后十个数
print(L[20:30]) #第21-30个数
print(L[10:20:3]) #每隔三个数去一次
print(L[::5])

L1 = L[:]   #复制一个L

#切片操作同样可以在tuple和字符创上进行
t = (0,1,2,3,4,5)[:4]
print(t)
s = 'abcdefghi'[-6:-2]
print(s)

print('==============练习=================')
def trim(s):
    l = len(s)
    n = 0
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
test = '   zhangliang  '  
print(test)     
print(trim(test))
print(trim(test)=='zhangliang')

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

















