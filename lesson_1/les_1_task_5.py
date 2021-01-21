"""
https://drive.google.com/file/d/1EmX43UNMNUofj4KMhxKnLgbQpWHJqreJ/view?usp=sharing
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
print("Введите две разные буквы которые нужно определить.")
a = ord(input())
b = ord(input())

if a > b:
    c = a - b - 1
else:
    c = b - a - 1

print(f'{a=}')
print(f'{b=}')
print(f'{c=}')
