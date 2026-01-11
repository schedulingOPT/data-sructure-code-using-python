def multiknap(w,v,n,W):				#求解多重背包问题
    global dp
    dp=[[0]*(W+1) for i in range(n+1)]	#二维动态规划数组
    for i in range(1,n+1):
        for r in range(0,W+1):
            k=0
            while k<=s[i-1]:
                if k*w[i-1]<=r:							#不超重时
                    dp[i][r]=max(dp[i][r],dp[i-1][r-k*w[i-1]]+k*v[i-1])
                k+=1
    return dp[n][W]
