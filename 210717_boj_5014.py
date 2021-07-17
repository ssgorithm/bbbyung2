from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        x = q.popleft()

        for i in range(2):
            nx = x + directions[i]

            if 0 <= nx < f and not visited[nx]:
                q.append(nx)
                result[nx] = result[x] + 1
                visited[nx] = 1


f, s, g, u, d = map(int, input().split())
directions = [u, -d]

visited = [0 for _ in range(f)]
result = [-1 for _ in range(f)]
result[s - 1] = 0

bfs(s - 1)

if result[g - 1] != -1:
    print(result[g - 1])
else:
    print('use the stairs')
