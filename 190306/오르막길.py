N = int(input())
num = list(map(int,input().split()))
stack = []
result = []
criteria = 0
stack.append(num[0])
for i in range(1, N):
    if i == N-1 and num[i] > stack[-1]:
        stack.append(num[i])
        a = stack[-1] - stack[criteria]
        result.append(a)
    if stack[-1] < num[i]:
        stack.append(num[i])
    else:
        a = stack[-1] - stack[criteria]
        b = len(stack)
        criteria = b
        stack.append(num[i])
        result.append(a)

print(max(result))

