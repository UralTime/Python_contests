def rasst(time,pointx,pointy,otrezokx1,otrezoky1,otrezokx2,otrezoky2):
    x1 += vx1*time
    x2 += vx1*time
    y1 += vy1*time
    y2 += vy1*time
    x3 += vx2*time
    x4 += vx2*time
    y3 += vy2*time
    y4 += vy2*time
    s = (pointx-)
    return
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
vx1, vy1 = map(int, input().split())
vx2, vy2 = map(int, input().split())
l = 0
r = 10000
ans = []
for i in range(100):
    d = (r-l)/3
    if rasst(d,x1,y1,x3,y3,x4,y4)>rasst(d,x1,y1,x3,y3,x4,y4):
        l += d
    else:
        r -= d
if int(rasst(l,x1,x3x4))==0:
    ans.append(l)
if ans==[]:
    print(-1)
else:
    print(min(ans))
