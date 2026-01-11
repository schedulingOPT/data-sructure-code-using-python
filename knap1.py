import copy
from collections import deque
class Goods:							     #物品类 
    def __init__(self,x,y,z):
        self.no=x						    #物品的编号
        self.w=y							#物品的重量
        self.v=z							#物品的价值
    def __lt__(self,other):	    		    #用于按v/w递减排序
        return 1.0*self.v/self.w>=1.0*other.v/other.w

class QNode:				    #队列中结点类型
    def __init__(self):
        self.i=0            #当前层次(物品序号) 
        self.cw=0          #当前总重量
        self.cv=0			#当前总价值
        self.x=[]			#当前解向量
        self.ub=0.0		    #上界
def bound(e):					#求结点e的上界函数值
    global g,n,W
    rw=W-e.cw												#背包的剩余容量
    b=e.cv												#表示物品价值的上界值
    j=e.i
    while j<n and g[j].w<=rw:
        rw-=g[j].w												#选择物品j
        b+=g[j].v													#累计价值
        j+=1
    if j<n:															#最后物品只能部分装入
        b+=1.0*g[j].v/g[j].w*rw
    e.ub=b

def EnQueue(e,qu):		#结点e进队操作
    global n,bestv,bestx,bestw
    if e.i==n:							#到达叶子结点
        if e.cv>bestv:					#比较更新最优解
            bestv=e.cv
            bestx=copy.deepcopy(e.x) 
            bestw=e.cw
    else:qu.append(e)					#非叶子结点进队

def bfs():				#求0/1背包最优解的算法
    global g,n,W,bextx,bestw,sum
    qu=deque()	#定义一个队列
    e=QNode()
    e.i,e.cw,e.cv=0,0,0           #根结点层次为0
    e.x=[-1]*n
    qu.append(e)					#根结点进队
    while qu:						#队不空循环
        e=qu.popleft()		        #出队结点e
        sum+=1
        if e.cw+g[e.i].w<=W:			#左剪支
            e1=QNode()
            e1.cw=e.cw+g[e.i].w					#选择物品e.i
            e1.cv=e.cv+g[e.i].v
            e1.x=copy.deepcopy(e.x); e1.x[e.i]=1
            e1.i=e.i+1							#左子结点的层次加1
            EnQueue(e1,qu)
        e2=QNode()
        e2.cw,e2.cv=e.cw,e.cv				#不选择物品e.i
        e2.x=copy.deepcopy(e.x); e2.x[e.i]=0
        e2.i=e.i+1							#右子结点的层次加1
        bound(e2);							#求出不选择物品i的价值上界
        if e2.ub>bestv:						#右剪支
            EnQueue(e2,qu)
def knap(g,n,W):					#求0/1背包问题
    global bestx,bestv,bestw,sum
    g.sort()			#按v/w递减排序
    bestx=[-1]*n	      #存放最优解向量
    bestv=0			    #存放最大价值,初始为0
    bestw=0              #最优解总重量
    sum=0				                #累计搜索的结点个数 
    bfs();				                    #i从0开始
    print("求解结果")
    for i in range(0,n):
        if bestx[i]==1:print("  选取第%d个物品"%(g[i].no))
    print("  总重量=%d,总价值=%d"%(bestw,bestv))
    print("sum=",sum)


g=[Goods(0,5,4),Goods(1,3,4),Goods(2,2,3),Goods(3,1,1)]
n=4
W=6
knap(g,n,W)
