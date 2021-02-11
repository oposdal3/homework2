"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы, в
другой — не больше медианы.
"""
import random

# Я ни как не мог догадаться как это сделать по этому узнал новый метод
# сортировки пирамидай. Код не копировал а печатал сам, хоть и с огляткой на сайт
# (https://senior.ua/articles/8-metodov-sortirovok-python-kotorye-obyazatelno-nuzhno-znat)


def heap(array, heap_size, root_index):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child

    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heap(array, heap_size, largest)


def sort_array(array):
    long = len(array)

    for i in range(long, -1, -1):
        heap(array, long, i)
    for i in range(long - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap(array, i, 0)


m = random.randint(1, 9)
n = 2 * m + 1
# list_ = [5, 7, 3, 1, 8, 4, 9, 2, 6]
list_ = [random.randint(0, n) for _ in range(n)]
print(list_)
sort_array(list_)
print(list_)
print(f'Мидеаной является число {list_[m]}')

