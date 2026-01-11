from operator import itemgetter, attrgetter
import math
INF=0x3f3f3f3f
def dis(a,b):	#求两个点之间的距离
    return math.sqrt(float(a[0]-b[0])*(a[0]-b[0])+float(a[1]-b[1])*(a[1]-b[1]))

def mindistance(p,l,r):							#求p[l..r]中不同组点之间的最小距离
    if l>=r:return INF							#区间为空或者只有一个点返回
    if l+1==r:return dis(p[l],p[r])				#区间中只有两个点
    mid=(l+r)//2     #求中点位置
    d1=mindistance(p,l,mid)
    d2=mindistance(p,mid+1,r)
    d=min(d1,d2)
    c=[]
    for i in range(l,r+1):							#与中点x方向距离<d的点存放在p1中
        if abs(p[i][0]-p[mid][0])<d:c.append(p[i])
    c.sort(key=itemgetter(1))              #p1中所有点按y递增排序
    for i in range(0,len(c)):
        j,k=i+1,0
        while k<7 and j<len(c) and c[j][1]-c[i][1]<d:
            d=min(d,dis(c[i],c[j]))
            j,k=j+1,k+1
    return d

p=[[1,1],[8,1],[9,4],[5,4],[8,7],[5,6],[7,10],[3,5],[3,7],[4,10],[1,6],[0,3]]
#p=[[1,1],[1,3],[5,0],[5,2],[6,2],[6,4],[8,1],[9,2]]
print(p)
p.sort(key=itemgetter(0))
print(len(p))
print(p)
print("ans=",mindistance(p,0,len(p)-1))