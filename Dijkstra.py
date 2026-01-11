INF=0x3f3f3f3f
def Dijkstra(A,n,v):	#Dijkstra算法
    global dist
    dist=[0]*n
    S=[False]*n
    for i in range(0,n):
        dist[i]=A[v][i]							#距离初始化
    S[v]=True									#源点v放入S中
    for i in range(0,n-1):						#循环n-1次
        u,mindis=-1,INF
        for j in range(0,n):				#选取U中具有最小距离的顶点u
            if not S[j] and dist[j]<mindis:
                u=j
                mindis=dist[j]
        if u==-1:break 
        S[u]=True							#顶点u加入S中
        for j in range(0,n):				#修改U中的顶点的距离
            if not S[j] and A[u][j]!=0 and A[u][j]<INF:
                dist[j]=min(dist[j],dist[u]+A[u][j])
def solve(A,n,v):
    Dijkstra(A,n,v)
    print("顶点%d出发的最短路径长度"%(v))
    for i in range(0,n):
        if i!=v:print("  顶点%d到顶点%d的最短路径长度=%d"%(v,i,dist[i]))

A=[			         #一个带权有向图
[0,4,6,6,INF,INF,INF],[INF,0,1,INF,7,INF,INF],
[INF,INF,0,INF,6,4,INF],[INF,INF,2,0,INF,5,INF],
[INF,INF,INF,INF,0,INF,6],[INF,INF,INF,INF,1,0,8],
[INF,INF,INF,INF,INF,INF,0]]
n=7
v=0

solve(A,n,v)
