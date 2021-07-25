import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
q = deque()
for key, value in enumerate(numbers, 1):
    q.append([key, value])

result = []

while q:
    index, num = q.popleft()
    result.append(index)

    if len(q) == 1:
        result.append(q.pop()[0])
    else:
        if num > 0:
            for _ in range(num - 1):
                q.append(q.popleft())
        else:
            for _ in range(abs(num)):
                q.appendleft(q.pop())

print(*result)
