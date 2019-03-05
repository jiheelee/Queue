N, M = map(int, input().split())
C = list(map(int,input().split()))
stack = []
for i in range(N):
    stack.append(i)

while len(stack) > 1:
    p = stack.pop(0)
    melt = C[p] // 2
    if melt == 0 and M < N:
        stack.append(M)
        M = M+1
    elif melt != 0:
        C[p] = melt
        stack.append(p)

print(stack[0])