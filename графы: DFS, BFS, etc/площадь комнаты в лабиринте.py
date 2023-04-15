def roomdfs(i, j):
    sum = 1
    used[i][j] = True
    for t in range(4):
        u = i + k[t]
        v = j + l[t]
        if not used[u][v] and g[v][u] != '*':
            sum += roomdfs(u, v)
    return sum


n = int(input())
g = ['*' * (n + 2)] + ['*' + input() + '*' for i in range(n)] + ['*' * (n + 2)]
used = [[False] * (n + 2) for i in range(n + 2)]
i, j = map(int, input().split())
k = [0, 0, -1, 1]
l = [-1, 1, 0, 0]
square = roomdfs(i, j)
print(square)
