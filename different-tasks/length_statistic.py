"""
На вход программе подаётся строка, содержащая слова, разделённые пробелом. Программа должна
вывести статистику длин слов в полученной строке, от меньшей длины слова к большей (см. пример).

Словом считается последовательность произвольных символов, окружённая пробелами либо границами
строки. Заметьте, что знаки препинания также относятся к слову.

Формат ввода:
Одна строка, содержащая последовательности латинских символов и знаков препинания, разделённые пробелом.

Формат вывода:
Для каждой длины слова, встречающейся в исходной строке, нужно указать количество слов с такой длиной
длина: количество
Статистика должна выводиться в порядке увеличения длины.

Sample Input:
Beautiful is better than ugly. Explicit is better than implicit.

Sample Output:
2: 2
4: 2
5: 1
6: 2
8: 1
9: 2
"""
# First solution
d = dict()

for i in (input().split()):
    if (len(i) in d):
        d[len(i)] += 1
    else:
        d[len(i)] = 1

for key, value in sorted(d.items()):
    print(str(key) + ':', value)


# Second with function
def create_d(val):
    d = dict()
    for i in (val):
        if (len(i) in d):
            d[len(i)] += 1
        else:
            d[len(i)] = 1
    for key, value in sorted(d.items()):
        print(f'{key}: {value}')


create_d(input().split())


# Third with collections module
import collections
c = collections.Counter()

for word in input().split():
    c[len(word)] += 1

for key, value in sorted(c.items()):
    print(str(key) + ':', value)


# Fourth with map and f string
val = list(map(len, input().split()))
for i in sorted(set(val)):
    print(f'{i}: {val.count(i)}')
