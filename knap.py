class Goods:							     #物品类 
    def __init__(self,x,y,z):
        self.no=x						    #物品的编号
        self.w=y							#物品的重量
        self.v=z							#物品的价值
    def __lt__(self,other):	    		    #用于按v/w递减排序
        return 1.0*self.v/self.w>=1.0*other.v/other.w

def greedly(g,W):		                #贪心算法
    global x,bestv
    n=len(g)
    g.sort()        #按v/w递减排序
    x=[0]*n             #存放最优解向量
    bestv=0					            #存放最大价值,初始为0
    rw=W								      #背包中能装入的余下重量
    i=0
    while i<n and g[i].w<rw:		#物品i能够全部装入时循环
        x[i]=1									#装入物品i
        rw-=g[i].w							#减少背包中能装入的余下重量
        bestv+=g[i].v						#累计总价值
        i+=1									#继续循环
    if i<n and rw>0:						#当余下重量大于0
        x[i]=rw/g[i].w						#将物品i的一部分装入
        bestv+=x[i]*g[i].v					#累计总价值

def knap(g,W):		                    #求解背包问题
    greedly(g,W)
    print("求解结果")		                #输出结果
    for j in range(0,len(g)):
        if x[j]==1:print("  选择%d[%d,%d]物品的比例是1"%(g[j].no,g[j].w,g[j].v))
        elif x[j]>0:print("  选择%d[%d,%d]物品的比例是%.1f"%(g[j].no,g[j].w,g[j].v,x[j]))
    print("  总价值=%d"%(bestv))

g=[Goods(0,10,20),Goods(1,20,30),Goods(2,30,66),Goods(3,40,40),Goods(4,50,60)]
W=100
knap(g,W)
