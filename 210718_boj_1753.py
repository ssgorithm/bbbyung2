import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


dijkstra(k)

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)
