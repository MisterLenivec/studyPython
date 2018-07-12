#Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
#пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.

#First
flag = True
ceeper = []
sum = 0
while (flag):
  a = int(input())
  sum += a
  ceeper.append(a*a)
  if (sum == 0):
    flag = False
if(flag == False):
  for i in range(len(ceeper)):
    sum += ceeper[i]
print(sum)

#Second
sum = 0
interrupt = 1
square = 0
while (interrupt != 0):
  a = int(input())
  sum += a
  square += a*a
  interrupt = sum
print(square)

#Third Решение не моё, но очень понравилось
s = [0, 0, 1]
while s[2]:
    i = int(input())
    s = [s[0] + i, s[1] + i ** 2, s[0] + i]
print(s[1])