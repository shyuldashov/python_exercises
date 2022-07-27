# Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы
# проучила и просит вас помочь ей определить, какие числа мог задумать Август.


# Формат ввода
# Первая строка входных данных содержит число n - наибольшее число, которое мог загадать Август.
# Далее идут строки, содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных
# пробелами. После каждой строки с вопросом идет ответ Августа: YES или NO. Наконец, последняя строка входных данных
# содержит одно слово HELP.

# Формат вывода
# Вы должны вывести (через пробел, в порядке возрастанию) все числа, которые мог задумать Август.


from random import randint

# наибольшее число, которое мог бы загадать игрок
n = int(input())
# загаданное число
# guess = randint(1, n + 1)
guess = 5

yes_nums = set()  # множество, в котором есть загаданное число
no_nums = set()  # множество, в котором нет загаданного числа

for _ in range(0, n + 1):
    # получить вопросы(числа через пробел), преобразовать в число
    input_data = input()

    # если была введена help, выводятся числа, которые игрок мог бы задумать
    if input_data.lower() == 'help':
        res = yes_nums - no_nums  # res = yes_nums.difference(no_nums)
        print(*res)
        break  # завершение программы

    # полученные числа преобразуются в числовой тип и добавляются к множеству
    num_question = {int(i) for i in input_data.split()}

    # если число находится в полученным списке чисел, то обновляет yes_nums, и пропускает итерацию
    if guess in num_question:
        yes_nums = yes_nums | num_question  # yes_nums = yes_nums.union(num_question)
        print('YES')
        continue

    # если дошли до сюда, значит в списке не было загаданное числое, обновляем no_nums
    print('NO')
    no_nums = no_nums | num_question  # no_nums = no_nums.union(num_question)