from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        visisted[z][x][y] = 1

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and box[nz][nx][ny] == 0 and visisted[nz][nx][ny] == 0:
                queue.append([nx, ny, nz])
                box[nz][nx][ny] = box[z][x][y] + 1
                visisted[nz][nx][ny] = 1


m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visisted = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
queue = deque()
isBad = False

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 1:
                queue.append([x, y, z])

bfs()
result = 0

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 0:
                isBad = True
            result = max(result, box[z][x][y])

if isBad == True:
    print(-1)
else:
    print(result - 1)
