import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
choice = [[] for i in range(m)]
cycle = False
result = 0

for i in range(m):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        cycle = True
        result = i + 1
        break
    else:
        union_parent(a, b)

print(result if cycle else 0)
