# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
# на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.

# Sample Input:
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
# Sample Output:
# Зенит:2 2 0 0 6
# ЦСКА:2 0 1 1 1
# Спартак:2 0 1 1 1

numberOfGames = int(input())
d = dict()
matchResult = []
def update_teams(d, team):
    if (team not in d):
        d[team] = [0, 0, 0, 0, 0]

def update_score(d, result):
    if(result[1] > result[3]):
        d[result[0]][0] += 1
        d[result[0]][1] += 1
        d[result[0]][4] += 3
        d[result[2]][0] += 1
        d[result[2]][3] += 1
    elif (result[1] == result[3]):
        d[result[0]][0] += 1
        d[result[0]][2] += 1
        d[result[0]][4] += 1
        d[result[2]][0] += 1
        d[result[2]][2] += 1
        d[result[2]][4] += 1
    else:
        d[result[2]][0] += 1
        d[result[2]][1] += 1
        d[result[2]][4] += 3
        d[result[0]][0] += 1
        d[result[0]][3] += 1

for i in range(numberOfGames):
    matchResult.append(input().split(';'))
    update_teams(d, matchResult[i][0])
    update_teams(d, matchResult[i][2])
    update_score(d, matchResult[i])

for key, values in d.items():
    print(key + ': ', values[0], values[1], values[2], values[3], values[4], end='')
    print()
