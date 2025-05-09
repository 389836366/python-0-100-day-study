# 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置
import random
import string

ALL_CHARS = string.digits + string.ascii_letters
def generate_code(*, code_len=4):
    return ''.join(random.choices(ALL_CHARS, k=code_len))

for _ in range(5):
    print(generate_code())