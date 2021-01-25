"""
https://drive.google.com/file/d/1wnh_moaFKuLB2NMUeems7u-7JxvKv4x1/view?usp=sharing
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
n = int(input("Введите количество чисел: "))
max_number = 0
max_sum = 0

for i in range(n):
    a = input(f"Введите {i + 1} число: ")
    sum_ = 0
    for el in a:
        sum_ += int(el)
    if sum_ > max_sum:
        max_sum = sum_
        max_number = int(a)

print(f'{max_number=}')
print(f'{max_sum=}')
