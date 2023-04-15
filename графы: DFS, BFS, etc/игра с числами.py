from collections import deque

l = int(input())
r = int(input())
predok = [-1] * 10000
predok[l] = 0
q = deque()
q.append(l)
x = l
while x != r:
    x = q.popleft()
    if x < 9000:
        if predok[x + 1000] == -1:
            q.append(x + 1000)
            predok[x + 1000] = x
    if x % 10 != 1:
        if predok[x - 1] == -1:
            q.append(x - 1)
            predok[x - 1] = x
    s = str(x)
    a = int(s[3] + s[:3])
    if predok[a] == -1:
        q.append(a)
        predok[a] = x
    b = int(s[1:] + s[0])
    if predok[b] == -1:
        q.append(b)
        predok[b] = x
path = []
while x != l:
    path.append(str(x))
    x = predok[x]
path.append(str(x))
print('\n'.join(path[::-1]))
