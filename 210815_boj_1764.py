n, m = list(map(int, input().split(' ')))

listen = [input() for _ in range(n)]
watch = [input() for _ in range(m)]

result = list(set(listen) & set(watch))

print(len(result))
for ele in sorted(result):
    print(ele)
