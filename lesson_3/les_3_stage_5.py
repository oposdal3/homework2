"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение
и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и
«максимальный отрицательный». Это два абсолютно разных значения.
"""
from random import *

KOL = 1000
A = -55
B = 20
array = [randint(A, B) for _ in range(KOL)]

NUMBER = A
INDEX = -1

for i in range(KOL):
    if array[i] < 0 and NUMBER < array[i] < 0:
        NUMBER = array[i]
        INDEX = i

if NUMBER == A and INDEX == -1:
    print(f'В массиве нет отрицательных элементов.')
else:
    print(f'В массиве максимальный отрицательный элемент {NUMBER} под индексом {INDEX}')
