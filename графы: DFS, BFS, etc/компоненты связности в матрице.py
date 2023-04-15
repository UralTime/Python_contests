from sys import setrecursionlimit

setrecursionlimit(1000000)


def dfskuska(i, j):
    global used
    used[i][j] = True
    for u, v in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
        if 0 <= u < m and 0 <= v < n:
            if not used[u][v] and g[u][v] != '.':
                dfskuska(u, v)


m, n = map(int, input().split())
g = [input() for i in range(m)]
used = [[False for j in range(n)] for i in range(m)]
peaces = 0
for i in range(m):
    for j in range(n):
        if not used[i][j] and g[i][j] != '.':
            peaces += 1
            dfskuska(i, j)
print(peaces)
