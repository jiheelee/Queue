N = int(input())
k = (N-2) //6
a = 0
result = 0

for i in range(N):
    a = a + i
    if k < a:
        result = i
        break

print(result+1)

print(0//6)