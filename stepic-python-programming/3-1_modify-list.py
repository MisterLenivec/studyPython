# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка.
# First solution
def modify_list(l):
    d = len(l)
    for i in range(0, len(l)):
        if (l[i] % 2 == 0):
            l.append(l[i] // 2)
    for j in range(d):
        l.remove(l[0])
    print(l)


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)


# Second
def modify_list(l):
    for i in (l[:]):
        if (i % 2 == 0):
            l.append(i // 2)
        l.remove(i)
    print(l)


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)


# Подсмотрел :)
def modify_list(l):
    l[:] = [i // 2 for i in l if not i % 2]
    print(l)


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
