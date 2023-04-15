n = int(input())
x = [0] * n
v = [0] * n
for i in range(n):
    x[i], v[i] = map(int, input().split())
l = 0
r = 2 * max(x)
for i in range(300):
    m = (r + l) / 2
    xx = [0] * n
    for i in range(n):
        xx[i] = x[i] + v[i] * m
    if v[xx.index(min(xx))] > v[xx.index(max(xx))]:
        l = m
    else:
        r = m
print(l, max(xx) - min(xx))
