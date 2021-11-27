n = int(input())
pattern = ['***', '* *', '***']


def star(n):
    array = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            array.append(n[i % len(n)] + ' ' * len(n) + n[i % len(n)])
        else:
            array.append(n[i % len(n)] * 3)
    return array


count = 0
while n != 3:
    n = int(n / 3)
    count += 1

for _ in range(count):
    pattern = star(pattern)

for element in pattern:
    print(element)
