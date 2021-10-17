n, h = map(int, input().split())
top = [0] * (h + 1)
bottom = [0] * (h + 1)

for i in range(n):
    height = int(input())
    if i % 2 == 0:
        bottom[h - height + 1] += 1
    else:
        top[height] += 1

for i in range(h - 1, 0, -1):
    top[i] += top[i + 1]

for i in range(1, h + 1):
    bottom[i] += bottom[i - 1]


result = [0] * (h + 1)
for i in range(1, h + 1):
    result[i] = top[i] + bottom[i]

result = result[1:]
obstacle_count = min(result)
print(obstacle_count, result.count(obstacle_count))
