T = int(input())

for tc in range(1,T+1):
    num_list = []
    N = int(input())
    mul = 1
    count = 0
    while len(set(num_list)) <= 9:
        a = N * mul
        for i in str(a):
            num_list.append(i)
        mul += 1
        count += 1
    print('#{} {}'.format(tc, count * N))
