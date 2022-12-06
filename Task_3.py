# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def f (k,ls):
    i = 0
    while i < len(ls):
        if k == i:
            i += 1
            continue
        if ls[k] == ls[i]:
            i == len(ls)
            return 0
        i += 1    
    return 1        

number =  [1, 1, 2, 3, 4, 5, 4]

i = 0
result = list()
while i < len(number):
    help = f(i,number)
    if help == 1:
        result.append(number[i])
    i += 1
print(result)    
    