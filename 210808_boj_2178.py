from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]


def bfs(start, end):
    queue = deque()
    queue.append((start, end, 0))
    graph[start][end] = 0

    while queue:
        x, y, count = queue.popleft()
        count += 1

        if x == n - 1 and y == m - 1:
            print(count)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny, count))


bfs(0, 0)
