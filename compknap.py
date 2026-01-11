def completeknap(w,v,n,W):				#求解完全背包问题
    global dp,fk
    dp=[[0]*(W+1) for i in range(n+1)]
    fk=[[0]*(W+1) for i in range(n+1)]
    for i in range(1,n+1):
        for r in range(0,W+1):
            k=0
            while k*w[i-1]<=r:
                if dp[i][r]<dp[i-1][r-k*w[i-1]]+k*v[i-1]:
                    dp[i][r]=dp[i-1][r-k*w[i-1]]+k*v[i-1]  #物品i-1取k件
                    fk[i][r]=k
                k+=1
    return dp[n][W]

def getx():												#回推求一个最优方案
    i,r=n,W
    while i>=1:
        print("  选择物品%d共%d件"%(i-1,fk[i][r]))
        r-=fk[i][r]*w[i-1]											#剩余重量
        i-=1
  
def solve(w,v,n,W):   #求解算法
    print("求解结果")
    print("  最大价值",completeknap(w,v,n,W))
    getx()

def completeknap1(w,v,n,W):						#时间改进算法
    dp=[[0]*(W+1) for i in range(n+1)]
    for i in range(1,n+1):
        for r in range(0,W+1):
            if r<w[i-1]:											#物品i-1放不下
                dp[i][r]=dp[i-1][r];
            else:														#在不选择和选择物品i-1（多次）中求最大值
                dp[i][r]=max(dp[i-1][r],dp[i][r-w[i-1]]+v[i-1])
    return dp[n][W]			#返回总价值
  
def completeknap2(w,v,n,W):					#空间改进算法
    dp=[0]*(W+1)								#一维动态规划数组
    for i in range(1,n+1):
        for r in range(w[i-1],W+1):     #r按w[i-1]到W的顺序
            dp[r]=max(dp[r],dp[r-w[i-1]]+v[i-1])
    return dp[W]

def solve1(w,v,n,W):   #求解算法
    print("求解结果")
    print("  最大价值",completeknap2(w,v,n,W))

n,W=3,7
w=[3,4,2]
v=[4,5,3]
    #int n=2,W=3;					#5种物品,限制重量不超过10
    #int w[]={2,1};
    #int v[]={3,6};
solve(w,v,n,W)
