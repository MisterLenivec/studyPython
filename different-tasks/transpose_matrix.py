'''
Напишите программу, которая принимает на вход матрицу, выполняет её
транспонирование и выводит результат.

Формат ввода:
В первой строке указываются два целых числа n
и m, количество строк и столбцов, соответственно.
Далее следуют n строк, содержащих по m целых чисел, разделённых пробелом.

Формат вывода:
Программа должна вывести m строк содержимого транспонированной матрицы.
Элементы матрицы стоит разделять пробелом.

Sample Input 1:
2 3
1 2 3
4 5 6

Sample Output 1:
1 4
2 5
3 6

Sample Input 2:
2 2
1 2
3 4

Sample Output 2:
1 3
2 4
'''
# First solution
val = input().split()

lst = [input().split() for i in range(int(val[0]))]

for i in zip(*lst):
    print(*i)


# Second solution, with numpy
import numpy as np

val = input().split()
matrix = np.array([input().split() for i in range(int(val[0]))])

for row in matrix.transpose():
    print(*row)
