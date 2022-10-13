"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueBoard:
    def __init__(self):
        self.base = []
        self.solved = []
        self.review = []

    def is_empty(self):
        return self.base == []

    def to_queue(self, task):
        self.base.insert(0, task)

    def from_queue(self):
        return self.base.pop()

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def to_review(self):
        self.review.insert(0, self.base.pop())

    def reviewed(self):
        self.base.insert(0, self.review.pop())

    def tasks_quantity(self):
        return len(self.base)


if __name__ == '__main__':
    queue_task = QueueBoard()

    queue_task.to_queue('my_task')
    queue_task.to_queue(4)
    queue_task.to_queue(True)

    print(queue_task.base)
    queue_task.to_solved()
    print(queue_task.solved)
    queue_task.to_review()
    print(queue_task.base)
    print(queue_task.to_review())
    queue_task.reviewed()
    print(queue_task.review)
    print(queue_task.base)

