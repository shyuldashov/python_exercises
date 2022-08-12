# 1102. Странный диалог

# Одна сущность по имени "one" беседует со своим другом, сущностью "puton", и нас интересует их разговор.
# "One" может говорить слова "out" и "output", кроме того, он может называть своего друга по имени.
# "Puton" может говорить слова "in", "input" и "one". Они прекрасно понимают друг друга и даже пишут
# диалоги в строки без пробелов между словами.

# Дано N строк. Определите, какие из них являются диалогами

# Исходные данные
# В первой строке ввода содержится одно неотрицательное целое число N ≤ 1000.
# Следующие N строк содержат непустые последовательности строчных латинских букв.
# Общая длина всех строк не превышает 107 символов.

# Результат
# Вывод состоит из N строк. Строка содержит слово "YES", если соответствующая строка
# ввода является некоторым диалогом сущностей "one" и "puton", в противном случае строка содержит "NO".


# Пример
# исходные данные	           результат
# 6
# puton                         # YES
# inonputin                     # NO
# oneputonininputoutoutput      # YES
# oneininputwooutoutput         # NO
# outpu                         # NO
# utput                         # NO


# Способ 1
n = int(input())
flag = True
current_player = ''

while n > 0:
    text = input()
    if flag:
        if 'puton' in text:
            flag = False
            current_player = 'puton'
        elif 'one' in text:
            flag = False
            current_player = 'one'

    if current_player and current_player != 'puton' and current_player in text:
        print("YES")
        current_player = 'one'
    elif current_player and current_player != 'one' and current_player in text:
        print("YES")
        current_player = 'puton'
    else:
        print("NO")

    n -= 1
