T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    num_list = list(map(int,input().split()))
    idx = M
    for k in range(K):
        if idx < len(num_list):
            n = num_list[idx-1] + num_list[idx]
        elif idx == len(num_list):
            n = num_list[-1] + num_list[0]
            idx = - 1
        elif idx > len(num_list):
            idx = idx % len(num_list)
            n = num_list[idx-1] + num_list[idx]
        num_list.insert(idx, n)
        idx = idx + M
    num_list = num_list[::-1]
    num = min(10,len(num_list))
    print('#{} {}'.format(tc,' '.join(map(str,num_list[0:num]))))