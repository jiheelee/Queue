T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    k = (N % M)
    print('#{} {}'.format(tc,(((N//M)**(M-k))*((N//M+1)**k))))
# print((3**6) * (4 ** 3))