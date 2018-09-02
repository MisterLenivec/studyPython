# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую
# самое маленькое целое число y, такое что:
#   y больше или равно x
#   y делится нацело на 5
# First solution
def closest_mod_5(x):
    y = x
    while (y % 5 != 0):
        y += 1
    return y

print(closest_mod_5(int(input())))

# Second
def closest_mod_5(x):
    return x + 5 - x % 5    # (x + 4) // 5 * 5

print(closest_mod_5(int(input())))

# Third, recursion
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return closest_mod_5(x + 1)

print(closest_mod_5(int(input())))