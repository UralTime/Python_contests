def NOD(a, b):
    if b > 0:
        return NOD(b, a % b)
    else:
        return a
# NOK = a * b // NOD(a,b)