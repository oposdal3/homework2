"""
https://drive.google.com/file/d/1wnh_moaFKuLB2NMUeems7u-7JxvKv4x1/view?usp=sharing
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5)
"""
a = input("Введите число, которое нужно проверить: ")
chet = "Чётные цифры - "
ne_chet = "Не чётные цифры - "
for el in a:
    if int(el) % 2 == 0:
        chet += el + " "
    else:
        ne_chet += el + " "
print(f'{chet}')
print(f'{ne_chet}')
