INF=0x3f3f3f3f
def Floyd1(A):			#Floyd算法
    global dp
    n=len(A)
    dp=[[[INF]*n for i in range(n)] for j in range(n+1)]	#三维动态规划数组
    for i in range(0,n):						#求B(-1)
        for j in range(0,n):
            dp[0][i][j]=A[i][j]
    for k in range(1,n+1):					#依次求B(0)到B(n-1)
        for i in range(0,n):
            for j in range(0,n):
                dp[k][i][j]=min(dp[k-1][i][j],dp[k-1][i][k-1]+dp[k-1][k-1][j])

def Floyd(A):
    global dp
    n=len(A)
    dp=[[INF]*n for i in range(n)]  #二维动态规划数组
    for i in range(0,n):        #求B(-1)
        for j in range(0,n):
            dp[i][j]=A[i][j]
    for k in range(0,n):       #依次求B(0)到B(n-1)
        for i in range(0,n):
            for j in range(0,n):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])

A=[[0,5,INF,7],[INF,0,4,2],[3,3,0,2],[INF,INF,1,0]]
n=len(A)
print("三维dp")
Floyd1(A)
for i in range(0,n):
    for j in range(0,n):
        print("%3d"%(dp[n][i][j]),end='')
    print()
print("二维dp")
Floyd(A)
for i in range(0,n):
    for j in range(0,n):
        print("%3d"%(dp[i][j]),end='')
    print()

