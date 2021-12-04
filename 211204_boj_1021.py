from collections import deque
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

queue = deque()
for i in range(n):
    queue.append(i + 1)

result = 0
for number in numbers:
    i = 0
    while number != queue[i]:
        i += 1
    if len(queue) - i < i:
        i = len(queue) - i
    else:
        i = -i
    queue.rotate(i)
    result += abs(i)
    queue.popleft()

print(result)
