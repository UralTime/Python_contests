n, m = map(int, input().split())
v = [0] + [int(elem) for elem in input().split()]
d = [[-10 ** 10] * (m + 1) for i in range(n + 1)]
for i in range(n + 1):
    d[i][0] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j - v[i] >= 0:
            d[i][j] = max(d[i - 1][j - v[i]] + v[i], d[i - 1][j])
        else:
            d[i][j] = d[i - 1][j]
if max(d[n]) == m:
    print('YES')
else:
    print('NO')