# 字符串的运算

# 拼接和重复
s1 = 'hello' + ', ' + 'world'
print(s1)
s2 = '!' * 3
print(s2)
s1 += s2
print(s1)
s1 *= 2
print(s1)

# 比较运算
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '李咏洋'
print(ord('李'))
print(ord('咏'))
print(ord('洋'))

# 成员运算
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)
print('wo' not in s2)
print(s2 in s1)

# 获取字符串长度
s = 'hello, world'
print(len(s))
print(len('goodbye, world'))

# 索引和切片
s = 'abc123456'
n = len(s)
print(s[0], s[-n])
print(s[n-1], s[-1])
print(s[2], s[-7])
print(s[5], s[-4])
print(s[2: 5])
print(s[-7:-4])
print(s[2:])
print(s[:2])
print(s[::2])
print(s[::-1])