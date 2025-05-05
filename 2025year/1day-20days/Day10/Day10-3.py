# 交换变量的值
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

a = 3
b = 4
c = 5
print(a, b, c)
a, b, c = b, c, a
print(a, b, c)
