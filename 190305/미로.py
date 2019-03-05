def bfs(i, j, n):

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = []
    visited = [[0]*n for i in range(n)]
    q.append(i)
    q.append(j)
    visited[i][j] = 1
    while len(q) != 0:
        i = q.pop(0)
        j = q.pop(0)
        if room[i][j] == 3:
            return visited[i][j]
        for m in range(4):
            ni = i + di[m]
            nj = j + dj[m]
            if (ni>=0 and ni < n and nj >= 0 and nj < n):
                if room[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] = 1

    return 0


import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    t = int(input())
    room = [list(map(int,input())) for i in range(16)]
    sj = 0
    for j in range(len(room[1])):
        if room[1][j] == 2:
            sj = j

    print('#{} {}'.format(tc, bfs(1,sj,16)))