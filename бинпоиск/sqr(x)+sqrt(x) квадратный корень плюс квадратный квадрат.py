def binsearch(toFind):
    L = 0
    R = toFind
    for i in range(100):
        c = (L + R) / 2
        if c > toFind:
            R = c
        else:
            if c * c > toFind:
                R = c
            else:
                L = c
    return L


q = float(input())
l = 1
r = 10 ** 10
for i in range(100):
    x = (l + r) / 2
    if x * x + binsearch(x) > q:
        r = x
    else:
        l = x
print(x)
