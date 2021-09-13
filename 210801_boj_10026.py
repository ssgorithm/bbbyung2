from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
picture = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

copy_picture = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if picture[i][j] == 'R' or picture[i][j] == 'G':
            copy_picture[i][j] = 1
        else:
            copy_picture[i][j] = 2

yes_count = 0
no_count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, array, color):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == color:
                array[nx][ny] = 0
                queue.append((nx, ny))


for i in range(n):
    for j in range(n):
        if picture[i][j] != 0:
            bfs(i, j, picture, picture[i][j])
            yes_count += 1

        if copy_picture[i][j] != 0:
            bfs(i, j, copy_picture, copy_picture[i][j])
            no_count += 1

print(yes_count, no_count)
