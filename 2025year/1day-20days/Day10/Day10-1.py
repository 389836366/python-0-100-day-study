# 元组的定义和运算
t1 = (35, 12, 98)
t2 = ('骆昊', 45, True, '四川成都')
# 查看变量的类型
print(type(t1))
print(type(t2))
# 查看元组中元素的数量
print(len(t1))
print(len(t2))
# 索引运算
print(t1[0])
print(t1[1])
print(t2[-1])
# 切片运算
print(t2[:2])
print(t2[::3])
# 循环遍历元组中的元素
for elem in t1:
    print(elem)
# 成员运算
print(12 in t1)
print(99 in t1)
print('Hao' not in t2)
# 拼接运算
t3 = t1 + t2
print(t3)
# 比较运算
print(t1 == t3)
print(t1 >= t3)
print(t1 <= (35, 11, 99))