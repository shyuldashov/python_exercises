# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей.
# Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.


# Формат ввода
# Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель.
# Известно, что общее число кандидатов не превосходит 20, но в отличии от предыдущих задач
# список кандидатов яно не задан.

# Формат вывода
# Если есть кандилат, набравший более 50% голосов, программа должна вывести его имя.
# Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
# затем имя кандидата, завявшего второе место

# Полуэкт Варфоломеев
# Варфоломей Полуэктов
# Варфоломей Виссарионов
# Виссарион Полуэктов
# Ким Чен Ир
# Ким Ир Сен

# ==================== Решение задачи без функций ====================

candidates = {}

# чтение файла
with open('votes.txt', 'r', encoding='utf-8') as file:
    # читать по строчно
    for row in file.readlines():
        # если количество кандидатов больше 20, останавливается программа
        if len(candidates) > 20:
            break

        # если за кандидата ещё не проголосовали, то добавим его в словарь с одним голосом
        if (row := row.strip()) not in candidates:
            candidates[row] = 1
            continue

        # если до сюда долшли, значит кандидат уже есть в словаре, увеличивает количество голосов на 1
        candidates[row] += 1

    # общее количество голосов
    total_votes = lambda x: sum([v for k, v in x.items()])

    # рассчитает соотношение голосов
    calculate_ratio = {k: round((v / total_votes(candidates) * 100), 2) for k, v in candidates.items()}

    # сортировка кандидатов по соотношению
    result = sorted(calculate_ratio.items(), key=lambda x: x[1], reverse=True)

    for i in range(0, 2):
        if result[i][1] > 50:
            print(result[i][0])
            break
        print(result[i][0])


# ==================== Решение задачи с использованием функционального программирования ====================
def get_and_count_votes(filename: str) -> dict:
    candidates = {}

    # чтение файла
    with open(filename, 'r', encoding='utf-8') as file:
        # читать по строчно
        for row in file.readlines():
            # если количество кандидатов больше 20, останавливается программа
            if len(candidates) > 20:
                break

            # если за кандидата ещё не проголосовали, то добавим его в словарь с одним голосом
            if (row := row.strip()) not in candidates:
                candidates[row] = 1
                continue

            # если до сюда долшли, значит кандидат уже есть в словаре, увеличивает количество голосов на 1
            candidates[row] += 1

    return candidates


def total_votes(candidates: dict) -> dict:
    return sum([v for k, v in candidates.items()])


def calculate_ratio(candidates: dict, total: int) -> dict:
    return {k: round((v / total * 100), 2) for k, v in candidates.items()}


def sort_candidates_by_ratio(ratio_candidates: dict) -> list:
    return sorted(ratio_candidates.items(), key=lambda x: x[1], reverse=True)


def print_result(file_name: str):
    votes = get_and_count_votes(file_name)
    total = total_votes(votes)
    ratio = calculate_ratio(votes, total)
    result = sort_candidates_by_ratio(ratio)

    for i in range(0, 2):
        if result[i][1] > 50:
            print(result[i][0])
            break
        print(result[i][0])


if __name__ == '__main__':
    # print_result('votes.txt')
    # print_result('votes_2.txt')
    print_result('votes_3.txt')

    '''
    votes.txt
    Полуэкт Варфоломеев
    Варфоломей Полуэктов
    Полуэкт Варфоломеев
    
    votes_2.txt
    Полуэкт Варфоломеев
    Варфоломей Виссарионов
    Виссарион Полуэктов
    Варфоломей Виссарионов
    Варфоломей Виссарионов
    Полуэкт Варфоломеев
    
    votes_3.txt
    Полуэкт Варфоломеев
    Варфоломей Виссарионов
    Виссарион Полуэктов
    Полуэкт Варфоломеев
    Варфоломей Виссарионов
    Варфоломей Виссарионов
    Полуэкт Варфоломеев
    Ким Чен Ир
    Ким Ир Сен
    Полуэкт Варфоломеев
    Полуэкт Варфоломеев
    Ким Чен Ир
    '''
