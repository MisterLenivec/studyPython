# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
# Класс A является предком класса B, если
# A = B;
# A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
# i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
# Sample Input:
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A
# Sample Output:
# Yes
# Yes
# Yes
# No

# First solution
graph = {}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if (start and end in graph):
        if start == end:
            return [path]
    if (start not in graph):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpath = find_all_paths(graph, node, end, path)
            if newpath:
                return newpath
    if paths:
        return paths

def az(graph, start, end):
    x = find_all_paths(graph, start, end)
    if (x != None and x != []):
        return 'Yes'
    else:
        return 'No'

for i in range(int(input())):
    total = input()
    if (':' in total):
        el, parent = total.split(':')
        el = el.replace(' ', '')
        parent = parent.split()
        graph[el] = parent
    else:
        graph[total] = [total]
    # print(graph)

for i in range(int(input())):
    check = input().split()
    print(az(graph, check[1], check[0]))