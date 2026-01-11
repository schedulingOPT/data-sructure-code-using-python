from collections import deque
MAXN=100
INF=0x3f3f3f3f
def bfs(s):	            #求解算法
    global A,n,dist,prev,sum
    dist=[INF]*n        #dist初始化所有元素为INF
    prev=[-1]*n         #prev初始化所有元素为-1
    dist[s]=0
    qu=deque()   #定义一个队列qu
    qu.append(s)                #源点结点进队
    while qu:				#队列不空循环
        u=qu.popleft()	        #出队顶点u
        sum+=1
        #print("(%d)出队%d,dist[%d]=%d"%(sum,u,u,dist[u])) 
        for edj in A[u]:
            v,w=edj[0],edj[1]          #相邻顶点为v
            #print("  考虑相邻点%d  "%(v))
            if dist[u]+w<dist[v]:	#剪支：u到v有边且路径长度更短
                dist[v]=dist[u]+w
                #print("[%d,%d]:%d 修改dist[%d]=%d  "%(u,v,w,v,dist[v]))
                prev[v]=u
                #print(" 扩展%d,dist=%d\n"%(v,dist[v]))	
                qu.append(v)				#顶点v进队
                #print("进队")
            #else:print("没有修改") 

def dispapath(s,i):		#输出s到i的一条最短路径
    global A,dist,prev
    path=[]
    if s==i:return;
    if dist[i]==INF:
        print("  源点%d到顶点%d没有路径"%(s,i))
    else:
        path.append(i)		            #添加目标顶点
        k=prev[i]
        while k!=s:			        #添加中间顶点
            path.append(k)
            k=prev[k]
        path.append(s)		            #添加源点
        print("  源点%d到顶点%d的最短路径长度: %d, 路径: "%(s,i,dist[i]),end='')
        for j in range(len(path)-1,-1,-1):	#反向输出构成正向路径
            print(path[j],end= ' ')
        print()

def solve(A,n,s):		    #求源点v出发的所有最短路径
    global sum
    sum=0
    bfs(s)
    print("求解结果")
    for i in range(0,n):dispapath(s,i)
    print("sum=",sum)

A=[[[2,10],[4,30],[5,100]],[[2,4]],[[3,50]],[[5,10]],[[3,20],[5,60]],[]]
n=6
s=0
solve(A,n,s)
