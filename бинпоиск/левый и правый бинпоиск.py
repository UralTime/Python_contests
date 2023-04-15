def binsearch_left(a, toFind):
    left = -1
    right = len(a)
    # левый бинпоиск, который ищет левую границу
    while right - left > 1:
        middle = (right + left) // 2
        if a[middle] < toFind:
            left = middle
        else:
            right = middle
    return (left, right)


def binsearch_right(a, toFind):
    left_1 = -1
    right_1 = len(a)
    # правый бинпоиск, который ищет правый границу
    while right_1 - left_1 > 1:
        middle = (right_1 + left_1) // 2
        if a[middle] <= toFind:
            left_1 = middle
        else:
            right_1 = middle
    return (left_1, right_1)


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for elem in b:
    first, second = binsearch_left(a, elem)
    first1, second1 = binsearch_right(a, elem)
    if first == first1 and second == second1:
        print(0)
    else:
        print(second + 1, first1 + 1)
#есть левый бинпоиск(x)
#правый - это левый бинпоиск(x)-1