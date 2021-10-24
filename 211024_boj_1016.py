min_num, max_num = map(int, input().split())
validate_list = [1 for _ in range(max_num - min_num + 1)]

index = 2

while index ** 2 <= max_num:
    num = min_num // (index ** 2)

    while num * (index ** 2) <= max_num:
        if 0 <= num * (index ** 2) - min_num <= max_num - min_num:
            validate_list[num * (index ** 2) - min_num] = 0
        num += 1

    index += 1

print(sum(validate_list))
