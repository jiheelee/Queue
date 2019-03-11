T = int(input())
for tc in range(1,T+1):
    S, N = map(int,input().split())
    keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    words = list(input().split())
    S = str(S)
    s = len(S)
    cnt = 0
    for word in words:
        c = 0
        if len(word) != s:
            c = 1
        else:
            for i in range(s):
                if word[i] not in keypad[int(S[i])]:
                    c = 1
                    break
        if c == 0:
            cnt += 1
    print('#{} {}'.format(tc,cnt))