def lagr(n, k):
    sq = int(n ** 0.5)
    if sq ** 2 == n:
        print(sq, end='')
        return int(sq ** 2)
    while sq >= 1:
        s = sq ** 2
        if k + 1 < 4:
            s += lagr(n - sq ** 2, k + 1)
        if s == n:
            print(' ', sq, sep='', end='')
            return int(s)
        sq -= 1
    return 0


n = int(input())
lagr(n, 0)
