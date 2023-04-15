n = int(input())
INF = 10**9
dp=[INF]*(n+1)
pr=[0]*(n+1)
dp[1]=0
for i in range(1,n):
    if i*3<=n:
        if dp[i]+1<dp[i*3]:
            dp[i*3]=dp[i]+1
            pr[i*3]=i
    if i*2<=n:
        if dp[i]+1<dp[i*2]:
            dp[i*2]=dp[i]+1
            pr[i*2]=i
    if dp[i]+1<dp[i+1]:
        dp[i+1]=dp[i]+1
        pr[i+1]=i
print(dp[n])
path=[]
while n!=0:
    path.append(n)
    n=pr[n]
path = path[::-1]
for elem in path:
   print(elem,end=' ')
# for i in range(1,len(path)):
#     if path[i]==path[i-1]*3:
#         print(3,end='')
#     elif path[i]==path[i-1]*2:
#         print(2,end='')
#     else:
#         print(1,end='')