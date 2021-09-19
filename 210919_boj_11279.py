import heapq
import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    temp = int(input())
    if temp != 0:
        heapq.heappush(heap, [-temp, temp])
    elif temp == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
