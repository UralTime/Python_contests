n, x, y = map(int, input().split())
min1 = min(x, y)
if n == 1:
    print(min1)
else:
    left = 0
    right = n * (x + y - min1 + 1)
    while right - left > 1:
        middle  = (right + left) // 2
        if n - 1 <= middle // x + middle // y:
            right = middle
        else:
            left = middle
    print(min1 + left + 1)