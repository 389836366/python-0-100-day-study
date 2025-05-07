# 字典的方法
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))
print(person.get('sex'))
print(person.get('sex', True))

person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.keys())
print(person.values())
print(person.items())
for key, value in person.items():
    print(f'{key}:\t{value}')

person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1.update(person2)
print(person1)

person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))
print(person)
print(person.popitem())
print(person)
person.clear()
print(person)