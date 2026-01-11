from collections import deque
MAXN=100
INF=0x3f3f3f3f
def bfs(s,t):	           #求解算法
    global A,n
    dist=[INF]*n             #dist初始化所有元素为INF
    dist[s]=0
    qu=deque()   #定义一个 队列qu
    qu.append(s)                      #源点结点进队
    while qu:				#队列不空循环
        u=qu.popleft()		        #出队顶点u
        #print("u=",u)
        for edj in A[u]:
            v,w=edj[0],edj[1]         #相邻顶点为v
            if dist[u]+w<dist[v]:	#剪支：u到v有边且路径长度更短
                dist[v]=dist[u]+w
                qu.append(v)				#顶点v进队
    return dist[t]

def solve(A,n,s,t):		    #求s->t的最短路径长度
    ans=bfs(s,t)
    if ans==INF:
        print("%d到%d没有路径"%(s,t))
    else:
        print("%d到%d的最短路径长度=%d"%(s,t,ans))

print("实例1")
A=[[[2,10],[4,30],[5,100]],[[2,4]],[[3,50]],[[5,10]],[[3,20],[5,60]],[]]
n=6
s=0
for t in range(0,n):
    if t!=s:solve(A,n,s,t)

print("实例2")
A=[[[1,5],[2,4]], [[2,3],[3,1]],[[1,-2]],[]]
n=4
s=0
for t in range(0,n):
    if t!=s:solve(A,n,s,t)
