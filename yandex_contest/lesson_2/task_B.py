office = 0
home = 1
store = 2

street = [int(i) for i in input().strip().split()]

plus_distance = 0
minus_distance = 0
max_distance = 0

flag_plus = False
flag_minus = False

for i in range(len(street)):
    if street[i] == home:
        for j in range(1, len(street)):
            if (i + j) < 10:
                if street[i + j] != store:
                    plus_distance += 1
                else:
                    plus_distance += 1
                    flag_plus = True
                    break
            if (i - j) >= 0:
                if street[i - j] != store:
                    minus_distance += 1
                else:
                    minus_distance += 1
                    flag_minus = True
                    break
        if flag_plus:
            if max_distance < plus_distance:
                max_distance = plus_distance

        elif flag_minus:
            if max_distance < minus_distance:
                max_distance = minus_distance

        flag_plus = False
        flag_minus = False

        plus_distance = 0
        minus_distance = 0

print(max_distance)
