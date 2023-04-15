def NOD(a, b):
    if b > 0:
        return NOD(b, a % b)
    else:
        return a


a, b, c, d = map(int, input().split())
nok = b * d // NOD(max(b, d), min(b, d))
chisl = a * (nok // b) + c * (nok // d)
q = NOD(max(nok, chisl), min(nok, chisl))
print(chisl // q, nok // q)
