import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

dictionary = {}

for number in n_list:
    if number not in dictionary:
        dictionary[number] = 1
    else:
        dictionary[number] += 1

m = int(input())
m_list = list(map(int, input().split()))

for number in m_list:
    if number in dictionary:
        print(str(dictionary[number]), end=' ')
    else:
        print('0', end=' ')
