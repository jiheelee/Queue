import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    line = []
    for i in range(N):
        line.append(list(map(int,input().split())))

    P = int(input())
    stop = []
    for p in range(P):
        stop.append(int(input()))
    count = [0] * 5001

    for i in range(N):
        a, b = line[i][0], line[i][1]
        # a = stop.index(a)
        # b = stop.index(b)
        for j in range(a,b+1):
            count[j] += 1
    result = []
    for i in stop:
        result.append(count[i])


    print('#{} {}'.format(tc," ".join(map(str,result))))

# 실행 결과 짧은 코드
# res = []
# for t in range(int(input())):
#     bus = [0]*5001
#     stop = []
#     for n in range(int(input())):
#         A, B = map(int, input().split())
#         for i in range(A, B+1):
#             bus[i] += 1
#     for p in range(int(input())):
#         stop.append(str(bus[int(input())]))
#     res.append("#{} {}".format(t+1, ' '.join(stop)))
# 
# for i in range(len(res)):
#     print(res[i])