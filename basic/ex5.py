age = 28
if age >= 25:
    print('abcdefg')
    print('lalala')
else:
    print('1234567')
    print('enenen')

#只要条件是非零数值、非空字符串、非空list，就判断为True
x = 'x'
if x:
    print('True')

#类型转换函数int()函数发现一个字符串并不是合法的数字时就会报错

#练习
height = input('请输入您的身高：')
weight = input('请输入您的体重：')
height = float(height)
weight = float(weight)
bmi = weight / pow(height, 2)
print(bmi)
if bmi <= 18.5:
    print('太轻了')
elif bmi <= 25 and bmi > 18.5:
    print('正常')
elif bmi <= 28 and bmi > 25:
    print('过重')
elif bmi <= 32 and bmi > 28:
    print('过重')
else:
    print('严重肥胖')






