import sys
import heapq

INF = 1e9


a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next_node in graph[now]:
            cost = dist + 1

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


dijkstra(a)

if distance[b] == INF:
    print(-1)
else:
    print(distance[b])
