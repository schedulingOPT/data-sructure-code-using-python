import heapq
class HTreeNode:			#哈夫曼树结点类型
    def __init__(self,d,w):             #构造方法
        self.val=d					    #结点对应的字符
        self.weight=w					#权值
        self.parent=-1					#双亲的位置
        self.left=-1					#左孩子的位置
        self.right=1					#右孩子的位置

class QNode:		        #优先队列结点类
    def __init__(self):
        self.no=-1	        #对应哈夫曼树ht中的位置
        self.weight=0       #权值
    def __lt__(self,other):	    #指定按weight越小越优先出队
        if self.weight<other.weight:return True
        else:return False

def CreateHTree(d,w,n):				#构造哈夫曼树
    global ht
    ht=[None]*(2*n-1)
    for i in range(0,n):
        ht[i]=HTreeNode(d[i],w[i])
    minpq=[]      #小根堆
    for i in range(0,n):		#将n个结点进队
        e=QNode()
        e.no,e.weight=i,ht[i].weight
        heapq.heappush(minpq,e)

    for j in range(n,2*n-1):	#构造哈夫曼树的n-1个非叶结点
        e1=heapq.heappop(minpq)		#出队权值最小的结点e1
        e2=heapq.heappop(minpq) 	#出队权值次小的结点e2
        ht[j]=HTreeNode(' ',e1.weight+e2.weight) #构造哈夫曼树非叶结点j	
        ht[j].left=e1.no
        ht[j].right=e2.no
        ht[e1.no].parent=j			#修改e1.no的双亲为结点j
        ht[e2.no].parent=j			#修改e2.no的双亲为结点j
        e=QNode()
        e.no,e.weight=j,e1.weight+e2.weight  #构造队列结点e
        heapq.heappush(minpq,e)

def CreateHCode():			#构造哈夫曼编码
    global htcode
    htcode={}               #用字典存放哈夫曼编码
    for i in range(0,n):	#构造叶结点i的哈夫曼编码
        code="";
        curno=i;
        f=ht[curno].parent
        while f!=-1:		#循环到根结点
            if ht[f].left==curno:	#curno为双亲f的左孩子
                code='0'+code
            else:					#curno为双亲f的右孩子
                code='1'+code
            curno=f; f=ht[curno].parent;
        htcode[ht[i].val]=code	  #得到ht[i].val字符的哈夫曼编码

def DispHTree():					#输出哈夫曼树
    for i in range(0,2*n-1):
        print("    val=%2c,weight=%2d,left=%2d,right=%2d,parent=%2d"%(ht[i].val,ht[i].weight,ht[i].left,ht[i].right,ht[i].parent))

def DispHCode():					      #输出哈夫曼编码
    for c in htcode.keys():
        print("  ",c,":",htcode[c])

d=['a','b','c','d','e']
w=[4,2,1,7,3]
n=5
CreateHTree(d,w,n)					#建立哈夫曼树
print("构造的哈夫曼树")
DispHTree()
CreateHCode()					    #求哈夫曼编码
print("产生的哈夫曼编码如下")
DispHCode()					      #输出哈夫曼编码