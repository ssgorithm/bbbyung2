from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = 0

    while q:
        x, y = q.popleft()

        if x == ex and y == ey:
            return graph[ex][ey]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


t = int(input())

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    graph = [[-1] * l for _ in range(l)]

    print(bfs(sx, sy, ex, ey))
