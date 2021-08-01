import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    order = list(input().split())

    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        print(queue.pop(0) if queue else -1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(0 if queue else 1)
    elif order[0] == 'front':
        print(queue[0] if queue else -1)
    elif order[0] == 'back':
        print(queue[-1] if queue else -1)
    else:
        pass
