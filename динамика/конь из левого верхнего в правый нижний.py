n, m = map(int, input().split())
d = [[0] * (m + 1) for i in range(n + 1)]
d[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, m + 1):
        d[i][j] = d[i - 2][j - 1] + d[i - 1][j - 2]
print(d[n][m])
