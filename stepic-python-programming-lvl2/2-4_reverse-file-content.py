# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
# Пример входного файла:
# ab
# c
# dde
# ff
# ﻿Пример выходного файла:
# ff
# dde
# c
# ab

with open('test.txt') as f, open("test_reverse", "w") as w:
    lst = [line.strip() for line in f]
    lst.reverse()
    content = "\n".join(lst)
    w.write(content)
    lst.clear()
