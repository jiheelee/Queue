T = int(input())

for tc in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))

    max_idx = N - 1
    plus = 0

    for m in range(N-1,-1,-1):
        if price[m] > price[max_idx]:
            max_idx = m
        if m == max_idx:
            pass
        else:
            plus = plus + price[max_idx] - price[m]

    print('#{} {}'.format(tc, plus))