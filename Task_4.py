# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
result = open('result.txt','w+')
num = int(input("Задайте степень многочленна: "))
k = random.randint(1, num + 1)
if k == 1:
    result.write('{}*(x**{})+'.format(random.randint(0, 101),num))
else:
    while k != 0:
        if k == 1:
            result.write('{}=0'.format(random.randint(0, 101)))
        elif num == 1:   
            result.write('{}*(x)+'.format(random.randint(0, 101)))
        else:
            result.write('{}*(x**{})+'.format(random.randint(0, 101),num)) 
        num -= 1
        k -= 1

result.close()