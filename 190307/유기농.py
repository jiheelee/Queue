def bfs(i, j, N, M):
    q = []
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q.append(i)
    q.append(j)
    while q:
        i = q.pop(0)
        j = q.pop(0)
        for d in range(4):
            si = i + di[d]
            sj = j + dj[d]
            if si >= 0 and si < N and sj >= 0 and sj < M:
                if ground[si][sj] == 1:
                    ground[si][sj] = 0
                    q.append(si)
                    q.append(sj)


T = int(input())
for tc in range(1,T+1):
    M, N, K = map(int,input().split())
    ground = [[0]*M for n in range(N)]
    for k in range(K):
        j, i = map(int,input().split())
        ground[i][j] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                ground[i][j] = 0
                bfs(i,j,N,M)
                count += 1
    print(count)
