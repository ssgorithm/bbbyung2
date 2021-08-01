n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

left, right = 1, max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    amount = 0

    for tree in trees:
        if tree > mid:
            amount += tree - mid

    if amount >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
