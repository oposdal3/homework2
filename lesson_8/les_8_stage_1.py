"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""

# Множество set не даст нам дабавить одну и ту же строковую переменную.
# В данном случае хеш.


def hash_kol(string):
    hash_array = set()
    for i in range(len(string) - 1):
        for j in range(len(string)):
            hash_array.add(hash(string[j:j + 1 + i]))
    return len(hash_array)


print(hash_kol('papa'))
print(hash_kol('sova'))
