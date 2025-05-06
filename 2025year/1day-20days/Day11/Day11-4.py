# 字符串的方法

# 大小写相关操作
s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())
# 字符串每个单词首字母大写
print(s1.title())
# 字符串变大写
print(s1.upper())
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())
# 检查s1和s2的值
print(s1)
print(s2)
# 查找操作
s = 'hello, world!'
print(s.find('or'))
print(s.find('or', 9))
print(s.find('of'))
print(s.index('or'))

# 性质判断
s1 = 'hello, world!'
print(s1.startswith('He'))
print(s1.startswith('hel'))
print(s1.endswith('!'))
s2 = 'abc123456'
print(s2.isdigit())
print(s2.isalpha())
print(s2.isalnum())
# 格式化
s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033
# 修剪操作
s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界
# 替换操作
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world
# 拆分与合并
s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you

