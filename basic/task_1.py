"""Даны m(m>1) слов. В каком из них доля (в %) заданной буквы больше.
Определить функцию для расчета доли некоторой буквы в слове"""


def fraction_of_letter_in_word(words: str, letter: str) -> tuple:
    word = ''  # слово, в котором доля буквы больше
    frequency = 0  # частота буквы

    for w in words.split():
        if (f := (w.lower().count(letter.strip().lower())) / len(w)) >= frequency:
            word = w
            frequency = f

    return frequency * 100, word


def fraction_of_letter_in_word_2(words: str, letter) -> tuple:
    # dict comprehension, создает словарь, где ключом является слово, значением является частота букв
    words_and_letter_freq = {key: key.lower().count(letter.strip().lower()) / len(key) for key in words.split()}

    # сортирует словарь по значению в порядке убывания и возвращает первый элемент (кортеж из двух элементов)
    return sorted(words_and_letter_freq.items(), key=lambda x: x[1], reverse=True)[0]


if __name__ == '__main__':
    text = input("Введите ваш текст: ")  # телефон арбуз вертолёт колбаса фонограмма
    let = input("Введите букву: ")  # а

    if text and let:
        # Способ 1
        # fraction, res_word = fraction_of_letter_in_word(text, let)

        # Способ 2
        res_word, fraction = fraction_of_letter_in_word_2(text, let)

        if fraction:
            print(f'Слово: "{res_word}"\nДоля буквы "{let}": {fraction:.2f}%')  # Слово: "колбаса" Доля: 28.57%
        else:
            print(f'Буква "{let}" не встречается ни в одном слове...')
    else:
        print("Вы не указали никаких слов или букву...")

    # ---- Test ----
    # кОлокОлчик потОлок оккО хОрошо мнОго
    # о

    # кОлокОлчик потОлок оккО хОрошо мнОго
    # к

    # LEXUS BMW AUDI CADILLAC BENZ
    # e

    # sun rocket sea cosmos
    # h
