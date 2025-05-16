# 读写文本文件
file = open('data.txt', 'r', encoding='utf-8')
print(file.read())
file.close()