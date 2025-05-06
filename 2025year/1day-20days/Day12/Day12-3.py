# 集合的方法
from itertools import cycle

set1 = {1, 10, 100}
# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)

# 清空元素
set1.clear()
print(set1)