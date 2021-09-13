import heapq
INF = int(1e9)


n, m, r = map(int, input().split())
t = list(map(int, input().split()))

graph = [[] for i in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


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


result = -1

for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    count = t[i - 1]

    for j in range(1, n + 1):
        if distance[j] != 0 and distance[j] <= m:
            count += t[j - 1]

        if count > result:
            result = count

print(result)
