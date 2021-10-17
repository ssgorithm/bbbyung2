word = input()
search = input()

index = 0
result = 0

while len(word) - index >= len(search):
    if word[index:index + len(search)] == search:
        result += 1
        index += len(search)
    else:
        index += 1

print(result)
