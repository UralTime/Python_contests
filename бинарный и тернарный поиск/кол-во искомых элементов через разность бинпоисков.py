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
    if right < len(a) and a[right] == toFind:
        return right
    else:
        return 0


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
    if a[left_1] == toFind:
        return left_1
    else:
        return -1


n = int(input())
a = [int(elem) for elem in input().split()]
a.sort()
m = int(input())
for elem in input().split():
    print(binsearch_right(a, int(elem)) - binsearch_left(a, int(elem)) + 1, end=' ')
