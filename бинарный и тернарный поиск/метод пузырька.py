def puzyr(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
