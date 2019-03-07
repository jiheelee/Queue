import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    string = input()
    two = ""
    for s in string:

        if(ord('A') <= ord(s) <=ord('Z')):
            n = ord(s) - ord('A')
        if(ord('a') <= ord(s) <=ord('z')):
            n = ord(s) - ord('a') + 26
        if(ord('0') <= ord(s) <= ord('9')):
            n = ord(s) - ord('0') + 52
        if(s == '+'):
            n = 62
        if(s == '/'):
            n = 63
        n = str(bin(n))
        n = n.split("0b")
        n = n[1]
        z = (6-len(n))*'0'
        two += (z+n)
        result = ""
    for i in range(len(two)//8):
        a = ""
        for j in range(8):
            a += two[8*i+j]
        b = '0b' + a
        result += chr(int(b,2))
    print('#{} {}'.format(tc, result))




