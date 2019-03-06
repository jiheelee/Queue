import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    multiple = [0] * (abs(N-M) + 1)



    if N < M:
        for i in range(N):
            for j in range(M-N+1):
                mul = A[i] * B[i+j]
                multiple[j] += mul
    else:
        for i in range(M):
            for j in range(N-M+1):
                mul = A[i+j] * B[i]
                multiple[j] += mul
    print('#{} {}'.format(tc, max(multiple)))