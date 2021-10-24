from collections import deque

a, b = map(int, input().split())


def bfs(start):
    q = deque()
    q.append((0, start))

    while q:
        cost, number = q.popleft()

        if number == b:
            return cost + 1

        if number * 2 <= b:
            q.append((cost + 1, number * 2))

        new_number = int(str(number) + '1')
        if new_number <= b:
            q.append((cost + 1, new_number))

    return -1


print(bfs(a))
