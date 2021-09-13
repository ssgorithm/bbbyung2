from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque()
    queue.append((0, 0, 1))

    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while queue:
        x, y, cost = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][cost]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and cost == 1:
                    visited[nx][ny][0] = visited[x][y][cost] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visited[nx][ny][cost] == 0:
                    visited[nx][ny][cost] = visited[x][y][cost] + 1
                    queue.append((nx, ny, cost))
    return -1


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
walls = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            walls.append((i, j))


print(bfs())
