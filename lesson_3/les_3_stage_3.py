"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import *

KOL = 10
A = 0
B = 1000
array = [randint(A, B) for _ in range(KOL)]
print(f'До {array}')

MAX_NUM = A
MAX_IND = 0
MIN_NUM = B
MIN_IND = 1

for i in range(KOL):
    if array[i] > MAX_NUM:
        MAX_NUM = array[i]
        MAX_IND = i
    if array[i] < MIN_NUM:
        MIN_NUM = array[i]
        MIN_IND = i

array[MAX_IND], array[MIN_IND] = array[MIN_IND], array[MAX_IND]

print(f'После {array}')
