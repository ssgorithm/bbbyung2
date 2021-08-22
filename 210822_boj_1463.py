n = int(input())
result = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        continue
    values = []
    if i % 3 == 0:
        values.append(result[i // 3] + 1)
    if i % 2 == 0:
        values.append(result[i // 2] + 1)
    values.append(result[i - 1] + 1)
    result[i] = min(values)

print(result[n])
