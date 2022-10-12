"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


def set_quantity(n=3):
    quantity_per_stack = n
    return quantity_per_stack


class Plates:
    def __init__(self):
        self.plates_stack = []

    def show_stacks(self):
        return self.plates_stack

    def check_stacks(self):
        if len(self.plates_stack[-1]) == set_quantity():
            self.plates_stack.append(list())

    def add_plate(self, n: int):
        while n:
            if self.plates_stack:
                self.plates_stack[-1].append(0)
            else:
                self.plates_stack = [[0]]
            n -= 1
            self.check_stacks()
        return self.plates_stack


s = Plates
print(s.add_plate(Plates(), n=3))       # [[0, 0, 0], []]
print(s.add_plate(Plates(), n=4))       # [[0, 0, 0], [0]]
