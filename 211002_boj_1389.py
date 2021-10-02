import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(e):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = [0] * (v + 1)

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i != j:
            result[i] += graph[i][j]

print(result.index(min(result[1:])))
