"""
https://drive.google.com/file/d/1wnh_moaFKuLB2NMUeems7u-7JxvKv4x1/view?usp=sharing
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def kol_numbers(m, n):
    if len(str(m)) == 1:
        if m == n:
            return 1
        else:
            return 0
    else:
        if m % 10 == n:
            return 1 + kol_numbers(m // 10, n)
        else:
            return 0 + kol_numbers(m // 10, n)


a = int(input("Введите число: "))
b = int(input("Введите цифру, которое нужно найти в числе: "))

z = kol_numbers(a, b)

print(f'{z=}')
