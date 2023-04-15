n = int(input())
i = 1
ans = False
while i<=111111111111111111111111111111111111111111111111111:
    if i%n==0:
        print(i)
        ans = True
        break
    i*=10
    i+=1
if not ans:
    print("NO")