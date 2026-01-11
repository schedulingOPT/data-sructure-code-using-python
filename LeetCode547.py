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
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        ufs=UFS()
        ufs.Init(n)
        for i in range(0,n):                            #读取矩阵上三角部分
            for j in range(i+1,n):
                if isConnected[i][j]==1:ufs.Union(i,j)
        ans=0
        for i in range(0,n):
            if ufs.parent[i]==i:ans+=1
        return ans
