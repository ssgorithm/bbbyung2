n, x = map(int, input().split())

if n > x or n * 26 < x:
    print('!')
else:
    string_list = ['A'] * n
    x -= n
    i = n - 1

    while x > 0:
        if x >= 25:
            string_list[i] = 'Z'
            i -= 1
            x -= 25
        else:
            string_list[i] = chr(x + 65)
            break

    print(''.join(string_list))
