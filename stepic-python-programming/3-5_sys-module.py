# Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран
# (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
# Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.
# Пример работы программы:
# > python3 my_solution.py arg1 arg2
# arg1 arg2

from sys import argv

# first solution
print(*argv[1:])

# second
print(' '.join(argv[1:]))

# third
for i in range(1, len(argv)):
    print(argv[i], end=' ')

# fourth
for i in argv[1:]:
    print(i, end=' ')
