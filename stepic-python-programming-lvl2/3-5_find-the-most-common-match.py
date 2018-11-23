# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года
# по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
# Дается файл с данными.

import csv
import re
from collections import Counter

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    c = Counter()
    for row in reader:
        if (re.findall(r'(2015)', row[2])):
            c[row[5]] += 1
    print(c.most_common(1)[0][0])
