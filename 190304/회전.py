T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    l = list(map(int,input().split()))

    for i in range(M):
        a = l.pop(0)
        l.append(a)

    print('#{} {}'.format(tc, l[0]))

