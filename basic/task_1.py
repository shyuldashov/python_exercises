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


if __name__ == '__main__':
    text = input("Введите ваш текст: ")  # телефон арбуз вертолёт колбаса фонограмма
    let = input("Введите букву: ")  # а

    if text and let:
        fraction, res_word = fraction_of_letter_in_word(text, let)
        if fraction:
            print(f"Слово: \"{res_word}\"\nДоля: {fraction:.2f}%")  # Слово: "колбаса" Доля: 28.57%
        else:
            print(f"Буква \"{let}\" не встречается ни в одном слове...")
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
