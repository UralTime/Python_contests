def lagr(n,k):
    sq = n ** 0.5

    while n > 0:
        n1 = n
        sq = n ** 0.5
        while int(sq) != sq:
            n1 -= 1
            #ost += 1
            sq = n1 ** 0.5
        print(int(sq), end=' ')
        n -= n1
        #ost = 0
    print()
n = int(input())
lagr(n,0)
