s = input()

# 전부 0인 경우
count_zero = 0
# 전부 1인 경우
count_one = 0

if s[0] == '0':
    count_one += 1
else:
    count_zero += 1

for i in range(len(s) - 1):
    # 현재 수가 다음 수와 다른 경우
    if s[i] != s[i + 1]:
        # 다음 수가 0인 경우
        if s[i + 1] == '0':
            count_one += 1
        # 다음 수가 1인 경우
        else:
            count_zero += 1

print(min(count_one, count_zero))
