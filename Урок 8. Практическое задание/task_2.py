"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # проверка на размер, если элемент для вставки влево больше
        # корня - то вызвать ошибку
        if new_node > BinaryTree.get_root_val(self):
            raise ValueError("left child is bigger than root!")
        # если проверка на размер прошла успешно и у узла нет левого потомка,
        # узел просто вставляется в дерево и формируется новое поддерево
        elif self.left_child is None:
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок и проверка на размер пройдена
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # проверка на размер, если элемент для вставки вправо меньше
        # корня - то вызвать ошибку
        if new_node < BinaryTree.get_root_val(self):
            raise ValueError("right child is less than root!")
        # если проверка на размер прошла успешно и у узла нет правого потомка,
        # узел просто вставляется в дерево и формируется новое поддерево
        elif self.right_child is None:
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок и проверка на размер пройдена
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


if __name__ == '__main__':
    r = BinaryTree(8)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(4)
    # assert r.insert_left(40) == ValueError("left child is bigger than root!")
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right(12)
    # assert r.insert_right(1) == ValueError("right child is less than root!")
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(16)
    print(r.get_right_child().get_root_val())


"""
Добавил проверку входных данных для вставки значений в левую и правую ветви:
    если выполняется вставка значения в левую ветвь и значение больше корня,
    то выбрасывается исключение ValueError("left child is bigger than root!");
    если выполняется вставка значения в правую ветвь и значение меньше корня,
    то выбрасывается исключение ValueError("right child is less than root!").
"""
