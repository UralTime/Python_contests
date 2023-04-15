for n in range(10**6,10**5,-1):
    q = [0, 0, 1, 1] + [1000] * (n - 3)
    predok = [0, 1, 1, 1] + [0] * (n - 3)
    predok[2] = 1
    predok[3] = 1
    for i in range(4, n + 1):
        if i % 3 == 0:
            if i % 2 == 0:
                q[i] = min(q[i // 3], q[i // 2], q[i - 1]) + 1
                if min(q[i // 3], q[i // 2], q[i - 1]) == q[i // 3]:
                    predok[i] = i // 3
                elif min(q[i // 3], q[i // 2], q[i - 1]) == q[i // 2]:
                    predok[i] = i // 2
                else:
                    predok[i] = i - 1
            else:
                q[i] = min(q[i // 3], q[i - 1]) + 1
                if q[i // 3] < q[i - 1]:
                    predok[i] = i // 3
                else:
                    predok[i] = i - 1
        elif i % 2 == 0:
            q[i] = min(q[i // 2], q[i - 1]) + 1
            if q[i // 2] < q[i - 1]:
                predok[i] = i // 2
            else:
                predok[i] = i - 1
        else:
            q[i] = q[i - 1] + 1
            predok[i] = i - 1
    path = []
    j = n
    while j > 1:
        if predok[j] * 3 == j:
            path.append('3')
        elif predok[j] * 2 == j:
            path.append('2')
        else:
            path.append('1')
        j = predok[j]
    #print(''.join([str(elem) for elem in path[::-1]]))
    print(n)