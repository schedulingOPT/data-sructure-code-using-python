class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.INF=0x3f3f3f3f
        n=len(points)
        if n==1:return 0
        if n==2:return self.distance(points,0,1)
        return self.Prim(points,n,0)

    def distance(self,p,i,j):   					#求p[i]和p[j]的曼哈顿距离
        return abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])

    def Prim(self,p,n,v):					#Prim算法
        lowcost=[self.INF]*n
        U=[0]*n
        closest=[0]*n
        for j in range(0,n):	#给初始化lowcost和closest数组
            lowcost[j]=self.distance(p,v,j)
            closest[j]=v
        ans=0;             							#存放最小生成树的长度
        U[v]=1                             			#源点加入U 
        for i in range(1,n):         				#找出(n-1)个顶点
            mincost=self.INF
            k=-1 
            for j in range(0,n):					#在(V-U)中找出离U最近的顶点k
                if U[j]==0 and lowcost[j]<mincost:
                    mincost=lowcost[j]
                    k=j 				#k记录最近顶点的编号
            ans+=mincost							#产生最小生成树的一条边
            U[k]=1                                  #顶点k加入U 
            for j in range(0,n): 					#修改数组lowcost和closest
                if U[j]==0 and self.distance(p,k,j)<lowcost[j]:
                    lowcost[j]=self.distance(p,k,j)
                    closest[j]=k
        return ans


class UFS():									#并查集类
    MAXN=1005
    def __init__(self):    
        self.parent=[0]*self.MAXN                   #并查集存储结构
        self.rnk=[-1]*self.MAXN;                    #存储结点的秩(近似于高度)
    def Init(self,n):                               #并查集初始化
        for i in range(0,n):
            self.parent[i]=i
            self.rnk[i]=0
    def Find(self,x):                                #递归算法：并查集中查找x结点的根结点
        if x!=self.parent[x]:
            self.parent[x]=self.Find(self.parent[x])        #路径压缩
        return self.parent[x]
    def Union(self,x,y):                        #并查集中x和y的两个集合的合并
        rx,ry=self.Find(x),self.Find(y)
        if rx==ry:                                  #x和y属于同一棵树时返回
            return
        if self.rnk[rx]<self.rnk[ry]:
            self.parent[rx]=ry                                          #rx结点作为ry的孩子
        else:
            if self.rnk[rx]==self.rnk[ry]:          #秩相同，合并后rx的秩增1
                self.rnk[rx]+=1
            self.parent[ry]=rx                  #ry结点作为rx的孩子

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.INF=0x3f3f3f3f
        n=len(points)
        if n==1:return 0
        if n==2:return self.distance(points,0,1)
        return self.Kruskal(points,n)

    def distance(self,p,i,j):    		#求p[i]和p[j]的曼哈顿距离
        return abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])

    def Kruskal(self,p,n):     		#Kruskal算法
        ufs=UFS() 
        E=[]        
        for i in range(0,n):   	#由A下三角部分产生的边集E
            for j in range(0,i):
                E.append([i,j,self.distance(p,i,j)])
        E.sort(key=itemgetter(2))           #按边权值递增排序
        ans=0
        ufs.Init(n)           					#初始化并查集
        k,j=0,0         			            #k表示当前构造生成树的边数
        while k<n-1:   			                #生成的边数小于n-1时循环
            u1,v1=E[j][0],E[j][1]               #取一条边(u1,v1)
            sn1,sn2=ufs.Find(u1),ufs.Find(v1)   #两个顶点所属的集合编号
            if sn1!=sn2:      	                #添加该边不会构成回路
                ans+=E[j][2]    	#产生最小生成树的一条边
                k+=1          			#生成边数增1
                ufs.Union(sn1,sn2)     		#将sn1和sn2两个顶点合并
            j+=1         				#遍历下一条边
        return ans
