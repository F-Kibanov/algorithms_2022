"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

companies = {                                               # O(N)
    'company_1': 9000,
    'company_2': 5000,
    'company_3': 1000,
    'company_4': 3000,
    'company_5': 8000,
    'company_6': 900
}


def get_value(el):                                          # O(1)
    return el[1]                                            # O(1)


def sort_companies_1():                                     # O(N)
    max_three_1 = {}                                        # O(1)
    i = 0                                                   # O(1)
    for key, value in sorted(
            companies.items(),
            key=get_value,
            reverse=True
    ):                                                      # O(N + N*logN)
        if i < 3:                                           # O(1)
            max_three_1.setdefault(key, value)              # O(1)
        i += 1                                              # O(1)

    return max_three_1                                      # O(1)


def sort_companies_2():                                     # O(N**2)
    key_max_value = 0                                       # O(1)
    max_three_2 = {}                                        # O(1)
    while len(max_three_2) < 3:                             # O(N)
        max_value = 0                                       # O(1)
        for key, value in companies.items():                # O(N)
            if max_value < value:                           # O(1)
                max_value = value                           # O(1)
                key_max_value = key                         # O(1)
        max_value = companies.pop(key_max_value)            # O(1)
        max_three_2.setdefault(key_max_value, max_value)    # O(1)

    return max_three_2                                      # O(1)


"""
Первый алгоритм работает быстрее, так как самая ресурсоемкая задача 
в нем - это перебор значений словаря в цикле  for со сложностью O(N);
тогда как во втором алгоритме имеются два вложенных цикла, дающие
итоговую сложность O(N**2)
"""


if __name__ == '__main__':
    print(sort_companies_1())
    print(sort_companies_2())
