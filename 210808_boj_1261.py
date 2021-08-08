import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[INF] * m for _ in range(n)]


def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distance[0][0] = 0

    while queue:
        x, y, dist = heapq.heappop(queue)

        if x == n - 1 and y == m - 1:
            print(distance[n - 1][m - 1])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (nx, ny, cost))


dijkstra()
