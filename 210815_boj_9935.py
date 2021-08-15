def check(string):
    if string == exp:
        return True
    return False


word = list(input())
exp = input()

check_string = ''
stack = []

if len(exp) == 1:
    for char in word:
        if char != exp:
            stack.append(char)
else:
    for index in range(len(word)):
        if index == 0:
            stack.append(word[index])

        else:
            check_string = word[index]
            if len(stack) + 1 >= len(exp):
                temp = []
                while len(temp) + 1 != len(exp):
                    temp.append(stack.pop())
                temp.reverse()
                check_string = ''.join(temp) + check_string

                if not check(check_string):
                    stack += list(check_string)
            else:
                stack.append(word[index])

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
