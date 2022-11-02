"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, namedtuple


class Node(namedtuple("Name", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    my_list = []
    for ch, freq in Counter(s).items():
        my_list.append((freq, len(my_list), Leaf(ch)))

    count = len(my_list)
    while len(my_list) > 1:
        freq1, _count1, left = my_list.pop()
        freq2, _count2, right = my_list.pop()
        my_list.append((freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if my_list:
        [(_freq, _count, root)] = my_list
        root.walk(code, "")
    return code


def main():
    s = input('enter string to encode: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(f'uniq symbols: {len(code)}\nlen encoded string: {len(encoded)}')
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)


if __name__ == '__main__':
    main()
