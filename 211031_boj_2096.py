n = int(input())

max_arr = [0] * 6
min_arr = [0] * 6
line = [0] * 3

for i in range(n):
    line = list(map(int, input().split()))

    max_arr[0] = max(max_arr[3], max_arr[4]) + line[0]
    max_arr[1] = max(max_arr[3], max_arr[4], max_arr[5]) + line[1]
    max_arr[2] = max(max_arr[4], max_arr[5]) + line[2]

    min_arr[0] = min(min_arr[3], min_arr[4]) + line[0]
    min_arr[1] = min(min_arr[3], min_arr[4], min_arr[5]) + line[1]
    min_arr[2] = min(min_arr[4], min_arr[5]) + line[2]

    for j in range(3):
        max_arr[j + 3] = max_arr[j]
        min_arr[j + 3] = min_arr[j]

print(max(max_arr[:3]), min(min_arr[:3]))
