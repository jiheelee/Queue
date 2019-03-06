import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    multiple = []

    for i in range(N):
        for j in range(N-i-1):
            mul = num_list[i] * num_list[i+j+1]
            a = str(mul)
            c = 0
            for k in range(len(a)):
                if k < len(a)-1 and int(a[k]) > int(a[k+1]):
                    c = 1
                    break
            if c == 0:
                multiple.append(int(a))


    result = max(multiple) if multiple else -1
    print('#{} {}'.format(tc,result))