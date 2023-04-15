import random


def qsort(a, nStart, nEnd):  # по возрастанию
    if nStart >= nEnd:
        return
    else:
        L = nStart
        R = nEnd
        x = random.choice(a[L:R + 1])  # a[(L + R) // 2]
        while L <= R:
            while a[L] < x:
                L += 1
            while a[R] > x:
                R -= 1
            if L <= R:
                # if a[L] > a[R]:
                a[L], a[R] = a[R], a[L]
                L += 1
                R -= 1
        if nStart < R:
            qsort(a, nStart, R)
        if L < nEnd:
            qsort(a, L, nEnd)
# nStart=0
# nEnd=len(a)-1
