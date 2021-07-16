from collections import deque
import sys

input = sys.stdin.readline


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x, y))


def bfs():
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            result.append(z)

        # a -> b
        if x > 0 and y < b:
            water = min(x, b - y)
            pour(x - water, y + water)

        # a -> c
        if x > 0 and z < c:
            water = min(x, c - z)
            pour(x - water, y)

        # b -> a
        if y > 0 and x < a:
            water = min(y, a - x)
            pour(x + water, y - water)

        # b -> c
        if y > 0 and z < c:
            water = min(y, c - z)
            pour(x, y - water)

        # c -> a
        if z > 0 and x < a:
            water = min(z, a - x)
            pour(x + water, y)

        # c -> b
        if z > 0 and y < b:
            water = min(z, b - y)
            pour(x, y + water)


a, b, c = map(int, input().split())
visited = [[0] * (b + 1) for _ in range(a + 1)]
result = []
q = deque()

bfs()

result.sort()
print(*result)
