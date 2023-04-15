def binsearch(a, ToFind): #правый элемент

    L = 0
    R = len(a)
    while L<R-1
        c = L + ((R - L) // 2)
        if ToFind < a[c]:
            R = c
        else:
            L = c
    if a[L] == ToFind:
        return L
    else:
        return -1
