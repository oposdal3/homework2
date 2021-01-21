"""
https://drive.google.com/file/d/1EmX43UNMNUofj4KMhxKnLgbQpWHJqreJ/view?usp=sharing
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
letter = int(input("Введите номер буквы."))
if 97 <= (letter + 96) <= 122:
    letter = chr(letter + 96)
    print(f'a={letter}')
else:
    print("Вы ввели запредельное число он не принемается")
