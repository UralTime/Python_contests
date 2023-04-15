def NOD(a, b):
    if b > 0:
        return NOD(b, a % b)
    else:
        return a


x1, y1, x2, y2 = map(int, input().split())
xx = abs(x2 - x1)
yy = abs(y2 - y1)
print(NOD(xx, yy) + 1)
