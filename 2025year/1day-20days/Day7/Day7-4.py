#百钱百鸡问题
for x in range(0 , 21):
    for y in range(0 , 34):
        for z in range(0 , 100 , 3):
            if x + y + z == 100 and x * 5 + y * 3 + z // 3 == 100:
                print(f'公鸡有{x}只,母鸡有{y}只，小鸡有{z}只')

for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')