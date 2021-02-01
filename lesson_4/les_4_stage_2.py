"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""


def sieve(n):
    number = 0
    step = 50
    while True:
        list_numbers = [_ for _ in range(2, step + 1)]
        for el in list_numbers:
            division_number = 1
            for i in range(1, el):
                if el % i == 0:
                    division_number += 1
            if division_number != 2:
                list_numbers[list_numbers.index(el)] = 0
        cope_n = n
        for i in range(len(list_numbers)):
            if list_numbers[i] != 0:
                cope_n -= 1
            if cope_n == 0:
                number = list_numbers[i]
                break
        if number != 0 and cope_n == 0:
            break
        else:
            step += 50
    return number


def prime(n):
    number = 0
    step = 1
    while n > 0:
        division_number = 1
        step += 1
        for i in range(1, step):
            if step % i == 0:
                division_number += 1
        if division_number == 2:
            number = step
            n -= 1
    return number


print(f'{sieve(2)=}')
print(f'{prime(4)=}')
print(f'{sieve(5)=}')
print(f'{prime(1)=}')
