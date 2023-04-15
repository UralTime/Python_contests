def nextSteps(fromLevel, n):
    # if n<0:
    #     return 0
    if n == 0:
        return 1
    cnt = 0
    lev = 1
    while n - lev >= 0 and lev<fromLevel:
    #for lev in range(1, fromLevel):
        # if n - lev < 0:
        #     break
        cnt = cnt + nextSteps(lev, n - lev)
        lev += 1
    return cnt


for i in range(1, 51):
    print(nextSteps(i+1, i), end = ',')
