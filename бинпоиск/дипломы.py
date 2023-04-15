w, h, n = map(int, input().split())
width, height, wPieces, hPieces = w, h, 1, 1
n -= 1
while n > 0:
    if height + h < width + w:
        height += h
        hPieces += 1
        n -= wPieces
    else:
        width += w
        wPieces += 1
        n -= hPieces
print(max(width, height))

# решение задачи бинпоиском по ответу
# w, h, n = map(int, input().split())
# l=0
# r=10**18 + 1
# while r-l>1:
#     if (a//w) * (a//h) >= n:
#         l = a
#     else:
#         r =a
# print(l)