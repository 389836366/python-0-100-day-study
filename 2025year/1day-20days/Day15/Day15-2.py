# 设计一个判断给定的大于1的正整数是不是质数的函数
def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True
