def trees(days):
    res = days * (a + b) - a * (days // k) - b * (days // m)
    return res

[a, k, b, m, x] = [int(elem) for elem in input().split()]
l = 0
r = 10 ** 20
while r - l > 1:
    day = (l + r) // 2
    if trees(day) < x:
        l = day
    else:
        r = day
print(r)
