#寻找100-999的水仙花数
for num in range(100 , 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


##寻找1000-9999的水仙花数
for number in range(1000 , 10000):
    a = number % 10
    b = number // 10 % 10
    c = number // 100 % 10
    d = number // 1000
    if number == a ** 4 + b ** 4 + c ** 4 + d ** 4:
        print(number)

