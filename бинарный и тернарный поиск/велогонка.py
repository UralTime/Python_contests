def rasst(t):
    xx = [0] * n
    for i in range(n):
        xx[i] = x[i] + v[i] * t
    return max(xx) - min(xx)


n = int(input())
x = [0] * n
v = [0] * n
for i in range(n):
    x[i], v[i] = map(int, input().split())
l = 0
r = 10 ** 8
for i in range(100):
    t = (r - l) / 3
    if rasst(l + t) > rasst(r - t):
        l += t
    else:
        r -= t
print(round(l, 7), rasst(round(l, 6)))
