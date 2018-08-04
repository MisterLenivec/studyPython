# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

# First solution
import requests

link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt') as inf:
    l = inf.readline().strip()

r = requests.get(l)
r = link + r.text

flag = True
while(flag):
    r = requests.get(r)
    if (r.text.count('.txt')):
        print(r.text) # Что бы было видно что консоль не просто висит
        r = link + r.text
    else:
        flag = False
        print(r.text)

# Second
import requests

link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt') as inf:
    t = inf.readline().strip()

t = str(requests.get(t).text)
while 'we' not in t:
    print(t)
    t = requests.get(link + t).text
print(t)