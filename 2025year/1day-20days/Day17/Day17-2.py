# 递归调用
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)