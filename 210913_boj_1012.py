import sys
sys.setrecursionlimit(50000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    result = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1

    print(result)
