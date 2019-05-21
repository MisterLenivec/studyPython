#!/usr/bin/env python3
"""
Последовательность n>0 целых чисел называется jolly jumper в случае, если значения абсолютных
разностей последовательных элементов принимают все возможные значения между 1 и n−1.

Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, так как
абсолютные разности равны 4 1 3 2, соответственно, а n−1=4.

Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.

Формат ввода:
Строка, содержащая 1≤n≤10000 целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly
jumper и "Not jolly" в противном случае.

Sample Input 1:
1 -3 -4 -1 1

Sample Output 1:
Jolly

Sample Input 2:
1 3 5

Sample Output 2:
Not jolly

Sample Input 3:
4

Sample Output 3:
Jolly
"""

# First solution


def jolly(a):
    b = set()
    for i in range(len(a)-1):
        b.add(abs(a[i]-a[i+1]))

    if len(b) != len(a)-1 or sum(b) != (1+len(a)-1)/2*len(b):
        print("Not jolly")
    else:
        print("Jolly")


jolly(list(map(int, input().split())))

# Second

# def jolly(vals):
#     val_diff = []
#     for i in range(len(vals)-1):
#         val_diff.append(abs(vals[i]-vals[i+1]))

#     if sorted(val_diff) == [i for i in range(1, len(vals))]:
#         print("Jolly")
#     else:
#         print("Not jolly")


# jolly([int(i) for i in input().split()])


# Third

# a = [int(i) for i in input().split()]
# print('Jolly' if sorted([abs(a[i]-a[i+1]) for i in range(len(a)-1)]) == [i for i in range(1, len(a))] else 'Not jolly')
