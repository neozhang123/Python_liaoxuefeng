#列表list

classmates = ['zhangliang', 'wangxu', 'fuxiaoyang']
print(classmates)
print(len(classmates))
#索引-1直接取到最后一个元素
#   -2倒数第二个元素
print(classmates[-1])
print(classmates[-2])
#append方法追加元素到末尾
classmates.append('wangmanna')
print(classmates)
#insert, pop, 方法
classmates.insert(0, 'Neo')
print(classmates)
classmates.pop(0)
classmates.pop()
print (classmates)



#元组tuple，一旦赋值便不能修改、
classmates = ('zhangliang', 'wangxu', 'fuxiaoyang')
#只有1个元素的tuple定义时必须加一个逗号
t = (1,)
print(t)
#tuple中的不变指的是“指向不变”   如果其中有元素为一个list，list内的元素可以改变
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'S'
t[2][1] = 'B'
print(t)















