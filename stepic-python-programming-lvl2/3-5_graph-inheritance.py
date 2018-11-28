# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть
# поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется
# явно от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.
# Sample Input:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Sample Output:
# A : 3
# B : 1
# C : 2

import json

d_edit = {i['name']: i['parents'] for i in json.loads(input())}


def find_path(start, key, const, child_lst):
    if (start == const and key not in child_lst):
        child_lst.append(key)
    for node in d_edit[start]:
        find_path(node, key, const, child_lst)


for i in sorted(d_edit):
    child_lst = []
    for key in d_edit.keys():
        find_path(key, key, i, child_lst)
    print(i + ' : ' + str(len(child_lst)))
