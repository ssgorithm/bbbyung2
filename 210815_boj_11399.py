N = int(input())
customer = list(map(int, input().split()))
customer.sort()
temp = 0
result = 0

for c in customer:
    temp += c
    result += temp

print(result)
