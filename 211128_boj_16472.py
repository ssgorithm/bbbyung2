n = int(input())
string = list(input())
length = len(string)
start = 0
end = 0
current_size = 1
max_size = 1
alphabet_cnt = [0] * 26
alphabet_cnt[ord(string[0]) - ord('a')] += 1

while start < length and end < length:
    end += 1

    if end == length:
        break
    if alphabet_cnt[ord(string[end]) - ord('a')] == 0:
        alphabet_cnt[ord(string[end]) - ord('a')] += 1
        current_size += 1
    else:
        alphabet_cnt[ord(string[end]) - ord('a')] += 1

    if current_size <= n:
        max_size = max(max_size, end - start + 1)

    while current_size > n and start < end:
        if alphabet_cnt[ord(string[start]) - ord('a')] == 1:
            alphabet_cnt[ord(string[start]) - ord('a')] -= 1
            current_size -= 1
        else:
            alphabet_cnt[ord(string[start]) - ord('a')] -= 1
        start += 1

print(max_size)
