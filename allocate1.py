import copy
INF=0x3f3f3f3f                #表示∞
def dfs1(cost,i):			#回溯算法
    global c,n,x,bestx,bestc,used,sum
    sum+=1 
    if i>=n:			            #到达一个叶子结点
        if cost<bestc:		        #比较求最优解
            bestc=cost
            bestx=copy.deepcopy(x)
    else:
        for j in range(0,n):	#为人员i试探任务j:0到n-1
            if used[j]:continue			#跳过已经分配的任务j
            used[j]=True
            x[i]=j					      #任务j分配给人员i
            cost+=c[i][j]
            dfs1(cost,i+1)			  #为人员i+1分配任务
            used[j]=False				#回退
            x[i]=-1
            cost-=c[i][j]

def allocate1(c1,n1):     #求解任务分配问题
    global c,n,x,bestx,bestc,used,sum
    c,n=c1,n1
    x=[0]*n
    bestx=[0]*n
    bestc=INF                           #初始化为∞
    used=[False]*n
    sum=0
    dfs1(0,0);							#从人员0开始
    print("求解结果")
    for k in range(0,n):
        print("   人员%d分配任务%d"%(k,bestx[k]))
    print("   总成本=",bestc)
    print("sum=",sum)


def bound(cost,i):								#求下界算法
    global c,n,used
    minsum=0
    for i1 in range(i,n):				#求c[i..n-1]行中未分配的最小成本和
        minc=INF										#置为∞
        for j1 in range(0,n):
            if not used[j1] and c[i1][j1]<minc:minc=c[i1][j1]
        minsum+=minc
    return cost+minsum

def dfs2(cost,i):		#回溯算法
    global c,n,x,bestx,bestc,used,sum
    sum+=1 
    if i>=n:			            #到达一个叶子结点
        if cost<bestc:		        #比较求最优解
            bestc=cost;bestx=copy.deepcopy(x)
    else:
        for j in range(0,n):	#为人员i试探任务j:0到n-1
            if used[j]:continue						#跳过已经分配的任务j
            used[j]=True
            x[i]=j					      #任务j分配给人员i
            cost+=c[i][j]
            if bound(cost,i+1)<bestc:			#剪支(考虑c[i+1..n-1]的行中最小成本)
                dfs2(cost,i+1)			  #为人员i+1分配任务
            used[j]=False				#回退
            x[i]=-1
            cost-=c[i][j]

def allocate2(c,n):     #求解任务分配问题
    global x,bestx,bestc,used,sum
    x=[0]*n
    bestx=[0]*n
    bestc=INF                           #初始化为∞
    used=[False]*n
    sum=0
    dfs2(0,0);							#从人员0开始
    print("求解结果")
    for k in range(0,n):
        print("   人员%d分配任务%d"%(k,bestx[k]))
    print("   总成本=",bestc)
    print("sum=",sum)


n=4
c=[[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
allocate1(c,n)
