import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dogam = []
dogam_dic = {}

for i in range(n):
    pokemon = input()
    dogam.append(pokemon)
    dogam_dic[pokemon] = i + 1

for _ in range(m):
    problem = input()

    if problem.isdigit():
        print(dogam[int(problem) - 1])
    else:
        print(dogam_dic[problem])
