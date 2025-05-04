#添加和删除元素
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)
languages.insert(1, 'SQL')
print(languages)
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)
languages.pop()
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
items = ['Python', 'Java', 'C++']
del items[1]
print(items)
