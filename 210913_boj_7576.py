from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))


bfs()

result = -1
isGood = True

for row in graph:
    for element in row:
        if element == 0:
            isGood = False

        result = max(result, element)

if not isGood:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)
