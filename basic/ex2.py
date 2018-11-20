#转义字符的应用
print('I\'m ok.')
print('I\'m looking at *** \t *** you\n hahaha')
print(r'\\\\\\\\\\')
print('''hello,
lalala,
world''')

#布尔值True   False（注意大写）
print(3<5)
#可以用and、or、not进行运算
true = True
false = False
print(true and true)
print(false and true)
print(false or true)
print(false and false)
print(not true)

#None是一个特殊的空值，跟0不一样
#练习
print('n = 123')
print('f = 456.789')
print('s1 = \'Hello, world\'')
print('s2 = \'Hello, \\\'Adam\\\'')
print('s3 = r\'Hello, \"Bart\"\'')
print('s4 = r\'\'\'Hello,\nLesa!\'\'\'')

#字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('张良，啦啦啦！')
