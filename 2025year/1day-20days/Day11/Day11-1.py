# 字符串的定义
s1 = 'hello world'
s2 = "你好，世界!"
s3 = '''hello,
wonderful
world!'''
print(s1)
print(s2)
print(s3)

# 转义字符
s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)

# 原始字符串
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

# 字符的特殊表示
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1)
print(s2)
