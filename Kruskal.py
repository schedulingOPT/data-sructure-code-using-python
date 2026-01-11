from operator import itemgetter,attrgetter
class UFS():									#并查集类
    MAXN=2005
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

#UFS并查集类参见第2章2.10.2节1～23的代码
INF=0x3f3f3f3f
def Kruskal(A,n):                #Kruskal算法
    T=[]                        #存放最小生成树
    E=[]                            #边集
    for i in range(0,n):		#由A下三角部分产生的边集E
        for j in range(0,i):
            if A[i][j]!=0 and A[i][j]!=INF:
                E.append([i,j,A[i][j]])
    E.sort(key=itemgetter(2))           #按边权值递增排序
    ufs=UFS()                       #定义并查集对象
    ufs.Init(n)						#初始化并查集
    k,j=0,0						#k表示当前构造生成树的边数 
    while k<n-1:					#生成的边数小于n-1时循环
        u1,v1=E[j][0],E[j][1]               #取一条边(u1,v1)
        sn1,sn2=ufs.Find(u1),ufs.Find(v1)   #两个顶点所属的集合编号
        if sn1!=sn2:      	                #添加该边不会构成回路
            T.append([u1,v1,E[j][2]])    	#产生最小生成树的一条边
            k+=1          			#生成边数增1
            ufs.Union(sn1,sn2)     		#将sn1和sn2两个顶点合并
        j+=1         				#遍历下一条边
    return T


def solve(A,n):           #构造一棵最小生成树
    ans=Kruskal(A,n)
    print("一棵最小生成树");    
    for x in ans:
        print("   [%d,%d]:%d"%(x[0],x[1],x[2]),end='')
    print()

#A=[[0,6,INF,INF,INF,1,INF],[6,0,4,INF,INF,INF,3],[INF,4,0,2,INF,INF,INF],
#   [INF,INF,2,0,6,INF,5],[INF,INF,INF,6,0,8,7],[1,INF,INF,INF,8,0,INF],[INF,3,INF,5,7,INF,0]];
#n=7
A=[[0,1,5,8,INF],[1,0,2,INF,1],[5,2,0,3,1],[8,INF,3,0,5],[INF,1,1,5,0]]
n=5

solve(A,n)
