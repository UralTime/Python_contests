def S(h):
    a1 = (y1 - yc) / (x1 - xc)
    b1 = yc - a1 * xc
    xl = (h - b1) / a1
    a2 = (y2 - yc) / (x2 - xc)
    b2 = yc - a2 * xc
    xr = (h - b2) / a2
    return h * (xr - xl)


xc, yc = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
l = min(y1, y2)
r = yc
for i in range(150):
    d = (r - l) / 3
    if S(l + d) < S(l + 2 * d):
        l = l + d  # l+=d
    else:
        r = l + 2 * d  # r-=d
print(S(l))
