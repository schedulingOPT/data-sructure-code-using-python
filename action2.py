class Action:		            #活动类
    def __init__(self,b,e):
        self.b=b                #活动起始时间
        self.e=e                #活动结束时间
        self.length=e-b         #求每个活动的占用时间
    def __lt__(self,other):	    #用于按e递增排序
        if self.e<other.e:return True
        else:return False

def plan(A):		        #求dp
    global dp,pre
    n=len(A)
    dp=[0]*n         #初始化dp元素为0
    pre=[-5]*n
    A.sort()	#按e递增排序
    dp[0]=A[0].length
    pre[0]=-2					        #A[0]没有前驱活动
    for i in range(1,n):
        j=i-1
        while j>=0 and A[j].e>A[i].b:j-=1       #在A[0..i-1]找与A[i]的前驱活动A[j]
        if j==-1:				#A[i]前面没有兼容活动
            dp[i]=A[i].length
            pre[i]=-2			#没有前驱活动
        else:					#A[i]存在前驱活动A[j]
        #dp[i]=max(dp[i-1],dp[j]+A[i].length)
            if dp[i-1]>dp[j]+A[i].length:
                dp[i]=dp[i-1]
                pre[i]=-1		    #不选择A[i]
            else:
                dp[i]=dp[j]+A[i].length
                pre[i]=j		    #选中活动i,前驱活动为A[j] 
    return dp[n-1]

def getx(n):				    #求一个最优方案
    x=[]    	            #存放一个方案 
    i=n-1					#从n-1开始
    while True:
        if i==-2:break		#A[i]没有前驱活动
        if pre[i]==-1:i-=1	#不选择A[i]
        else:				#选择A[i]
            x.append(i)
            i=pre[i]
    x.reverse()     	#逆置x
    return x

def solve(A):       #求解算法
    n=len(A)
    print("求解结果")
    ans=plan(A)
    x=getx(n)
    print("   x: ",x)
    print("   选择的活动:",end='')
    for i in range(0,len(x)):
        print("%d[%d,%d] "%(x[i],A[x[i]].b,A[x[i]].e),end=' ')
    print()
    print("   最长兼容活动的总时间:",ans)


A=[Action(1,4),Action(3,5),Action(0,6),Action(5,7),Action(3,8),Action(5,9),Action(6,10),Action(8,11),Action(8,12),Action(2,13),Action(12,15)]

#A=[Action(1,6),Action(6,8),Action(1,10),Action(8,12)]	#存放活动
#A=[Action(4,6),Action(6,8),Action(1,10),Action(6,12)]	#存放活动
solve(A)