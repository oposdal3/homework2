"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import *

KOL = 1000
A = 0
B = 100
array = [randint(A, B) for _ in range(KOL)]

NUMBER = 0
MAX_KOL = 0
already_count = []
for i in range(KOL):
    if array[i] not in already_count:
        kol = 0
        for j in range(KOL):
            if array[i] == array[j]:
                kol += 1
        already_count.append(array[i])
        if kol > MAX_KOL:
            MAX_KOL = kol
            NUMBER = array[i]

if MAX_KOL == 1:
    print(f'Все числа в массиве встречаются только 1 раз')
else:
    print(f'В массиве чаще всего встречается число {NUMBER}')
