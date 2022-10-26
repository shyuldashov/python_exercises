i = 0  # counter
nums = []  # all nums
while (num := int(input())):
    nums.append(num)
    i += 1

    if i >= 10000:
        break

max_item = max(nums)
result = print(nums.count(max_item))
