# Гипотеза Эйлера о сумме степеней

# В 1769 году Леонард Эйлер сформулировал обобщенную версию "Великой теоремы Ферма", предполагая, что
# по крайней мере n энных степеней необходимо для получения суммы, которая сама является энной степенью для n > 2.

# Напишите программу для опровержения гипотезы Эйлера (продержавшейся до 1967 года), и найдите четыре
# положительных целых числа, сумма 5-х степеней которых равна 5-й степени другого положительного целого числа.

# Таким образом, найдите пять натуральных чисел а, b, c, d, е удовлетворяющих условию:

# 		a^5 + b^5 + c^5 + d^5 = e^5

# В ответе укажите сумму a + b + c + d + e

# Примечание 1. Используйте вложенный цикл for .
# Примечание 2. Считайте, что числа а, b, c, d, е не превосходят 150.


def euler_sum(max_n=250):
    p = 5  # степень
    nums_powers = {i ** p: i for i in range(0, max_n)}  # ключ: р-я степень числа, значение: само число

    keys = list(nums_powers.keys())  # ключи (p-е степени каждого числа от 2 до max_n)

    for d in range(0, max_n):
        for c in range(0, d):
            for b in range(0, c):
                for a in range(0, b):
                    power_sum = sum(keys[i] for i in (a, b, c, d))  # сумма степеней чисел a, b, c, d
                    if power_sum in nums_powers:
                        e = nums_powers[power_sum]  # получить число, степень которого равна сумме a, b, c, d

                        # раскомментируйте это, чтобы посмотреть какие значения a, b, c, d, e
                        print(f'{a}^5 + {b}^5 + {c}^5 + {d}^5 = {e}^5')

                        # возвращает сумму a + b + c + d + e
                        return a + b + c + d + e


if __name__ == '__main__':
    n = 150
    import time

    start = time.time()
    euler_sum(n)
    end = time.time()
    print(f'{end - start:.4f} сек')
