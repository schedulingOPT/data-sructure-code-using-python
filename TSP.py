import copy
INF=0x3f3f3f3f
def dfs(d,s,i):	                            #回溯算法
    global A,n,x,bestx,bestd
    if i>=n:								#达到一个叶子结点
        if d+A[x[n-1]][s]<bestd:			#比较求最优解 
            bestd=d+A[x[n-1]][s]			    #求TSP路径长度 
            bestx=copy.deepcopy(x)  #更新bestx
    else:
        for j in range(i,n):				#试探x[i]走到x[j]的分支
            if A[x[i-1]][x[j]]!=0 and A[x[i-1]][x[j]]!=INF:	#若x[i-1]到x[j]有边
                if d+A[x[i-1]][x[j]]<bestd:			#剪支
                    x[i],x[j]=x[j],x[i]     #swap(x[i],x[j]
                    dfs(d+A[x[i-1]][x[i]],s,i+1)
                    x[i],x[j]=x[j],x[i]     #swap(x[i],x[j]


def TSP1(A,n,s):	#求解TSP(起始点为s)\
    global x,bestx,bestd
    x=[s]           #x[0]=s,解向量初始化
    for i in range(0,n):			#将非s的顶点添加到x中
        if i==s:continue
        x.append(i)
    bestx=[0]*n
    bestd=INF
    dfs(0,s,1)
    bestx.append(s)			            #末尾添加起始点
    print("求解结果")
    print("  最短路径: ",end='')					#输出最短路径
    for j in range(0,len(bestx)):
        if j==0:print(bestx[j],end='')
        else:print("->%d"%(bestx[j]),end='')
    print("\n  路径长度:",bestd)

A=[[0,8,5,36],[6,0,8,5],[8,9,0,5],[7,7,8,0]]
n=4
s=1
#A=[[0,3,2],[5,0,2],[7,4,0]]
#n=3
#s=0
TSP1(A,n,s)
