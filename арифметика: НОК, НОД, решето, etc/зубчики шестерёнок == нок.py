def NOD(a, b):
    if b > 0:
        return NOD(b, a % b)
    else:
        return a


n, k = map(int, input().split())
print(n * k // NOD(n, k))
