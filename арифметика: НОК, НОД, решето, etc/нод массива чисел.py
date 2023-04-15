def NOD(a, b):
    if b > 0:
        return NOD(b, a % b)
    else:
        return a


n = int(input())
a = [int(elem) for elem in input().split()]
nodd = 0
for elem in a:
    nodd = NOD(nodd, elem)
print(nodd)
