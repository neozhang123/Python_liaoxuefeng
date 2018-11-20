#dict内部存放的顺序和key放入的顺序是没有关系的
#和list相比：dict是一种以空间换时间的一种方法
#在dict中，key的数据类型必须是不可变的，整数，字符串等都可以，list不行
d = {'张三': 95, '李四':88, '王五':79}
print(d)
print(d['张三'])
d['Adam'] = 89
print(d)
print('Adam' in d)
print(d.get('张三'))
d.pop('Adam')
print(d)


print('============================================')
#set是一组key的组合，不能重复
#创建set需要一个list作为输入
s = set([1, 2, 3]) 
print(s)             #set是无序的，与显示无关
s = set([1, 2, 3, 2, 1, 5]) 
print(s)
#.add   .remove方法增加删除key
s.add(8)
s.add(9)
print(s)
s.remove(1)
print(s)
#set可以看成数学上无序和无重复元素的组合，可以做交集，并集工作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s_and = s1 & s2
print(s_and)
s_or = s1 | s2
print(s_or)

















