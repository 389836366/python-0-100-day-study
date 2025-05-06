# 集合的运算

# 成员运算
set1 = {11, 12, 13, 14, 15}
print(10 in set1)
print(15 in set1)
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)
print('Java' in set2)
# 二元运算
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
# 交集
print(set1 & set2)
print(set1.intersection(set2))
# 并集
print(set1 | set2)
print(set1.union(set2))
# 差集
print(set1 - set2)
print(set1.difference(set2))
# 对称差
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
# 比较运算
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}
print(set1 < set2)
print(set1 <= set3)
print(set2 < set3)
print(set2 <= set3)
print(set2 > set1)
print(set2 == set3)

print(set1.issubset(set2))
print(set2.issuperset(set1))
