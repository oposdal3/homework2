"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран
исходный и отсортированный массивы.
"""
import random

# Сайт где вычитал про слияние, но не понял пример огромного кода.
# В итоге написал сам.
# (http://aliev.me/runestone/SortSearch/TheMergeSort.html)


def sort_array(array):
    n = len(array)

    if n < 2:
        return array

    left_array = sort_array(array[:n // 2])
    right_array = sort_array(array[n // 2:])

    i = 0
    j = 0
    reserve = []

    while i < len(left_array) or j < len(right_array):
        if not i < len(left_array):
            reserve.append(right_array[j])
            j += 1
        elif not j < len(right_array):
            reserve.append(left_array[i])
            i += 1
        elif left_array[i] < right_array[j]:
            reserve.append(left_array[i])
            i += 1
        else:
            reserve.append(right_array[j])
            j += 1
    return reserve


# list_ = [random.uniform(0, 50) for _ in range(5)]
list_ = [random.uniform(0, 50) for _ in range(500)]
print(list_)
print(sort_array(list_))
