k = int(input())
numbers = [int(input()) for _ in range(k)]

stack = []
for number in numbers:
    if number == 0:
        stack = stack[:-1]
    else:
        stack.append(number)

if not stack:
    print(0)
else:
    print(sum(stack))
