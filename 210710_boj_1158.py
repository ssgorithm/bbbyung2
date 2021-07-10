n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
result = []
num = k - 1

for i in range(n):
    if len(arr) > num:
        result.append(str(arr.pop(num)))
        num += k - 1
    elif len(arr) <= num:
        num = num % len(arr)
        result.append(str(arr.pop(num)))
        num += k - 1

print(f'<{", ".join(result)}>')
