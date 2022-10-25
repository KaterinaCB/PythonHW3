#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#some_list = [2, 3, 5, 9, 3]
#summ = 0
#for i in range (1, len(some_list)):
#    if i % 2 != 0: 
#        summ += some_list[i]
#print(f'Сумма элементов стоящих на нечетных позициях: {summ}')

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#some_list1 = [2, 3, 4, 5, 6]
#some_list2 = []

#for i in range(len(some_list1)): 
#    if i < len(some_list1)/2:
#        some_list2.append(some_list1[i] * some_list1[len(some_list1) - i - 1])
#print(some_list2)

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#some_list = [1.1, 1.2, 3.1, 5, 10.01]
#min = 0
#max = 0

#for i in some_list:
#    if (i - int(i)) <= min:
#        min = i - int(i)
#    if (i - int(i)) >= max:
#        max = i - int(i)
#print(max - min)

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#numm = int(input('Введите число: '))
#line = ''

#while numm != 0:
#    line = str(numm % 2) + line
#    numm //= 2
#print(line)

# Или функция:

numm = int(input('Введите число: '))
print(bin(numm))