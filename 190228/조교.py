import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    result_list = ["D0","C-","C0","C+","B-","B0","B+","A-","A0","A+"]
    N, K = map(int,input().split())
    score = []
    for n in range(N):
        A, B, C = map(int,input().split())
        result = 0.35 * A + 0.45 * B + 0.2 * C
        score.append(result)
    target = score[K-1]
    score.sort()
    for i in range(len(score)):
        if score[i] == target:
            target_idx = i
    student_list = []

    for s in range(len(score)):
        student_list.append(result_list[s // (N//10)])
    print(f'#{tc} {student_list[target_idx]}')