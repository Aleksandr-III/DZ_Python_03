# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



from random import randint

n = int(input('Введите количество элементов: '))
x = int(input('Введите минмальное значение: '))
y = int(input('Введите максимальное значение: '))
numbers = []
for i in range(n):
    numbers.append(randint(x, y))
list2 = []
for i in range(len(numbers)):
    while i < len(numbers)/2 and n > len(numbers)/2:
        n = n - 1
        a = numbers[i] * numbers[n]
        list2.append(a)
        i += 1
print(f'В данном списке {numbers} прооизведение пар чисел списка = 1*последний 2*предпоследний и т. д. => {list2}')
