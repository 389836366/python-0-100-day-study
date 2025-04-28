#计算圆的周长和面积 Version: 1.2
#周长=2πr，面积=πr²
import math

radius = float(input('请输入圆的半径: '))  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')
print(f'{area = :.2f}')
