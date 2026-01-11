import copy
class Goods:							     #物品类 
    def __init__(self,x,y,z):
        self.no=x						    #物品的编号
        self.w=y							#物品的重量
        self.v=z							#物品的价值
    def __lt__(self,other):	    		    #用于按v/w递减排序
        return 1.0*self.v/self.w>=1.0*other.v/other.w

def bound(cw,cv,i):		#计算第i层结点的上界函数值
    global g,W,n 
    rw=W-cw						#背包的剩余容量
    b=cv						#表示物品价值的上界值 
    j=i
    while j<n and g[j].w<=rw:	
        rw-=g[j].w						#选择物品j
        b+=g[j].v						#累计价值
        j+=1
    if j<n:						#最后物品k=j+1只能部分装入 
        b+=1.0*g[j].v/g[j].w*rw
    return b
  
def dfs(cw,cv,i):  #回溯算法
    global g,W,n,x,bestx,bestv,sum
    sum+=1
    #print("  当前结点[%d,%d]"%(cw,cv))
    if i>=n:							#到达一个叶子结点
        #print("  找到一个解[%d,%d]"%(cw,cv)) 
        if cw<=W and cv>bestv:				#找到一个满足条件的更优解,保存它
            bestv=cv
            bestx=copy.deepcopy(x)
    else:									#没有到达叶子结点
        if cw+g[i].w<=W:	  #左剪支
            x[i]=1;							#选取物品i
            #print("    扩展左孩子结点[%d,%d]"%(cw+g[i].w,cv+g[i].v))         
            dfs(cw+g[i].w,cv+g[i].v,i+1)
        #else:
        #    print("    左剪支[%d,%d]"%(cw+g[i].w,cv+g[i].v))
        b=bound(cw,cv,i+1)	            #计算限界函数值 
        if b>bestv:			          #右剪支
            x[i]=0;								    #不选取物品i 
            #print("    扩展右孩子结点[%d,%d,b=%.2f]"%(cw,cv,b)) 
            dfs(cw,cv,i+1)
        #else:
        #    print("    右剪支[%d,%d],b=%.2f"%(cw,cv,b))

def knap(g,W):		    #求0/1背包问题
    global n,x,bestx,bestv,sum
    n=len(g)                    #物品个数
    x=[0]*n                     #解向量
    bestx=[0]*n					      #存放最优解向量
    bestv=0 						    #存放最大价值,初始为0
    sum=0									#累计搜索的结点个数 
    print("求解结果")
    #print("排序前")
    #for i in range(0,len(g)):
    #    print("[%d,%d,%d]"%(g[i].no,g[i].w,g[i].v))
    g.sort()
    #print("排序后")
    #for i in range(0,len(g)):
    #    print("[%d,%d,%d]:%.2f"%(g[i].no,g[i].w,g[i].v,1.0*g[i].v/g[i].w))
    dfs(0,0,0);				                              #i从0开始
    for i in range(0,n):
        if bestx[i]==1:print("  选取第%d个物品"%(g[i].no))
    print("  总重量=%d,总价值=%d"%(W,bestv))
    print("sum=",sum)

g=[Goods(0,5,4),Goods(1,3,4),Goods(2,2,3),Goods(3,1,1)]
W=6
knap(g,W)
