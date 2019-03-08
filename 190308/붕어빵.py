# T = int(input())
N, M = map(int,input().split())
buy = [0] * 61
for i in range(M):
    t, c = map(int,input().split())
    buy[t] += c

N = 0

for i in range(1,61):
    N += 2
    N = N - buy[i]
    if N < 0:
        break
if N < 0:
    print(-1)
else:
    print(N)

