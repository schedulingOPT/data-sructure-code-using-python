import copy
INF=0x3f3f3f3f                #表示∞
def dfs3(cost,i):				#回溯算法
    global c,n,x,bestx,bestc,used,sum
    sum+=1 
    if i>=n:			            #到达一个叶子结点
        if cost<bestc:		        #比较求最优解
            bestc=cost
            bestx=copy.deepcopy(x)
    else:
        for j in range(i,n):					#为人员i试探任务x[j]
            if used[x[j]]:continue			        #跳过已经分配的任务j
            x[i],x[j]=x[j],x[i]					#swap(x[i],x[j]):为人员i分配任务x[j]
            used[x[i]]=True
            cost+=c[i][x[i]]
            if bound(cost,i+1)<bestc:			#剪支
                dfs3(cost,i+1)				    #继续为人员i+1分配任务
            cost-=c[i][x[i]]					#cost回溯
            used[x[i]]=False					#used回溯
            x[i],x[j]=x[j],x[i]                 #x回溯
  
def bound(cost,i):							#求下界算法
    global c,n,x,used
    minsum=0
    for i1 in range(i,n):				#求c[i..n-1]行中最小元素和
        minc=INF
        for j1 in range(0,n):
            if not used[x[j1]] and c[i1][x[j1]]<minc:minc=c[i1][x[j1]]
        minsum+=minc
    return cost+minsum

def allocate3(c,n):     				#求解任务分配问题
    global x,bestx,bestc,used,sum
    x=[]
    for i in range(0,n):x.append(i)     #初始化解向量x
    bestx=[0]*n                         #最优解向量
    bestc=INF                           #最优成本初始化为∞
    used=[False]*n
    sum=0
    dfs3(0,0);							#从人员0开始
    print("求解结果")
    for k in range(0,n):
        print("   人员%d分配任务%d"%(k,bestx[k]))
    print("   总成本=",bestc)
    print("sum=",sum)


n=4
c=[[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
allocate3(c,n)
