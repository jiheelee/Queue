T = int(input())
for tc in range(1,11):
    string = input()
    for i in range(1,11):
        s = string[0:i]
        check = 0
        for j in range(30//i):
            if s != string[i*j:i*j+i]:
                check = 1
                break
        if check == 0:
            print('#{} {}'.format(tc, i))
            break
