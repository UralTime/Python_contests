n, a, b, w, h = map(int, input().split())
l = 0
r = min(w, h) + 1
while r - l > 1:
    d = (l + r) // 2
    if (w // (a + 2 * d)) * (h // (b + 2 * d)) >= n or (h // (a + 2 * d)) * (w // (b + 2 * d)) >= n:
        l = d
    else:
        r = d
print(l)