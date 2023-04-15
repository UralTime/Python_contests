def dfs(v, pr):
    used[v]=True
    for i in range(len(g[v])):
        u = g[v][i]
        if not used[u]:
            dfs(u)

n=int(input()) #n-количество вершин в графе
used=[False]*(n)
count=0 #count вернёт количество компонентов связности в графе
for i in range(n):
    if not used[i]:
        dfs(i, -1)
        count += 1

