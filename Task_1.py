# Вычислить число c заданной точностью d

import math
def f (x):
    count = 0
    while x != 1:
        count = count + 1
        x = x * 10
    return count

number = float(input("Введите точность числа(формата 0.001): "))
print(round(math.pi, f(number)))