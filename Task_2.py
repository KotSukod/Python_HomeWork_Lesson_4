# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
count = 2
ls = list()
while number !=1:
    if number % count == 0:
        ls.append(count)
        number = number / count
        count = 1
    count += 1
print(ls)    

