def Resheto(N):
    a = [True] * (N + 1)
    a[0], a[1], a[2] = [False, False, True]
    i = 2
    while i*i <= N:
        if a[i]:
            for j in range(i*i, N + 1, i):
                a[j] = False
        i+=1
    for k in range(2,N+1):
        print(k,'-', 'простое' if a[k] else 'составное')

Resheto(100)