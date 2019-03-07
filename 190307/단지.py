def bfs(start_i,start_j,N):
        #start idx 넣어주기
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        count = 1
        q = []
        q.append(start_i)
        q.append(start_j)
        # 1 없어질 때까지 방향 탐색하기
        while len(q) > 0:
            i = q.pop(0)
            j = q.pop(0)
            for d in range(4):
                si = i + di[d]
                sj = j + dj[d]
                if si >= 0 and si < N and sj >= 0 and sj < N:
                    if apt[si][sj] == 1:
                        count += 1
                        apt[si][sj] = 0
                        q.append(si)
                        q.append(sj)
        return count

N = int(input())

apt = [list(map(int,input())) for i in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if apt[i][j] == 1:
            start_i = i
            start_j = j
            apt[i][j] = 0
            result.append(bfs(start_i,start_j,N))

print(len(result))
for i in sorted(result):
    print(i)