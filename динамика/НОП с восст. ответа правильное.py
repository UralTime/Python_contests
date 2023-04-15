n = int(input())
a=[0]
for elem in input().split():
    a.append(int(elem))
m = int(input())
b=[0]
for elem in input().split():
    b.append(int(elem))
d = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i] == b[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i][j - 1], d[i - 1][j])
ans = []
i = n
j = m
while d[i][j]>0:
    while d[i][j-1]==d[i][j]:
        j -= 1
    while d[i-1][j]==d[i][j]:
        i -= 1
    ans.append(str(a[i]))
    i -= 1
    j -= 1
print(' '.join(ans[::-1]))
