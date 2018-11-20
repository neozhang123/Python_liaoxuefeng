#一个参数
def power(x):
    return x*x
print(power(6))
#两个参数
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(7, 2))
#两个参数,设置参数默认值
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power2(7))
#默认参数的另一个例子
def enroll(name, gender, age=6, city='beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)

enroll('张三', 'F')
enroll('李四', 'M', '26', '加州')

#默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    print(L)
add_end([1, 2, 3])
add_end()
add_end()
add_end()
print('=========修改后==========')
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    print(L)
add_end()
add_end()
add_end()

print('=========(个数)可变参数: *args 接收一个tuple==========')
#num接受到的是一个tuple
def calc(*num):
    sum = 0
    for n in num:
        sum = sum + n*n
    print(sum)
calc(1, 2, 3, 4)
num = [1, 2, 3]
calc(*num)

print('=========关键字参数: **kw 接收一个dict==========')
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)
person('neo', 18)
person('leo', 20, city = '北京')
extra = {'city': '北京', 'job': '程序员'}
person('neo', 18, **extra)

#关键字参数命名
def person1(name, age, *, city, job):
    print('name', name, 'age', age, 'other', city, job)
person1('neo', 18, city='北京', job='程序员')
    

















