print(abs(-100))
print(max(3, 3, 4, 5))
#数据类型转换
#print(int('a'))   #int只能转换数字形式的str，此语句会报错
print(int('123'))
print(int(18.99))
print(str(1.23))
print(float('9.99'))
print(bool(100))
print(bool('None'))   #这条居然是True
print(bool(''))  # False

#练习
n = 255 
m = 1000
str1 = hex(n)
str2 = hex(m)
print(str1,    str2)
