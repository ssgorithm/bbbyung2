import sys
import heapq
input = sys.stdin.readline

N = int(input())
numbers = []
zero_cnt = 0
for _ in range(N):
    temp = int(input())
    if temp > 0:
        heapq.heappush(numbers, temp)
    elif temp == 0:
        if len(numbers) == 0:
            print(0)
        else:
            print(heapq.heappop(numbers))
