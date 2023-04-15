n = int(input())
d = [[0] * (n + 2) for i in range(n + 2)]
for i in range(n + 2):
    d[i][0] = 1
for fromLev in range(1, n + 2):
    for j in range(1, n + 1):
        lev = 1
        while j - lev >= 0 and lev < fromLev:
            d[fromLev][j] += d[lev][j - lev]
            lev += 1
print(d[n + 1][n])
