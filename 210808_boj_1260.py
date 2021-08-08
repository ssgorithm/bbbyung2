n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)


def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=' ')

    for i in range(1, n + 1):
        if not visited[i] and graph[vertex][i] == 1:
            dfs(i)


def bfs(vertex):
    queue = [vertex]
    visited[vertex] = False

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for i in range(1, n + 1):
            # dfs에서 visited가 모두 True가 됐으므로 bfs에서는 False로 방문 여부 확인
            if visited[i] and graph[vertex][i] == 1:
                queue.append(i)
                visited[i] = False


for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1


dfs(v)
print()
bfs(v)
