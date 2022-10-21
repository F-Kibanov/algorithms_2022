"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple, defaultdict
from statistics import mean


def namedtuple_profit():
    companies_number = int(input('Введите количество предприятий: '))
    companies = namedtuple(
        'Company', 'company_name first_quart second_quart third_quart fourth_quart'
    )
    avg_profit = defaultdict(float)
    for i in range(companies_number):
        company = companies(
            company_name=input('Введите название компании: '),
            first_quart=int(input('Введите прибыль предприятия за первый квартал: ')),
            second_quart=int(input('Введите прибыль предприятия за второй квартал: ')),
            third_quart=int(input('Введите прибыль предприятия за третий квартал: ')),
            fourth_quart=int(input('Введите прибыль предприятия за четвертый квартал: ')))
        avg_profit[company.company_name] = (
            company.first_quart + company.second_quart + company.third_quart + company.first_quart
        ) / 4
    total_avg = 0
    for value in avg_profit.values():
        total_avg += value
    total_avg = total_avg / companies_number
    if companies_number == 1:
        print(f'Средняя прибыль предприятия {company.company_name} = {avg_profit[company.company_name]}')
    else:
        print(f'Средняя годовая прибыль всех компаний = {total_avg}')
        for key, value in avg_profit.items():
            if value > total_avg:
                print(f'{key} - прибыль выше среднего')
            elif value < total_avg:
                print(f'{key} - прибыль ниже среднего')
            elif value == total_avg:
                print(f'{key} - средняя прибыль')


def defaultdict_profit():
    companies_number = int(input(f'Введите количество компаний: '))
    companies = defaultdict(float)
    for i in range(companies_number):
        company = input(f'Введите название компании: ')
        quart_profit = input(f'Введите прибыль компании за 4 квартала через пробел: ')
        companies[company] = mean([int(el) for el in quart_profit.split(' ')])
    avg_profit = round((mean(companies.values())), 2)
    if companies_number == 1:
        print(f'Средняя годовая прибыль = {avg_profit}')
    else:
        print(f'Средняя годовая прибыль всех компаний = {avg_profit}')
        print(f'{", ".join([el for el in companies.keys() if companies[el] > avg_profit])} - прибыль выше среднего')
        print(f'{", ".join([el for el in companies.keys() if companies[el] < avg_profit])} - прибыль ниже среднего')


if __name__ == '__main__':
    namedtuple_profit()
    defaultdict_profit()
