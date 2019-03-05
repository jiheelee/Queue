T = int(input())
for tc in range(1,T+1):
    N = int(input())

    result = [[] for i in range(N)]
    for i in range(N):
        if i == 0:
            result[i].append(1)
        else:
            for j in range(i+1):
                a = 0
                b = 0
                if j-1 >= 0:
                    a = result[i-1][j-1]
                if j < len(result[i-1]):
                    b = result[i-1][j]
                s = a + b
                result[i].append(s)
    print("#{}".format(tc))
    for i in result:
        for j in i:
            print(j,end=" ")
        print()

