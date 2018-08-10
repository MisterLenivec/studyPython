# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
# одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
# после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
# которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac

# First solution
str1, str2, encrypt, decrypt = list(input()), list(input()), list(input()), list(input())
# str1 = ['a', 'b', 'c', 'd']
# str2 = ['*', 'd', '%', '#']
# encrypt = ['a', 'b', 'a', 'c', 'a', 'b', 'a' ,'d', 'a', 'b', 'a']
# decrypt = ['#', '*', '%', '*', 'd', '*', '%']

d = dict (zip (str1, str2))
d2 = dict (zip (str2, str1))

def encr(enc):
    print(d[enc], end='')

def decr(dec):
    print(d2[dec], end='')

for i in range(len(encrypt)):
    encr(encrypt[i])
print()
for i in range(len(decrypt)):
    decr(decrypt[i])

# Second
str1, str2, encrypt, decrypt = list(input()), list(input()), list(input()), list(input())
for i in encrypt:
    print(str2[str1.index(i)], end='')

print()

for j in decrypt:
    print(str1[str2.index(j)], end='')

#Third
str1, str2 = input(), input()
print(''.join([str2[str1.index(i)] for i in input()]), ''.join([str1[str2.index(i)] for i in input()]), sep='\n')