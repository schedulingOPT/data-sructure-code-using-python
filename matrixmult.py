def matrixchain(p,n): 	#求dp和s 
    global dp,s
    dp=[[0]*(n+1) for i in range(n+1)]      #二维动态规划数组
    s=[[0]*(n+1) for i in range(n+1)]       #存放最优分割点
    len=2
    while len<=n:  #按长度len枚举区间[i,j]
        i=1
        while i+len-1<=n:
            j=i+len-1
            #print("len=%d,i=%d"%(len,i))
            dp[i][j]=dp[i+1][j]+p[i-1]*p[i]*p[j]
            #print("dp[%d][%d]=dp[%d][%d]+%d*%d*%d=%d"%(i,j,i+1,j,p[i-1],p[i],p[j],dp[i][j]))
            s[i][j]=i
            for m in range(i+1,j):              	#枚举分割点m(不包含i和j)
                tmp=dp[i][m]+dp[m+1][j]+p[i-1]*p[m]*p[j]
                #print("tmp=dp[%d][%d]+dp[%d][%d]+%d*%d*%d=%d"%(i,m,m+1,j,p[i-1],p[m],p[j],tmp))
                if tmp<dp[i][j]:
                    dp[i][j]=tmp
                    s[i][j]=m
                    #print("修改dp[%d][%d]=tmp=%d"%(i,j,dp[i][j]))
            i+=1
        len+=1
         
def getx(i,j): 			#构造最优解
    if i==j:return  
    getx(i,s[i][j])  
    getx(s[i][j]+1,j)
    print("    A[%d..%d] × A[%d..%d]"%(i,s[i][j],s[i][j]+1,j))

def solve(p,n):				#求解算法
    matrixchain(p,n)
    print("求解结果")
    print("  矩阵最优计算次序:")
    getx(1,n)
    print("  最少数乘次数=",dp[1][n])      
    #print("dp: ")
    #for i in range(1,n+1):
    #    print(dp[i])
    #print("s: ");
    #for i in range(1,n+1):
    #    print(s[i])

n=6						          #矩阵个数
p=[30,35,15,5,10,20,25] 			#矩阵大小
    #int n=3;
    #int p[]={10,100,50,5};
solve(p,n)
