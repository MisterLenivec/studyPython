# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

with open('dataset_3363_2.txt') as inf:
    s1 = inf.readline()
# s1 = 'R20D17h4I3F15l13D5u14l12D15S16B2M20o17j19M1U6H2T17g19X20D16d16'

d = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
numb = ''
symb = s1[0]
result = ''
for i in range(1, len(s1)):
    if (s1[i] in d):
        numb += s1[i]
    if (s1[i] not in d):
        result += symb * int(numb)
        symb = s1[i]
        numb = ''
# result = RRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDhhhhIIIFFFFFFFFFFFFFFFlllllllllllllDDDDDuuuuuuuuuuuuuullllllllllllDDDDDDDDDDDDDDDSSSSSSSSSSSSSSSSBBMMMMMMMMMMMMMMMMMMMMooooooooooooooooojjjjjjjjjjjjjjjjjjjMUUUUUUHHTTTTTTTTTTTTTTTTTgggggggggggggggggggXXXXXXXXXXXXXXXXXXXXDDDDDDDDDDDDDDDDdddddddddddddddd

with open('dataset_3363_2.txt', 'w') as ouf:
    ouf.write(str(result))
