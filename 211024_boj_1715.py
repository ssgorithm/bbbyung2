import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    result = 0
    while len(cards) > 1:
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        result += first + second
        heapq.heappush(cards, first + second)
    print(result)
