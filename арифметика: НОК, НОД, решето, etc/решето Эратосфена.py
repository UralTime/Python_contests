def Resheto(N):  # N-проверяемое на простоту число
    a = [True] * (N + 1)
    a[0], a[1], a[2] = [False, False, True]
    for p in range(4, N + 1, 2):
        a[p] = False
    p = 3
    while p ** 2 <= N:
        k = p ** 2
        if a[p]:
            for i in range(k, N + 1, p):
                a[i] = False
        p += 2
    for k in range(2,N+1):
        print(k,'-', 'простое' if a[k] else 'составное')
# в массиве a[i]==True, если число простое; False - если составное
# 0 и 1 не простые и не составные ;)

Resheto(100)

#ассимптотика N*loglogN, почти линия