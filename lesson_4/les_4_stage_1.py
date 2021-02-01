"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы
 проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
 Была взята задача из 2 урока 8 задания, где нужно было посчитеть сколько раз
 встречалась в числе опппределённая цифра
"""
import timeit
import cProfile


def kol_numbers1(m, n):             # №1 Способ с рекурсией
    if len(str(m)) == 1:
        if m == n:
            return 1
        else:
            return 0
    else:
        if m % 10 == n:
            return 1 + kol_numbers1(m // 10, n)
        else:
            return 0 + kol_numbers1(m // 10, n)


def kol_numbers2(m, n):             # №2 Способ с циклом с исчезающим числом
    kol = 0
    for i in range(len(str(m))):
        if m % 10 == n:
            kol += 1
        m = m // 10
    # print(f'{kol=}')


def kol_numbers3(m, n):             # №3 Способ с использованием методов Python
    m = [_ for _ in str(m)]
    x = m.count(str(n))
    # print(f'{x=}')


print(timeit.timeit('kol_numbers1(5556555, 6)', number=100, globals=globals()))
# 0.0002904999999999991
print(timeit.timeit('kol_numbers1(5556666555, 6)', number=100, globals=globals()))
# 0.000399500000000004
print(timeit.timeit('kol_numbers1(5556666666666666666555, 6)', number=100, globals=globals()))
# 0.0009619999999999976
print(timeit.timeit('kol_numbers1(55566666666666666666666666666666666555, 6)', number=100, globals=globals()))
# 0.0018180000000000002

cProfile.run('kol_numbers1(5556555, 6)')
# 17 function calls (11 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       7/1    0.000    0.000    0.000    0.000 les_4_stage_1.py:18(kol_numbers1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers1(5556666555, 6)')
# 23 function calls (14 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 les_4_stage_1.py:18(kol_numbers1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers1(5556666666666666666555, 6)')
# 47 function calls (26 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      22/1    0.000    0.000    0.000    0.000 les_4_stage_1.py:18(kol_numbers1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        22    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers1(55566666666666666666666666666666666555, 6)')
# 79 function calls (42 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      38/1    0.000    0.000    0.000    0.000 les_4_stage_1.py:18(kol_numbers1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        38    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('kol_numbers2(5556555, 6)', number=100, globals=globals()))
# 0.00012070000000000136
print(timeit.timeit('kol_numbers2(5556666555, 6)', number=100, globals=globals()))
# 0.00015699999999999742
print(timeit.timeit('kol_numbers2(5556666666666666666555, 6)', number=100, globals=globals()))
# 00.0003398000000000012
print(timeit.timeit('kol_numbers2(55566666666666666666666666666666666555, 6)', number=100, globals=globals()))
# 0.0005888000000000004

cProfile.run('kol_numbers2(5556555, 6)')
# 5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:31(kol_numbers2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers2(5556666555, 6)')
# 5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:31(kol_numbers2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers2(5556666666666666666555, 6)')
# 5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:31(kol_numbers2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers2(55566666666666666666666666666666666555, 6)')
# 5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:31(kol_numbers2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('kol_numbers3(5556555, 6)', number=100, globals=globals()))
# 0.00011029999999999374
print(timeit.timeit('kol_numbers3(5556666555, 6)', number=100, globals=globals()))
# 0.00012270000000000336
print(timeit.timeit('kol_numbers3(5556666666666666666555, 6)', number=100, globals=globals()))
# 0.00017550000000000204
print(timeit.timeit('kol_numbers3(55566666666666666666666666666666666555, 6)', number=100, globals=globals()))
# 0.0002593999999999999

cProfile.run('kol_numbers3(5556555, 6)')
# 6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:40(kol_numbers3)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers3(5556666555, 6)')
# 6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:40(kol_numbers3)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers3(5556666666666666666555, 6)')
# 6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:40(kol_numbers3)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('kol_numbers3(55566666666666666666666666666666666555, 6)')
# 6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:40(kol_numbers3)
#         1    0.000    0.000    0.000    0.000 les_4_stage_1.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Все 3 варианта имеют O(1) константную сложность, но я предпочитаю 3 вариант, так как
он имеет читаемый код.
"""
