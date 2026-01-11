import copy
import heapq
class QNode:					#优先队列结点类
    def __init__(self):
        self.i=0			    #人员编号
        self.cost=0				#已经分配任务所需要的成本
        self.x=[]				#当前解向量
        self.used=[]			#used[i]为真表示任务i已经分配
        self.lb=0				#下界
    def __lt__(self,other):	    #按lb越小越优先出队
        return self.lb<other.lb
INF=0x3f3f3f3f
def bound(e):			#求结点e的下界值	
    global n,used,c
    minsum=0
    for i1 in range(e.i,n):	#求c[e.i..n-1]行中最小元素和
        minc=INF
        for j1 in range(0,n):
            if not e.used[j1] and c[i1][j1]<minc:minc=c[i1][j1]
        minsum+=minc
    e.lb=e.cost+minsum

def EnQueue(e,pqu):		#结点e进队操作
    global n,bestx,bestc
    if e.i==n:				#到达叶子结点
        if e.cost<bestc:				#比较更新最优解
            bestc=e.cost
            bestx=copy.deepcopy(e.x)
    else:heapq.heappush(pqu,e)			#非叶子结点进队
  
def bfs():					#求解任务分配
    global c,n,bextx,bestc,sum
    pqu=[]                    #定义一个优先队列pqu
    e=QNode()
    e.i,e.cost=0,0           #根结点层次为0
    e.x=[-1]*n
    e.used=[False]*n
    bound(e)
    heapq.heappush(pqu,e)			#源点结点进队
    while pqu:						#队不空循环
        e=heapq.heappop(pqu)	        #出队结点e
        sum+=1
        for j in range(0,n):			#共n个任务
            if e.used[j]:continue		#任务j已分配时跳过
            e1=QNode()
            e1.i=e.i+1						#子结点的层次加1
            e1.cost=e.cost+c[e.i][j]
            e1.x=copy.deepcopy(e.x);e1.x[e.i]=j	#为人员e.i分配任务j
            e1.used=copy.deepcopy(e.used);e1.used[j]=True				#标志任务j已经分配
            bound(e1)						#求e1的lb
            if e1.lb<bestc:			#剪支 
                EnQueue(e1,pqu)

def allocate(c,n):     #求解任务分配问题
    global bestx,bestc,sum 
    sum=0								#累计搜索结点个数
    bestx=[-1]*n	      #最优解向量 
    bestc=INF					  #最优解的成本
    bfs()
    print("求解结果");
    for k in range(0,n):
        print("   人员%d分配任务%d"%(k,bestx[k]))
    print("   总成本=%d"%(bestc))
    print("sum=",sum)

n=4
c=[[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
allocate(c,n)
