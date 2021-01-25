"""
https://drive.google.com/file/d/1wnh_moaFKuLB2NMUeems7u-7JxvKv4x1/view?usp=sharing
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, надо вывести 6843.
"""


def back(m):
    if len(str(m)) == 1:
        return m
    else:
        return int(f'{m % 10}{back(m // 10)}')


a = int(input("Введите число, которое нужно перевернуть: "))
z = back(a)
print(f'{z=}')
