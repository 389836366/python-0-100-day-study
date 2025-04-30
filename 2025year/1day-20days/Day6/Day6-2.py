#使用while循环求和
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

#1-100偶数求和
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(f'结果为: {total}')

total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)

total = 0
for i in range(1 , 101):
    if i %2 != 0:
        continue
    total += i
print(total)



