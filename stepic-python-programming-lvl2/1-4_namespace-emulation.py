# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку
# создания пространств имен и добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
# Вашей программе на вход подаются следующие запросы:
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует
# Формат входных данных:
# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.
# Формат выходных данных:
# Для каждого запроса get выведите в отдельной строке его результат.

# Recursion
d = dict()
d['global'] = {'parent': 'None'}
def creating(nmsp, var):
  d[nmsp] = {'parent': (var)}

def adding(nmsp, var):
  if (nmsp in d):
    if ('var' in d[nmsp]):
      d[nmsp]['var'] += [var]
    else:
      d[nmsp].update({'var': [var]})

def reception(nmsp, var):
  if (d[nmsp].get('parent', ()) == 'None' and var not in d[nmsp].get('var', [])):
    return d[nmsp].get('parent', ()) # С print конечно чуть быстрее
  elif (var in d[nmsp].get('var', [])):
    return nmsp
  else:
    return reception(d[nmsp].get('parent', ()), var)

def actionSelection(cmd, nmsp, var):
  if (cmd == 'create'):
    creating(nmsp, var)
  elif (cmd == 'add'):
    adding(nmsp, var)
  else:
    print(reception(nmsp, var))

for i in range(int(input())):
  cmd, nmsp, var = input().split()
  actionSelection(cmd, nmsp, var)

# Cycle
d = {'global': ['None']}
for ops, nms, var in [input().split() for i in range(int(input()))]:
  if (ops == 'create'):
    d[nms] = [var]
  elif (ops == 'add'):
    d[nms].append(var)
  else:
    while (nms != 'None' and var not in d[nms]):
      nms = d[nms][0]
    print(nms)