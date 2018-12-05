# Поле для игры сапёр представляет собой сетку размером n×m. В ячейке сетки может находиться или отсутствовать мина.
# Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной,
# указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)
# Формат ввода:
# На первой строке указываются два натуральных числа 1≤n,m≤100, после чего в n строках содержится описание поля
# в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.
# Формат вывода:
# n строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"),
# при этом число означает количество мин в соседних ячейках поля.
# Sample Input:
# 4 4
# ..*.
# **..
# ..*.
# ....
# Sample Output:
# 23*1
# **32
# 23*1
# 0111

val = input().split()
x = [list(input().replace('.', '0').replace('*', '1')) for i in range(int(val[0]))]


def getCell(i, j):
    if (i > -1 and i < len(x) and j > -1 and j < len(x[0])):
        return int(x[i][j])
    else:
        return 0


for i in range(len(x)):
    if (i != 0):
        print()
    for j in range(len(x[i])):
        if (x[i][j] != '1'):
            sum = 0
            sum += getCell(i - 1, j)
            sum += getCell(i + 1, j)
            sum += getCell(i, j - 1)
            sum += getCell(i, j + 1)
            sum += getCell(i - 1, j - 1)
            sum += getCell(i + 1, j - 1)
            sum += getCell(i + 1, j + 1)
            sum += getCell(i - 1, j + 1)
            print(sum, end='')
        else:
            print('*', end='')
# print()
