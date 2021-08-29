from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

count = set()

houses = []
chickens = []

chicken_distance_array = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

chickens = list(combinations(chickens, M))

for comb in chickens:
    chicken_distance = 0
    for house in houses:
        distance_array = []
        for chicken in comb:
            distance_array.append(
                abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        chicken_distance += min(distance_array)
    chicken_distance_array.append(chicken_distance)

print(min(chicken_distance_array))
