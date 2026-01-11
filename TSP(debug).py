import copy
import heapq
class QNode:					#优先队列结点类
    def __init__(self):
        self.i=0;			    #解空间的层次 
        self.vno=0				#当前顶点
        self.used=0             #用于路径中顶点判重
        self.length=0           #当前路径长度
    def __lt__(self,other):	    #按length越小越优先出队
        return self.length<other.length
INF=0x3f3f3f3f

def inset(used,j):	#判断顶点j是否在used中
    return (used&(1<<j))!=0;

def addj(used,j):			#在used中添加顶点j
    return used|(1<<j);

def bfs(s):						#优先队列式分支限界算法
    global A,n,bestd
    pqu=[]                    #定义一个优先队列pqu
    e=QNode()
    e.i,e.vno=0,s                       #根结点层次为0
    e.used,e.length=0,0
    e.used=addj(e.used,s)				#表示顶点s已经访问
    heapq.heappush(pqu,e)			    #源点结点进队
    while pqu:						    #队不空循环
        e=heapq.heappop(pqu)	        #出队结点e
        print("出队[%d,%d,%d],used=%d"%(e.i,e.vno,e.length,e.used))
        for j in range(0,n):
            if inset(e.used,j):continue     #顶点j在路径中时跳过
            e1=QNode()
            e1.i=e.i+1						        #扩展下一层 
            e1.vno=j							    #e1.i层选择顶点j
            e1.used=addj(e.used,j)					#添加已访问的顶点j
            e1.length=e.length+A[e.vno][e1.vno]	    #累计路径长度
            print("    扩展[%d,%d,%d],used=%d"%(e1.i,e1.vno,e1.length,e1.used))
            if e1.i==n-1:						    #e1为叶子结点
                bestd[e1.vno]=min(bestd[e1.vno],e1.length)			
            if e1.i<n-1:						    #e1为非叶子结点
                if e1.length<bestd[e1.vno]: 		#剪支
                    heapq.heappush(pqu,e1)			#非叶子结点进队
                    print("        进队")

def TSP(A,n,s):			#求解TSP(起始点为s)
    global bestd
    bestd=[INF]*n         #初始化bestd所有元素为∞
    bestd[s]=0
    bfs(s)
    for i in range(0,n):
        print("bestd[%d]=%d"%(i,bestd[i]))
    ans=INF
    for i in range(0,n):
        if i!=s:ans=min(ans,bestd[i]+A[i][s])
    print("以%d为起点的最短路径长度=%d"%(s,ans))

A=[[0,8,5,36],[6,0,8,5],[8,9,0,5],[7,7,8,0]]
n=4
s=1
TSP(A,n,s)
