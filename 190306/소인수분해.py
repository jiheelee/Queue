import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    small = [2,3,5,7,11]
    count = [0] * 5
    for i in range(5):
        while N % small[i] == 0:
            N = N/small[i]
            count[i] += 1
    print('#{} {}'.format(tc, " ".join(map(str, count))))
