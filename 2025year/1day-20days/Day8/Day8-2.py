#列表的运算
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)
print(items6 + items7)
items5 += items6
print(items5)
print(items6 * 3)
print(items7 * 2)
print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])
print(items8[2])
print(items8[4])
items8[2] = 'durian'
print(items8)
print(items8[-5])
print(items8[-4])
print(items8[-1])
items8[-4] = 'strawberry'
print(items8)
print(items8[1:3])
print(items8[:3:1])
print(items8[::2])
print(items8[-4:-2])
print(items8[-2::-1])
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True
print(nums2 >= nums3)  # False