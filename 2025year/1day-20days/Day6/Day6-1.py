#1-100的整数求和
total = 0
for i in range(1 , 101):
    total += i
print(f'1-100整数求和的结果: {total}')

#1-100的偶数求和
total = 0
for i in range(1 , 101):
    if i % 2 == 0:
        total += i
print(f'1-100的偶数求和结果: {total}')

#修改range参数实现求和
total = 0
for i in range(2 , 101 , 2):
    total += i
print(total)

#使用sum函数求和
print(sum(range(2 , 101 , 2)))