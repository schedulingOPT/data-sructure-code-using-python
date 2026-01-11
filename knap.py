def knap(w,v,n,W):			#动态规划法求0/1背包问题
    global dp
    dp=[[0]*(W+1) for i in range(n+1)]  #二维动态规划数组
    for i in range(0,n):	#置边界条件dp[i][0]=0
        dp[i][0]=0
    for r in range(0,W+1):#置边界条件dp[0][r]=0
        dp[0][r]=0
    for i in range(1,n+1):
        for r in range(0,W+1):
            if r<w[i-1]:			
                dp[i][r]=dp[i-1][r]
            else:
                dp[i][r]=max(dp[i-1][r],dp[i-1][r-w[i-1]]+v[i-1])
    return dp[n][W]


def getx(w):			#回推求一个最优方案
    global x
    x=[0]*n
    i,r=n,W
    while i>=1:
        if dp[i][r]!=dp[i-1][r]:
            x[i-1]=1				  #选取物品i-1
            r=r-w[i-1]
        else:
            x[i-1]=0				  #不选取物品i-1
        i-=1
    
def solve(w,v,n,W):         #求解算法
    print("求解结果")
    print("  最大价值",knap(w,v,n,W))
    getx(w)
    for i in range(0,n):
        if x[i]==1:print("  选择物品%d:[%d,%d]"%(i,w[i],v[i]),end=' ');
  
def knap1(w,v,n,W):					    #改进算法
    dp=[0]*(W+1)						#一维动态规划数组
    for i in range(1,n+1):
        for r in range(W,-1,-1):	    #r按0到W的逆序（重点）
            if r<w[i-1]:dp[r]=dp[r]
            else:dp[r]=max(dp[r],dp[r-w[i-1]]+v[i-1])
    return dp[W]

def knap2(w,v,n,W):					#改进算法
    dp=[0]*(W+1)						#一维动态规划数组
    for i in range(1,n+1):
        for r in range(W,w[i-1]-1,-1):	    #r按w[i-1]到W的逆序（重点）
            dp[r]=max(dp[r],dp[r-w[i-1]]+v[i-1])
    return dp[W]
 
def solve1(w,v,n,W):   #求解算法
    print("求解结果")
    print("  最大价值",knap2(w,v,n,W))

n,W=5,10			#5种物品,限制重量不超过10
w=[2,2,6,5,4]
v=[6,3,5,4,6]
solve(w,v,n,W)
