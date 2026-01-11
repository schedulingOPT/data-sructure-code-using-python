def editdist(a,b):		#求a到b的编辑距离 
    m,n=len(a),len(b)
    dp=[[0]*(n+1) for i in range(m+1)]   #二维动态规划数组 
    for i in range(1,m+1): 
        dp[i][0]=i			#把a的i个字符全部删除转换为b
    for j in range(1,n+1):
        dp[0][j]=j			#在a中插入b的全部字符转换为b
    for i in range(1,m+1): 
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1
    return dp[m][n]

a="sfdqxbw"
b="gfdgw"
print("求解结果")
print("    最少的字符操作次数:",editdist(a,b))