"""
https://drive.google.com/file/d/1EmX43UNMNUofj4KMhxKnLgbQpWHJqreJ/view?usp=sharing
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
year = int(input("Введите год, который нужно проверить."))

if year % 4 == 0:
    if year % 100 != 0:
        print(f'Год {year} високосный.')
    elif year % 400 == 0:
        print(f'Год {year} високосный.')
    else:
        print(f'Год {year} не високосный.')
else:
    print(f'Год {year} не високосный.')
