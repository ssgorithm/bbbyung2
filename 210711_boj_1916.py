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

            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])
