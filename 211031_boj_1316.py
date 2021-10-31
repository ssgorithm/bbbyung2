n = int(input())
words = [input() for _ in range(n)]
result = 0
for word in words:
    group = []
    for a in list(word):
        if a in group and group[-1] != a:
            break
        else:
            group.append(a)
    if len(group) == len(word):
        result += 1
print(result)
