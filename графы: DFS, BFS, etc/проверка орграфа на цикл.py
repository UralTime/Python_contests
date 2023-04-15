def dfs(v, parents):
    global cycle
    global used
    global color
    used[v] = True
    color[v] = 1
    for u in range(n):
        if g[v][u] == 1:
            color[v] = 2
            if not used[u]:
                dfs(u, parents + [v])
            else:
                if u in parents and color[u] == 2:
                    cycle = 1


n = int(input())
g = [[int(elem) for elem in input().split()] for i in range(n)]
color = [0] * n
used = [False] * n
cycle = 0
for i in range(n):
    if not used[i]:
        dfs(i, [])
print(cycle)
