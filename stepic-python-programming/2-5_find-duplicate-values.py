#Напишите программу, которая принимает на вход список чисел в одной строке и
#выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
#Для решения задачи может пригодиться метод sort списка.
#Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

#First
a = [int(i) for i in input().split()]
x = []
for i in range(len(a)-1):
  if(a.count(a[i]) > 1):
    if a[i] not in x:
      x.append(a[i])
      print(a[i], end = ' ')

#Second
a = [int(i) for i in input().split()]
a.sort()
bol = False
for i in range(len(a)-1):
  if((a[i] == a[i+1]) and (bol == False)):
    print(a[i], end = ' ')
    bol = True
  elif(a[i] != a[i+1]):
    bol = False