
def miro(i, j, n):
    di = [0, 1, 0, -1]
    dj = [1, 0 , -1, 0]
    if (maze[i][j] == 3): # 목적지에 도착한 경우
        return 1
    else:
        maze[i][j] = 1 # 방문한 칸으로 미로에 직접 표시
        for k in range(4): # 주변 칸으로 이동 가능한지 검사
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                if(maze[ni][nj] != 1): # 벽이 아니면 이동
                    r = miro(ni, nj, n)
                    if(r==1):
                        return 1
        return 0 # 가능한 모든 단계에서 목적지를 찾지 못할 때


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for i in range(N)]
    si = 0
    sj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j
                break
    print('#{} {}'.format(tc,miro(si,sj,N)))