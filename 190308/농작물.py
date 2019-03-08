import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    farm = [list(map(int,input())) for i in range(N)]
    lu = 0
    ru = 0
    ld = 0
    rd = 0
    for k in range(N//2):
        for p in range(k+1):
            lu += farm[p][k-p]
            ru += farm[p][N-1-(k-p)]
            ld += farm[N-1-p][k-p]
            rd += farm[N-1-p][N-1-(k-p)]
    result = 0
    for i in farm:
        result += sum(i)
    print('#{} {}'.format(tc,result-(lu+ru+ld+rd)))
