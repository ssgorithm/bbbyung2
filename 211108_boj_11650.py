n = int(input())

dots = []

for _ in range(n):
    dots.append(list(map(int, input().split(' '))))

result = sorted(dots, key=lambda x: (x[0], x[1]))

for i in result:
    print(i[0], i[1])
