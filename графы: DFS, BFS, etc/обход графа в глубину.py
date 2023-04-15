def dfs(v):
    global used
    used[v] = True
    for i in range(n):
        u = g[v][i]
        if u == 1 and not used[i]:
            dfs(i)


n, ver = map(int, input().split())
g = [[int(elem) for elem in input().split()] for i in range(n)]
used = [False] * n
dfs(ver)
print(used.count(True))
