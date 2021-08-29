coin_num, coin_sum = map(int, input().split())
coin_list = [int(input()) for _ in range(coin_num)]

result = 0
for coin in coin_list[::-1]:
    if coin <= coin_sum:
        result += coin_sum // coin
        coin_sum %= coin

print(result)
