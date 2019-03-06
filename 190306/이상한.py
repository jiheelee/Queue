import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = input()

    M = str(N)
    num_list = []
    for i in M:
        num_list.append(i)

    result = "B"
    while len(num_list) > 1:
        i = num_list.pop(-1)
        j = num_list.pop(-1)
        sum = str(int(i) + int(j))
        for s in sum:
            num_list.append(s)
        result = "B" if result == "A" else "A"

    print('#{} {}'.format(tc, result))