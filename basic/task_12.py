# Даны два числа A и B. Вам нужно вычислить их сумму A+B.
# В этой задаче вам нужно читать из файла и выводить ответ в файл


# Формат ввода
# Первая строка входного файла содержит числа A и B (-2 ⋅ 10^9 ≤ A, B ≤ 2 ⋅ 10^9) разделенные пробелом

# Формат вывода
# В единственной строке выходного файла выведите сумму чисел A+B

with open('input.txt', mode='r', encoding='utf-8') as file_to_read, \
        open('output.txt', mode='w', encoding='utf-8') as file_to_write:

    # чтение строки
    row = file_to_read.readline()

    # запись в выходной файл
    file_to_write.write(str(sum(int(i) for i in row.strip().split())))
