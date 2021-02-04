"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой
— цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из
примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
"""
from collections import deque, defaultdict

dict_numbers = defaultdict(int, {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                                 '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                                 'C': 12, 'D': 13, 'E': 14, 'F': 15})
dict_symbols = defaultdict(str, {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                                 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                                 12: 'C', 13: 'D', 14: 'E', 15: 'F'})
print('Буквы пожалуйста вводите заглавные.')
a = deque(input('Введите 1 число: '))
b = deque(input('Введите 2 число: '))
sum_c = deque()
print(dict_numbers[b[2]])

car = 0
len_max_num = max(len(a), len(b))
for i in range(len_max_num):
    if len(a) - (i + 1) < 0:
        sum_ = dict_numbers[b[len(b) - (i + 1)]] + car
    elif len(b) - (i + 1) < 0:
        sum_ = dict_numbers[a[len(a) - (i + 1)]] + car
    else:
        sum_ = dict_numbers[a[len(a) - (i + 1)]] + dict_numbers[b[len(b) - (i + 1)]] + car
    if sum_ > 15:
        sum_ -= 16
        car = 1
        sum_c.appendleft(dict_symbols[sum_])
    else:
        car = 0
        sum_c.appendleft(dict_symbols[sum_])
print('Сумма этих чисел: ', end='')
print(*sum_c, sep='')
