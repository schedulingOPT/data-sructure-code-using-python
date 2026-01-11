import heapq
class QNode:					            #优先队列结点类
    def __init__(self,vno,length):        #构造方法
        self.vno=vno		      			#顶点编号
        self.length=length		  			#路径长度
    def __lt__(self,other):	    		    ##按length越小越优先出队
        return self.length<other.length

def bfs(s,t):	           #求解算法
    global A,n
    pqu=[]                    #定义一个优先队列pqu
    heapq.heappush(pqu,QNode(s,0))			#源点结点进队
    while pqu:				#队列不空循环
        e=heapq.heappop(pqu)	        #出队结点e
        u=e.vno
        #print("出队顶点%d,e.length=%d"%(u,e.length))
        if u==t:return e.length
        for edj in A[u]:
            v,w=edj[0],edj[1]         #相邻顶点为v
            e1=QNode(v,e.length+w)     #建立相邻点的结点e1
            #print("   扩展顶点%d,e1.length=%d"%(v,e1.length))
            heapq.heappush(pqu,e1)				#顶点v进队
            #print("进队")
    return -1                    #表示没有找到顶点t

def solve(A,n,s,t):		    #求s->t的最短路径长度
    ans=bfs(s,t)
    if ans==-1:print("%d到%d没有路径"%(s,t))
    else:print("%d到%d的最短路径长度=%d"%(s,t,ans))

A=[[[2,10],[4,30],[5,100]],[[2,4]],[[3,50]],[[5,10]],[[3,20],[5,60]],[]]
n=6
s=0
for t in range(0,n):
    if t!=s:solve(A,n,s,t)