T = int(input())
for tc in range(1,T+1):
    s = input()
    l = len(s)
    print('..#.'* l + '.')
    print('.#.#'*l + '.')
    for i in range(l):
        print('#.{}.'.format(s[i]),end="")
    print("#")
    print('.#.#' * l + '.')
    print('..#.' * l + '.')

