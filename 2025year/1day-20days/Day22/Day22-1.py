# 读写JSON格式的数据
import json

my_dict = {
    'name': '李英语',
    'age': 21,
    'friends': ['zs', 'ls'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))

with open('data.json', 'w') as file:
    json.dump(my_dict, file)

with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)