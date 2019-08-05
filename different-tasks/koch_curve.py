#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Кривая Коха -- это простой геометрический фрактал.
Строится этот фрактал следующим образом: берётся отрезок, разделяется на три
равных части. Вместо средней части вставляется два таких же отрезка,
поставленные под углом 60 градусов друг к другу.
Этот процесс повторяется на каждой итерации: каждый отрезок заменяется четырьмя.

Напишите программу, которая принимает на вход число n − количество итераций
генерации кривой и выводит последовательность углов поворота при рисовании
соответствующей линии от начальной точки к конечной, без отрыва пера.

Способ проверки своего решения приведён на следующем степе.

Формат ввода:
Строка с целым числом n, 1≤n≤10.

Формат вывода:
Строки, содержащие последовательность поворотов. Каждый поворот указывается на
отдельной строке как слово "turn" и угол поворота в градусах. Угол поворота
должен находиться в интервале [-180; 180].

Sample Input:
1

Sample Output:
turn 60
turn -120
turn 60

"""


# First solution

# def koch(n):
#     if n == 0:
#         pass
#     elif n == 1:
#         return 'turn 60\nturn -120\nturn 60\n'
#     else:
#         return koch(n - 1) + 'turn 60\n' + koch(n - 1) + 'turn -120\n' + koch(
#             n - 1) + 'turn 60\n' + koch(n - 1)
#
#
# print(koch(int(input())))


# Second

# def koch(n):
#     if n > 0:
#         koch(n - 1)
#         print('turn 60')
#         koch(n - 1)
#         print('turn -120')
#         koch(n - 1)
#         print('turn 60')
#         koch(n - 1)
#
#
# koch(int(input()))


# Third - Turtle!

import turtle


def koch_turns(n):
    if n == 0:
        pass
    elif n == 1:
        return [60, -120, 60]
    else:
        return koch_turns(n-1) + [60] + koch_turns(n-1) + [-120] + koch_turns(
            n-1) + [60] + koch_turns(n-1)

def turtle_koch_curve(n, line_length=5):
    turtle.speed(100)
    turtle.up()
    turtle.setpos(-300, -50)
    turtle.down()
    for move in koch_turns(n):
        turtle.forward(line_length)
        turtle.left(move)
    turtle.forward(line_length)
    turtle.mainloop()


print("Введите 2 числа на отдельных строках, количество итераций генерации "
      "кривой и длинну линии")
turtle_koch_curve(int(input()), int(input()))
