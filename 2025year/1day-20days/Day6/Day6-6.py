import random

answer = random.randrange(1,101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('你猜小了，废物')
    elif num > answer:
        print('你猜大了，垃圾')
    else:
        print('你真棒，让我奖励你一下')
        break
print(f'你一共猜了{counter}次')
