"""
https://drive.google.com/file/d/1wnh_moaFKuLB2NMUeems7u-7JxvKv4x1/view?usp=sharing
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def calculate(m):
    if m - 1 == 0:
        return 1
    else:
        return (1 / ((-2) ** (m - 1))) + calculate(m - 1)


n = int(input("Введите количество элементов: "))

z = calculate(n)

print(f'{z=}')
