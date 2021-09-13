def dfs(node):
    visited[node] = 1

    for i in range(n):
        if graph[node][i] == 1 and visited[i] == 0:
            dfs(i)


n = int(input())
pairs = int(input())
graph = [[0] * n for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(pairs):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

dfs(0)

result = 0

for i in range(1, n):
    if visited[i] == 1:
        result += 1

print(result)
