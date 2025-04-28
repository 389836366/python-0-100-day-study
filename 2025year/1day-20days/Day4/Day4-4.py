#计算圆的周长和面积 Version: 1.1
#周长=2πr，面积=πr²
import math

radius = float(input('请输入半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长={perimeter:.2f}')
print(f'面积={area:.2f}')