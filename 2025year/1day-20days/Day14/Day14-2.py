# 函数的参数
def make_judagement(a, b, c):
    return a + b > c and a + c > b and b + c > a
print(make_judagement(1, 2, 3))
print(make_judagement(4, 5, 6))

# 参数的默认值
from random import randrange
def roll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total
print(roll_dice())
print(roll_dice(3))

def add(a=0, b=0, c=0):
    return a + b + c
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

# 可变参数
def add(*args):
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val
    return total
print(add())