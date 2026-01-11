import copy
def dfs(w,t,cw,rw,i):                   #回溯算法
    global bestx,bestw,sum
    sum+=1
    print("当前结点[%d,%d]"%(cw,rw))
    if i>=len(w):							#达到一个叶子结点
        print("一个解[%d,%d]"%(cw,rw))
        if cw>bestw:			          #找到一个满足条件的更优解
            bestw=cw		            #保存更优解
            bestx=copy.deepcopy(x)		
    else:								#尚未找完所有集装箱
        rw-=w[i];						#求剩余集装箱的重量和
        if cw+w[i]<=t:			#左孩子结点剪支：选择满足条件的集装箱
            x[i]=1						#选取集装箱i 
            cw+=w[i]					#累计当前所选集装箱的重量和 
            print("   扩展左结点[%d,%d]"%(cw,rw))
            dfs(w,t,cw,rw,i+1)
            cw-=w[i]					#恢复当前所选集装箱的重量和(回溯)
        else:
            print("   左结点被剪支,cw=%d,rw=%d"%(cw+w[i],rw))
        
        if cw+rw>bestw:				#右孩子结点剪支
            x[i]=0						#不选择集装箱i
            print("   扩展右结点[%d,%d],bestw=%d"%(cw,rw,bestw))
            dfs(w,t,cw,rw,i+1)
        else:
            print("   右结点被剪支,cw=%d,rw=%d,bestw=%d"%(cw,rw,bestw))
        rw+=w[i]						#恢复剩余集装箱的重量和(回溯)

def loading(w,t):		#求解简单装载问题
    global x,bestx,bestw,sum
    x=[0]*len(w)                #解向量
    bestx=[0]*len(w)		#存放最优解向量
    bestw=0				#存放最优解的总重量，初始化为0 
    sum=0                      #累计搜索的结点个数
    rw=0
    for e in w:rw+=e
    dfs(w,t,0,rw,0)
    print("求解结果")
    for i in range(0,len(w)):     #输出最优解
        if bestx[i]==1:print("  选取第%d个集装箱"%(i))
    print("  总重量=",bestw)
    print("sum=",sum)


w=[5,2,6,4,3]					#各集装箱重量,不用下标0的元素
t=10
loading(w,t)
