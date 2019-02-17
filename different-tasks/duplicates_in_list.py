'''
Напишите программу, которая принимает на вход список целых чисел и выводит
на экран значения, которые повторяются в нём более одного раза.

Формат ввода:
Одна строка с целыми числами, разделёнными пробелом.

Формат вывода:
Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться,
порядок вывода может быть произвольным.

Sample Input:
4 8 0 3 4 2 0 3

Sample Output:
0 3 4
'''
# First solution
lst = input().split()
res = []

for i in (lst):
    if (lst.count(i) > 1):
        if (i not in res):
            res.append(i)

print(*res)


# Second
lst = input().split()

for i in set(lst):
    if (lst.count(i) > 1):
        print(i, end = '')


# Third, generator
lst = input().split()

print(*[i for i in set(lst) if lst.count(i) > 1])


# Fourth, with collections
from collections import Counter

res = Counter(input().split())

for i in res.keys():
    if (res[i] > 1):
        print(i, end=' ')

# Fifth, generator and collections
from collections import Counter

print(*([i for i, j in Counter(input().split()).items() if j > 1]))
