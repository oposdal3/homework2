"""
https://drive.google.com/file/d/1EmX43UNMNUofj4KMhxKnLgbQpWHJqreJ/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

a = int(input("Введите любое натуральное целое трёхзначное число: "))

sum_numbers = (a // 100) + ((a // 10) % 10) + (a % 10)
multiply_numbers = (a // 100) * ((a // 10) % 10) * (a % 10)

print(a // 100, a // 10 % 10, a % 10)
print(f"{sum_numbers=}")
print(f"{multiply_numbers=}")
print(-123 // 10)
