n, k = map(int, input().split())
a = [int(elem) for elem in input().split()]
l = 0
r = a[-1] - a[0]
while r - l > 1:
    d = (l + r) // 2
    cows_success = 1
    j = 0
    for i in range(1, len(a)):
        if a[i] - a[j] >= d:
            j = i
            cows_success += 1
    if cows_success >= k:
        l = d
    else:
        r = d
if k == 2:
    l += 1
print(l)
