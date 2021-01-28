"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не
включать.
"""
from random import *

KOL = 10
A = 0
B = 1000
array = [randint(A, B) for _ in range(KOL)]
print(*array)

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

sum_ = 0

if MIN_IND < MAX_IND:
    for i in range(MIN_IND + 1, MAX_IND):
        sum_ += array[i]
else:
    for i in range(MAX_IND + 1, MIN_IND):
        sum_ += array[i]

print(f'Сумма чисел межды максимальным и минимальным элементами равен {sum_}')
