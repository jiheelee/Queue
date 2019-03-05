def millionare(price):
    global plus
    max_idx = 0
    for idx in range(len(price)):
        if price[max_idx] < price[idx]:
            max_idx = idx
    plus = plus + price[max_idx] * max_idx - sum(price[0:max_idx])

    for i in range(max_idx+1):
        price.pop(0)

    if price:
        millionare(price)
    else:
        return
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    plus = 0

    millionare(price)
    print('#{} {}'.format(tc, plus))



