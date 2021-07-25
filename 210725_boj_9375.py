import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}

    for _ in range(n):
        name, type = input().split()

        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1

    result = 1

    for key in clothes.keys():
        result *= clothes[key] + 1

    print(result - 1)
