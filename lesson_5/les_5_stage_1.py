"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за
4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю
прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья
прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict

collect = defaultdict(int)
n = int(input(f'Введите количество предприятий: '))
avg = 0

for _ in range(n):
    sum_ = 0
    name = input(f'Введите наименование {_ + 1} предприятия: ')
    for i in range(4):
        a = int(input(f'Введите прибыль за {i + 1} квартал: '))
        sum_ += a
    avg += sum_
    collect[name] = sum_

avg = avg / n
print(f'Средняя прибыль предприятий {avg}')
high_coastal = []
low_coastal = []
for place in collect:
    if collect[place] > avg:
        high_coastal.append(place)
    elif collect[place] < avg:
        low_coastal.append(place)

print('Предприятия с большой приболью', end=' ')
print(*high_coastal, sep=', ')
print('Предприятия с низкой приболью', end=' ')
print(*low_coastal, sep=', ')
