# 打包和解包操作

# 打包操作
a= 1, 10, 100
print(type(a))
print(a)
# 解包操作
i, j, k = a
print(i, j, k)
# 星号表达式
a =1, 10, 100, 1000
i, j, *k = a
print(i, j,k)
i, *j, k = a
print(i, j, k)
*i, j, k = a
print(i, j, k)
*i, j = a
print(i, j)
i, *j = a
print(i, j)
i, j, k, *l = a
print(i, j, k, l)
i, j, k, l, *m = a
print(i, j, k, l, m)
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)