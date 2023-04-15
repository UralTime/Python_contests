n, m = map(int, input().split())
v = [0] + [int(elem) for elem in input().split()]
c = [0] + [int(elem) for elem in input().split()]
d = [[-10 ** 10] * (m + 1) for i in range(n + 1)]
prev = [[-10 ** 10] * (m + 1) for i in range(n + 1)]
for i in range(n + 1):
    d[i][0] = 0
    prev[i][0] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j - v[i] >= 0:
            d[i][j] = max(d[i - 1][j - v[i]] + c[i], d[i - 1][j])
            if d[i][j] == d[i - 1][j - v[i]] + c[i]:
                prev[i][j] = i - 1, j - v[i]
            else:
                prev[i][j] = i - 1, j
        else:
            d[i][j] = d[i - 1][j]
            prev[i][j] = i - 1, j
j = d[n].index(max(d[n]))
while j > 0:
    t, k = prev[n][j]
    if t == n - 1 and k != j:
        print(n)
    n, j = t, k
