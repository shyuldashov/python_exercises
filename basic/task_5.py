# На вход функции с именем get_sort поступает словарь, например, такой:
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# Необходимо отсортировать словарь d по убыванию ключей (лексикографическая сортировка строк) и возвратить список
# из соответствующих значений ключей словаря. Например, для указанного словаря d, результатом должен быть список:
# ['дерево', 'лошадь', 'собака', 'кот', 'книга']
# Вызовите функцию get_sort для заданного в программе произвольного словаря
# dсt и выведите возвращенный ею список на экран.

def get_sort(arg: dict) -> list:
    """
    :param arg: словарь
    :param by: критерии сортировки 0 - по ключу, 1 - по значению
    :param reverse: True - по убыванию, False - по возрастанию. По умолчанию: по возрастанию
    :return: список значений словаря
    """
    return list({key: value for key, value in sorted(arg.items(), key=lambda x: x[0], reverse=True)}.values())


if __name__ == '__main__':
    en_ru_dict = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
    body = {'head': 'голова', 'eyes': 'глаза', 'lips': 'губы', 'nose': 'нос', 'neck': 'шея'}
    print(get_sort(en_ru_dict))
    print(get_sort(body))
