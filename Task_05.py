# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def fib(n):
    if n in [1, 2]:                       
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def nefib(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        n1, n2 = 1, -1
        for i in range(2, n):
            n1, n2 = n2, n1 - n2
        return n2

list_fib = [0]
v = int(input('Введите число: '))
for z in range(1, v + 1):
    list_fib.append(fib(z))
    list_fib.insert(0, nefib(z))
print(list_fib)




