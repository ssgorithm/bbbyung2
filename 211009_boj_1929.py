def prime_check(num):
    if num == 1:
        return False
    end = int(num ** 0.5)
    for i in range(2, end + 1):
        if num % i == 0:
            return False
    return True


m, n = map(int, input().split())

for num in range(m, n + 1):
    if prime_check(num):
        print(num)
