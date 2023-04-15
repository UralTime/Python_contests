n = int(input())
a = [int(elem) for elem in input().split()]
a.sort()
ves1 = a[0]
if n==1:
    print('NO')
else:
    ves2 = a[1]
