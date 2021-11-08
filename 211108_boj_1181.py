n = int(input())
words = [input() for _ in range(n)]
words = list(set(words))
result = sorted(words, key=lambda x: (len(x), x))
print('\n'.join(result))
