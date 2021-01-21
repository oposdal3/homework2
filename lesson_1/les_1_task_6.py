"""
https://drive.google.com/file/d/1EmX43UNMNUofj4KMhxKnLgbQpWHJqreJ/view?usp=sharing
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
letter = int(input("Введите номер буквы."))

letter = chr(letter + 96)

print(f'a={letter}')
