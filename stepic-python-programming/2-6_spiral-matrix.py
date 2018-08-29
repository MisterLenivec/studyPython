# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и
# закрученной по часовой стрелке, как показано в примере (здесь n=5):

# First solution
d = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
n = int(input())
x, y = 0, 0
s = []
a = []
turn = 0
counter = 1
c = 0
slicer = 1

for i in range(1, n * n + 1):
    a.append(i)
    if (len(a) == n):
        s.append(a)
        a = []

while ((counter <= n * n) and (n > 1)):
    for i in range(0, n - slicer):
        if (counter == 1):
            s[x][y] = counter
            counter += 1
        x += d[turn % 4][0]
        y += d[turn % 4][1]
        s[x][y] = counter
        counter += 1
    turn += 1
    if ((c % 2 == 0) and (c > 1)):
        slicer += 1
    c += 1

for i in range(0, n):
    print(*s[i])