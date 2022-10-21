"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
import collections
import functools


def hex_sum_mult():
    nums = collections.defaultdict(list)

    for d in range(2):
        n = input(f'Введите {d + 1}-е натуральное шестнадцатеричное число: ')
        nums[f'{d + 1}'] = list(n)

    sum_res = sum([int(''.join(i), 16) for i in nums.values()])
    print('Сумма: ', list("%X" % sum_res))

    mul_res = functools.reduce(lambda a, b: a * b,
                               [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mul_res))


hex_sum_mult()


class HexSumMult:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16)
                        + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16)
                        * int(''.join(other.second_num), 16)))[2:]


hex_first_num = list(input('Введите первое число: '))
hex_second_num = list(input('Введите второе число: '))

res_sum = HexSumMult(hex_first_num, hex_second_num) \
          + HexSumMult(hex_first_num, hex_second_num)
res_mul = HexSumMult(hex_first_num, hex_second_num) \
          * HexSumMult(hex_first_num, hex_second_num)
print(f'Сумма чисеп = {res_sum}\nПроизведение чисел ={res_mul}')

