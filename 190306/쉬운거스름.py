T = int(input())
for tc in range(1,T+1):
    money = int(input())
    count = [0]*8
    for i in range(8):
        t = (10000 if i % 2 else 50000) // (10**(i//2))
        while money-t >= 0:
            money = money - t
            count[i] += 1
    print('#{}\n{}'.format(tc," ".join(map(str,count))))