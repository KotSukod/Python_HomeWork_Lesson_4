#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).
def text_to_list (text):
    ls = list()
    help = ''
    for i in text:
        if i == '+' or i == '=':
            ls.append(help)
            help = ''
        else:     
            help = help + i
    return ls

def f (x):
    ls = list()
    for i in x:
        ls.append(i)
    b = '*' in ls
    if b == False:
        return 0  
    for i in ls:
        if i == '*':    
            return ls[len(ls) - 2] 

def num (x):
    help = ''
    for i in x:
        if i == '*':
            return int(help) 
        help = help + i


file1 = open('result.txt')
file2 = open('result1.txt')
result_file = open('result_file.txt','w+')
file1_ls = text_to_list(file1.read())
file2_ls = text_to_list(file2.read())

print('первый многочлен: {}'.format(file1_ls))
print('второй многочлен: {}'.format(file2_ls))

i = 0

while i < len(file1_ls):
    if f(file1_ls[i]) == 0:
        result_file.write(file1_ls[i])
        i += 1
        continue
    k = 0
    count = 0
    while k < len(file2_ls):
        if f(file1_ls[i]) == f(file2_ls[k]):
            test = num(file1_ls[i]) + num(file2_ls[k])
            result_file.write('{}*(x**{})+'.format(test,f(file1_ls[i])))
            count = 1
        k += 1
    if count == 0:
        result_file.write('{}*(x**{})+'.format(num(file1_ls[i]),f(file1_ls[i])))
    i += 1

result_file.write(' = 0')

            
            



