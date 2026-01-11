INF=0x3f3f3f3f
def Prim(A,n,v):                #Prim算法
    T=[]                        #存放最小生成树
    lowcost=[INF]*n
    U=[0]*n
    closest=[0]*n
    for j in range(0,n):        #初始化lowcost和closest数组
        lowcost[j]=A[v][j]
        closest[j]=v
    U[v]=1								#源点加入U 
    for i in range(1,n):			#找出(n-1)个顶点
        mincost,k=INF,-1
        for j in range(0,n):		#在(V-U)中找出离U最近的顶点k
            if U[j]==0 and lowcost[j]<mincost:
                mincost=lowcost[j]
                k=j					#k记录最近顶点的编号
        T.append([closest[k],k,mincost])      #产生最小生成树的一条边
        U[k]=1									        #顶点k加入U 
        for  j in range(0,n):					#修改数组lowcost和closest
            if U[j]==0 and A[k][j]<lowcost[j]:
                lowcost[j]=A[k][j]
                closest[j]=k
    return T

def solve(A,n,v):           #构造一棵最小生成树
    ans=Prim(A,n,v)
    print("一棵最小生成树");    
    for x in ans:
        print("   [%d,%d]:%d"%(x[0],x[1],x[2]),end='')
    print()

#A=[[0,6,INF,INF,INF,1,INF],[6,0,4,INF,INF,INF,3],[INF,4,0,2,INF,INF,INF],
#   [INF,INF,2,0,6,INF,5],[INF,INF,INF,6,0,8,7],[1,INF,INF,INF,8,0,INF],[INF,3,INF,5,7,INF,0]]
#n=7
#v=0
A=[[0,1,5,8,INF],[1,0,2,INF,1],[5,2,0,3,1],[8,INF,3,0,5],[INF,1,1,5,0]]
n=5
v=0
solve(A,n,v)
