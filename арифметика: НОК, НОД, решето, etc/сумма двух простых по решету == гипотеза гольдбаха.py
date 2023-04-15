def Resheto(n):
    global b
    b = set()
    a = [True] * (n + 1)
    a[0], a[1], a[2] = [False, False, True]
    i = 2
    while i * i <= n:
        if a[i]:
            for j in range(i * i, n + 1, i):
                a[j] = False
        i += 1
    for k in range(2, n + 1):
        if a[k]:
            b.add(k)


n = int(input())
Resheto(n)
for elem in b:
    if n - elem in b:
        print(elem, n - elem)
        break
