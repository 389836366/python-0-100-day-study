# 字典的运算
person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 成员运算
print('name' in person)
print('tel' in person)

# 索引运算
print(person['name'])
print(person['addr'])
person['age'] = 25
person['height'] = 178
person['tel'] = 13122334455
person['signature'] = '不知道说什么，随便打点字上去'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')
    