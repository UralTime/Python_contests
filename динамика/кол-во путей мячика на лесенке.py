ways = [0] * 35
n = int(input())
ways[n] = 1
for i in range(n - 1, -1, -1):
    ways[i] = ways[i + 1] + ways[i + 2] + ways[i + 3]
print(ways[0])
