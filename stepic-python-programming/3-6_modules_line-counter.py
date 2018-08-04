# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и
# посчитать число строк в нём.
# В поле ответа введите одно число или отправьте файл, содержащий одно число.

import requests

with open('dataset_3378_2.txt') as inf:
    l = inf.readline().strip()

r = requests.get(l.strip())
r = r.text.splitlines()

with open('dataset_3378_2.txt', 'w') as ouf:
    ouf.write(str(len(r)))

#print(len(r))