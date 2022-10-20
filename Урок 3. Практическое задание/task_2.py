"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import hashlib

"""
Функция запрашивает ввод логина (в качестве "соли") и пароля,
записывает введенный пароль в файл user_passwords.csv, после
запрашивает пароль еще раз и сравниват с записанным в файле.
Если пароли совпали - выводится его хеш, если не совпали - 
выводится хеш обоих паролей с сообщением о неправильном вводе.
"""


def get_login():
    log = input('Введите логин: ')
    return log


def get_password():
    pwd = input('Введите пароль: ')
    return pwd


def get_pwd_hash(log, pwd):
    hash_pwd = hashlib.sha256((log + pwd).encode('utf-8')).hexdigest()
    return hash_pwd


def write_pass(hash_pwd):
    with open('user_passwords.csv', 'a', encoding='utf-8') as pw:
        pw.write(hash_pwd + "\n")


def check_user(hash_pwd):
    with open('user_passwords.csv', 'r', encoding='utf-8') as pw:
        for line in pw:
            pass
        first_pass = line
    if first_pass.strip() == hash_pwd.strip():
        return f'Вы ввели правильный пароль! Его хеш: {first_pass}'
    else:
        return f'Вы ввели НЕправильный пароль! Его хеш: {first_pass} а вы ввели {hash_pwd}'


if __name__ == '__main__':
    log = get_login()
    hash_pwd_1 = get_pwd_hash(log, get_password())
    write_pass(hash_pwd_1)
    print('*' * 50)
    print('Введите пароль еще раз для проверки')
    hash_pwd_2 = get_pwd_hash(log, get_password())
    print(check_user(hash_pwd_2))
