line = input()
step = 0
N = len(line)
i = 0
j = N - 1
while i != int(N / 2):
    if line[i] != line[j]:
        step += 1

    j -= 1
    i += 1

print(step)
