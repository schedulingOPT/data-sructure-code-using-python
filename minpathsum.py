def minPathSum(a):	                #自顶向下求最小路径和
    n=len(a)
    dp=[[0]*n for i in range(n)]    #二维动态规划数组
    dp[0][0]=a[0][0];
    for i in range(1,n):				#考虑第0列的边界
        dp[i][0]=dp[i-1][0]+a[i][0]
    for i in range(1,n):        #考虑对角线的边界
        dp[i][i]=a[i][i]+dp[i-1][i-1]
    for i in range(2,n):		    #考虑其他有两条达到路径的结点
        for j in range(1,i):
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+a[i][j]
    ans=min(dp[n-1])            #求出dp[n-1]中最小元素ans
    return ans

def minPathSum1(a):	                #求最小路径和以及一条最小和路径
    n=len(a)
    dp=[[0]*n for i in range(n)]    #二维动态规划数组
    pre=[[0]*n for i in range(n)]	  #二维路径数组 
    dp[0][0]=a[0][0]
    for i in range(1,n):			#考虑第0列的边界
        dp[i][0]=dp[i-1][0]+a[i][0]
        pre[i][0]=0
    for i in range(1,n):		#考虑对角线的边界
        dp[i][i]=a[i][i]+dp[i-1][i-1]
        pre[i][i]=i-1
    for i in range(2,n):				#考虑其他有两条达到路径的结点
        for j in range(1,i):
            if dp[i-1][j-1]<dp[i-1][j]:
                pre[i][j]=j-1
                dp[i][j]=a[i][j]+dp[i-1][j-1]
            else:
                pre[i][j]=j
                dp[i][j]=a[i][j]+dp[i-1][j]
    ans,minj=min(dp[n-1]),dp[n-1].index(min(dp[n-1]))   #求出dp[n-1]中最小ans和对应列号minj
    print("  最小路径和ans=",ans)
    i=n-1
    path=[]	#存放一条路径
    while i>=0:                   #从(n-1,minj)位置反推求出反向路径
        path.append(a[i][minj])
        minj=pre[i][minj]					#最小路径在前一行中的列号
        i-=1								#在前一行查找
    path.reverse()          #逆置path
    print("  一条最小路径: ",path)

def minPathSum2(a):	#自底向上求最小路径和
    n=len(a)
    dp=[[0]*n for i in range(n)]    #二维动态规划数组
    for j in range(0,n):
        dp[n-1][j]=a[n-1][j]						#第n-1行 
    for i in range(n-2,-1,-1):						#考虑第0列的边界
        dp[i][0]=dp[i+1][0]+a[i][0]
    for i in range(n-2,-1,-1):							#考虑对角线的边界
        dp[i][i]=a[i][i]+dp[i+1][i+1]
    for i in range(n-2,-1,-1):				#考虑其他有两条达到的路径
        for j in range(0,len(a[i])):
            dp[i][j]=min(dp[i+1][j+1],dp[i+1][j])+a[i][j]
    return dp[0][0]
    
def minPathSum3(a):	      #自底向上的优化算法 
    n=len(a)
    dp=[0]*n              #一维动态规划数组
    for i in range(n-1,-1,-1):
        for j in range(0,len(a[i])):
            if j<len(a)-1:
                dp[j]=min(dp[j],dp[j+1])+a[i][j]
            else:
                dp[j]+=a[i][j]
    return dp[0]

def solve(a):              #求解算法
    print("求解结果")
    #minPathSum1(a)
    ans=minPathSum3(a)
    print("  ans=",ans)     #输出最小路径和

a=[[2],[3,4],[6,5,7],[8,3,9,2]]
solve(a)