def pal(word):
    l = len(word)
    for i in range(l//2):
        if word[i] == "?" or word[-(i+1)] == "?":
            continue
        elif word[i] != word[-(i+1)]:
            return "Not exist"
    return "Exist"
T = int(input())
for tc in range(1,T+1):
    print('#{} {}'.format(tc, pal(input())))
