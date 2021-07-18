import sys

input = sys.stdin.readline

n = int(input())
num_array = list(map(int, input().split()))
m = int(input())
cases = list(map(int, input().split()))


def binary_search(num):
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2

        if num_array[mid] == num:
            return 1
        elif num_array[mid] < num:
            l = mid + 1
        else:
            r = mid - 1

    return 0


num_array.sort()
result = []

for case in cases:
    result.append(binary_search(case))

print(*result)
