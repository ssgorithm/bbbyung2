from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
result = []


def bfs(start, end):
    queue = deque()
    queue.append((start, end))
    count = 0
    graph[start][end] = 0

    while queue:
        x, y = queue.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
result.sort()
for number in result:
    print(number)
