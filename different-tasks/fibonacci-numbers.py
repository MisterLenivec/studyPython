# Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи (напомним, что F0=0, F1=1 и Fn=Fn−1+Fn−2 при n≥2).
# Sample Input:
# 3
# Sample Output:
# 2
# Пробуем решенить без рекурсии

# First solution
# Создаем список и обращаемся к нему
def fib(n):
    fib_list = []
    for i in range(0, n):
        if (i <= 1):
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[i]

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()

# Second
# Сохраняем предыдущее и текущее число в переменных
def fib(n):
    prev, cur = 0, 1
    for i in range(1, n):
        prev, cur = cur, prev + cur
    return cur

# def main():
n = int(input())
print(fib(n))

# if __name__ == "__main__":
#     main()

# Third, it's magic formula :)
import sys
print(round(0.4472135954999579*1.618033988749895**int(input())))
