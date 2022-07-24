"""Результат сессии, состоящей из 3 экзаменов (История, Математика, Информатика), для студента задается в виде списка,
содержащего фамилию студента и 3 оценки по пятибальной системе
0 - неявка,
2 - неудоблетворительно
3 - удовлетворительно
4 - хорошо
5 - отлично
Результаты группы сохраняются в виде словаря. Для группы выведите на экран
a) таблицу с результатами экзаменов;
b) средний балл по каждой дисциплин;
с) средний балл для каждого студента.
"""


def exam_results_table(students: dict, avg_disciplines: dict, avg_students: dict):
    """
    Функция нарисует таблицу с резултатами экзаменов, средний балл по каждой дисциплины и
    средний балл для каждого студента
    :param students:
    :param avg_disciplines:
    :param avg_students:
    :return:
    """
    print(f"Фамилия\t\t\t\tИстория\tМатематика\tИнформатика")
    for student, grades in students.items():
        print(f"{student:<16}{grades[0]:>8}{grades[1]:>9}{grades[2]:>13}")

    print()
    print("Средний балл по каждой дисциплине".center(51, '='))
    for discipline, grade in avg_disciplines.items():
        print(f"{discipline:<16}{grade:^9.2f}")

    print()
    print("Средний балл для каждого студента".center(51, '='))
    print(f"Фамилия\t\t\tСредний балл")
    for student, avg_grade in avg_students.items():
        print(f"{student:<16}{avg_grade:>8.1f}")


def avg_for_each_discipline(students):
    disciplines = {'История': 0, "Математика": 0, "Информатика": 0}

    # сумма оценок по каждому предмету
    for _, grades in students.items():
        disciplines['История'] += grades[0]
        disciplines['Математика'] += grades[1]
        disciplines['Информатика'] += grades[2]

    # средний балл по каждому предмету
    disciplines['История'] /= len(disciplines)
    disciplines['Математика'] /= len(disciplines)
    disciplines['Информатика'] /= len(disciplines)

    return disciplines


def avg_for_each_student(students):
    avg_student = {}
    for student, grades in students.items():
        # ключ - фамилия студента, значение - средний балл студента
        avg_student[student] = sum(grades) / len(grades)

    return avg_student


def exam_result(data: list):
    students = {}
    # создает словарь студентов, ключ - фамилия студента, значение - список оценок
    for item in data:
        students[item[0]] = list(map(int, item[1:]))

    # средний балл для каждого студента
    avg_students = avg_for_each_student(students)
    # средний балл по каждому предмету
    avg_discipline = avg_for_each_discipline(students)

    # таблица результатов сессии
    exam_results_table(students, avg_discipline, avg_students)


if __name__ == '__main__':
    num = int(input("Укажите количество студентов: "))
    students_list = [input("Введите фамилию и оценки студента через пробел: ").split() for _ in range(num)]
    print()
    exam_result(students_list)

    # Александрова 4 5 5
    # Молчанов 4 3 5
    # Кузнецов 2 5 4
    # Сазонов 3 3 5
