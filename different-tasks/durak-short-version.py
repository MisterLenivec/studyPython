# A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades
# (denoted C, D, H, S). Each card also has a value of either 6 through 10, jack, queen, king, or ace
# (denoted 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes card values are ordered as above, with 6
# having the lowest and ace the highest value.
# Напишите программу, которая определяет, бьёт ли одна карта другую.
# Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
# Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
# Если карты разных мастей и нет козырных, то никто не побеждает.
# Формат ввода:
# На первой строке через пробел указываются две карты в формате <значение><масть>,
# а на следующей строке указывается козырная масть.
# Формат вывода:
# Программа должна вывести слово
# First, если первая карта бьёт вторую,
# Second, если вторая карта бьёт первую,
# Error, если ни одна из карт не может побить другую.
# Sample Input 1:
# AH JH
# D
# Sample Output 1:
# First
# Sample Input 2:
# AH JS
# S
# Sample Output 2:
# Second
# Sample Input 3:
# 7C 10H
# S
# Sample Output 3:
# Error

d = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
     'J': 11, 'Q': 12, 'K': 13, 'A': 14,
     'C': 0, 'D': 0, 'H': 0, 'S': 0}

f, s = input().split()
d[input()] = 15

if (((d[f[:-1]] + d[f[-1:]]) == (d[s[:-1]] + d[s[-1:]])) or
    ((d[f[:-1]] + d[f[-1:]]) != (d[s[:-1]] + d[s[-1:]]) and ((f[-1:] != s[-1:]) and ((d[f[-1:]] or d[s[-1:]]) != 15)))):
    print('Error')
elif ((d[f[:-1]] + d[f[-1:]]) > (d[s[:-1]] + d[s[-1:]])):
    print('First')
else:
    print('Second')
