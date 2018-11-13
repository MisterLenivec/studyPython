# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# Пример:
# s = "abababa"
# t = "aba"
#
# Sample Input 1:
# abababa
# aba
# Sample Output 1:
# 3

# First solution
def check(s, t, counter=0):
    for i in s:
        if (s.startswith(t)):
            counter += 1
        s = s[1:]
    print(counter)


check(input(), input())

# Second
s,t = [input() for i in range(2)]
count = 0

for i in range(len(s)):
    if s.startswith(t, i):
        count += 1

print(count)

# Third
s, t = input(), input()

print(sum(s[i:].startswith(t) for i in range(len(s))))
