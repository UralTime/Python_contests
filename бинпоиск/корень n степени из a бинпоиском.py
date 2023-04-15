# корень n-ой степени из введённого числа
def fastpow(x, y):
    res = 1
    for i in range(y):
        res *= x
    return res


a = float(input())
n = int(input())
l = 0
r = max(1, a)
for i in range(100):
    c = (l + r) / 2
    if a >= 1 and c > a:
        r = c
    else:
        if fastpow(c, n) > a:
            r = c
        else:
            l = c
print(r)
