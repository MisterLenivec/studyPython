# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# Пример:
# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
# имеют ценность 3. И т. д.
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
# Sample Input:
# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
# Sample Output:
# 4 3 1
# First solution
from xml.etree import ElementTree

root = ElementTree.fromstring(input())
d = {'red': 0, 'green': 0, 'blue': 0}


def find_val(root, count):
    if (root.tag == 'cube' and root.attrib['color'] in d):
        d[root.attrib['color']] += count
    for node in root:
        find_val(node, count + 1)


find_val(root, 1)

for value in d.values():
    print(value, end=' ')

# Second, with collections
from xml.etree import ElementTree
from collections import Counter

c = Counter()


def find_val(root, count):
    c[root.attrib['color']] += count
    for node in root:
        find_val(node, count + 1)


find_val(ElementTree.fromstring(input()), 1)

print(c['red'], c['green'], c['blue'])
