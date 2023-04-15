import math


def time(x):
    s1 = math.sqrt((x ** 2 + (1 - a) ** 2))
    time1 = s1 / vp
    s2 = math.sqrt((a ** 2 + (1 - x) ** 2))
    time2 = s2 / vf
    return time1 + time2


vp, vf = map(int, input().split())
a = float(input())
l = 0
r = 1
for i in range(200):
    d = (r - l) / 3
    if time(l + d) > time(l + d * 2):
        l += d
    else:
        r = l + 2 * d
print(l)
