# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# print ("Введите числа: ")
# my_list = [int(input()) for _ in range(int(input()))]
# result = 0
# for i in range(1, len(my_list), 2):
#     result += my_list[i]
#     print(f"Ответ: {result}")

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my_list = [2,3,4,5,6]
# def produckOfNumbers(list_0):
#     productOfNumbers = []
#     for i in range((len(list_0)+1)//2):
#         productOfNumbers.append(list_0[i]*list_0[len(list_0)-1-i])
#     return productOfNumbers
# print(produckOfNumbers(my_list))

# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5.1, 10.01]
# def dif(list_0):
#     MaxMin = []
#     for i in range (len( list_0 )):
#         MaxMin.append (list_0[i] % 1)
#     return max (MaxMin) - min (MaxMin)
# print(my_list, ' -> ', round(dif(my_list),2))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input("Введите число: "))
# my_str = ""
# while number > 0:
#     my_str = str(number % 2) + my_str
#     number = number//2
# print(my_str)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите число k: '))
my_list = [0]*(k*2+1)
my_list[k] = 0
my_list[k+1] = 1
for i in range(k+2, len(my_list)):
    my_list[i] = my_list[i-2] + my_list[i-1]

for i in range(k, -1, -1):
    my_list[i] = my_list[i+2] - my_list[i+1]
print(my_list)