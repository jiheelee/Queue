N = int(input())
for i in range(1,N+1):
    num = str(i)
    count = 0
    for alp in num:
        if alp in ["3","6","9"]:
            count += 1
    if count != 0:
        print("-" * count, end=" ")
    else:
        print(i, end=" ")