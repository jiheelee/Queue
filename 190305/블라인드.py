M, N = map(int,input().split())
a = []

for i in range(5*M+1):
    a.append(input())
# print(a)
windows = []
for i in range(M):
    for j in range(N):
        s = ""
        for k in range(1, 5):
            s += a[5*i+k][5*j+1:5*j+5]
        windows.append(s)
# print(windows)
blind = ['................','****............','********........','************....','****************']
count = [0,0,0,0,0]

for i in range(len(blind)):
    for j in windows:
        if blind[i] == j:
            count[i] += 1

for c in count:
    print(c, end=" ")